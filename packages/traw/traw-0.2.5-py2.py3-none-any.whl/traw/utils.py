from copy import deepcopy
from datetime import datetime as dt, timedelta
from functools import update_wrapper, wraps
from inspect import isclass
import re

from singledispatch import singledispatch

from .const import DEFAULT_LIMIT


def cacheable_generator(obj_type):
    """ Caching decorator for API generator methods

        If the decorated method has cached objects for that method and argument
        combination and those objects have not expired, the cached objects are
        yielded without calling the underlying method. If there are no objects in
        that method's cache or the objects have expired, the underlying API method
        is called and the resulting objects are then cached and yielded.

        Cache object expiration is based on the obj_type, and defaults to
        traw.const.DEFAULT_CACHE_TIMEOUT (300 seconds). Cache expiry timeouts can
        be adjusted on a per-object bases from the client:

        .. code-block:: python

            client.change_cache_timeout(models.Run, 30)

        The above will set the cache timeout of models.Run objects from 300
        seconds to 30 seconds
    """
    def _cacheable_generator(func):
        """ """
        cache = func.cache = {}

        @wraps(func)
        def cacheable_func(inst, *args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache or cache[key]['expires'] < dt.now():
                returned_vals = list()
                timeout = inst.cache_timeouts[inst][obj_type]
                expires = dt.now() + timedelta(seconds=timeout)
                for val in func(inst, *args, **kwargs):
                    returned_vals.append(val)
                    yield val
                else:  # pylint: disable=useless-else-on-loop
                    # Only cache results if the generator has been exhausted
                    cache[key] = dict()
                    cache[key]['value'] = returned_vals
                    cache[key]['expires'] = expires
            else:
                for val in cache[key]['value']:
                    yield val

        return cacheable_func
    return _cacheable_generator


def cacheable(obj_type):
    """ Caching decorator for API methods that return a single object

        If the decorated method has a cached object for that method and argument
        combination and that object has not expired, the cached object is
        returned without calling the underlying method. If there is no object in
        that method's cache or the object has expired, the underlying API method
        is called and the resulting object is then cached and returned.

        Cache object expiration is based on the obj_type, and defaults to
        traw.const.DEFAULT_CACHE_TIMEOUT (300 seconds). Cache expiry timeouts can
        be adjusted on a per-object bases from the client:

        .. code-block:: python

            client.change_cache_timeout(models.Run, 30)

        The above will set the cache timeout of models.Run objects from 300
        seconds to 30 seconds
    """
    def cacheable_func(func):
        """ """
        cache = func.cache = {}

        @wraps(func)
        def _cacheable_func(inst, *args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache or cache[key]['expires'] < dt.now():
                timeout = inst.cache_timeouts[inst][obj_type]
                cache[key] = dict()
                cache[key]['value'] = func(inst, *args, **kwargs)
                cache[key]['expires'] = dt.now() + timedelta(seconds=timeout)

            return cache[key]['value']

        return _cacheable_func
    return cacheable_func


def clear_cache(method):
    """ API method decorator for API methods that POST to the TestRail API

        When TRAW adds/closes/deletes/updates ojects to the TestRail API, any
        objects of the same type that are currently cached by TRAW are
        considered stale. To insure TRAW does not return a cached object that
        has been modified on the TestRail side, ``clear_cache`` is used to
        clear the cache of any API method that works with that same object
        type.

        For instance, if ``traw.api.project_by_id`` has been decorated with the
        ``@cacheable`` decorator, then any API method that POSTs changes to the
        TestRail API for models.Project objects should be decorated with
        ``@clear_cache(project_by_id)``

        .. code-block:: python

            class API(object):

                @cacheable
                def foo_by_id(self, foo_id):
                    # ...
                    return foo

                @cacheable_generator
                def foos(self):
                    # ...
                    yield from foo_list

                @clear_cache(foo_by_id)
                @clear_cache(foos)
                def add_foo(self, new_foo):
                    # ...
                    return new_foo_response

        The method cache is only cleared if the reponse is successful;
        exceptions raises from the actual call to TestRail's API will not clear
        the cache.

    """
    def target(func):
        @wraps(func)
        def _func(*args, **kwargs):
            response = func(*args, **kwargs)
            method.cache.clear()
            return response
        return _func
    return target


def dispatchmethod(func):
    """ singledispatch for class methods

    This provides for a way to use ``functools.singledispatch`` inside of a class.
    It has the same basic interface that ``singledispatch`` does.
    """
    # This implementation builds on the following gist:
    # https://gist.github.com/adamnew123456/9218f99ba35da225ca11
    dispatcher = singledispatch(func)

    def register(type):  # pylint: disable=redefined-builtin
        def _register(func):
            return dispatcher.register(type)(func)

        return _register

    def dispatch(type):  # pylint: disable=redefined-builtin
        return dispatcher.dispatch(type)

    def wrapper(inst, *args, **kwargs):
        obj = args[0] if len(args) > 0 else inst
        cls = obj if isclass(obj) else obj.__class__
        impl = dispatch(cls)
        return impl(inst, *args, **kwargs)

    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = dispatcher.registry
    wrapper._clear_cache = dispatcher._clear_cache  # pylint: disable=protected-access
    update_wrapper(wrapper, func)
    return wrapper


def duration_to_timedelta(duration):
    def timespan(segment):
        return int(segment.group(0)[:-1]) if segment else 0

    timedelta_map = {
        'weeks': timespan(re.search(r'\d+w', duration)),
        'days': timespan(re.search(r'\d+d', duration)),
        'hours': timespan(re.search(r'\d+h', duration)),
        'minutes': timespan(re.search(r'\d+m', duration)),
        'seconds': timespan(re.search(r'\d+s', duration))
    }
    return timedelta(**timedelta_map)


def paginate(func):
    """ """
    @wraps(func)
    def paginated_func(*args, **kwargs):
        limit = kwargs.get('limit', None)
        offset = 0

        keep_paging = True
        while keep_paging:
            new_kwargs = deepcopy(kwargs)
            new_kwargs['offset'] = offset
            if limit:
                new_kwargs['limit'] = min([limit - offset, DEFAULT_LIMIT])

            obj_count = 0
            for obj_count, obj in enumerate(func(*args, **new_kwargs), 1):
                yield obj

                if limit and obj_count + offset >= limit:
                    break

            offset = offset + obj_count
            if limit and offset >= limit:
                keep_paging = False
            elif limit is None and DEFAULT_LIMIT > obj_count:
                # If obj_count is less than the paging size (DEFAULT_LIMIT),
                # it indicates that there are no more objects for the API
                # to return
                keep_paging = False

    return paginated_func
