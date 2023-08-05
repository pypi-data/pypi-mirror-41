from copy import deepcopy
import logging
import time

import requests
from retry import retry
from requests.status_codes import codes
from requests.exceptions import ChunkedEncodingError, ConnectionError, ReadTimeout

from .const import BASE_API_PATH, TIMEOUT
from .exceptions import (BadRequest, Conflict, Forbidden, NotFound, RateLimited,
                         Redirect, ServerError, ServiceUnavailableError,
                         TooLarge, UnknownStatusCode)

log = logging.getLogger(__package__)


class Session(object):
    """  """
    RATE_LIMIT_STATUS = 429
    RETRY_EXCEPTIONS = (ChunkedEncodingError, ConnectionError, RateLimited,
                        ServerError, ReadTimeout)
    STATUS_EXCEPTIONS = {codes['bad_gateway']: ServerError,
                         codes['bad_request']: BadRequest,
                         codes['conflict']: Conflict,
                         codes['found']: Redirect,
                         codes['forbidden']: Forbidden,
                         codes['gateway_timeout']: ServerError,
                         codes['internal_server_error']: ServerError,
                         codes['not_found']: NotFound,
                         codes['request_entity_too_large']: TooLarge,
                         codes['service_unavailable']: ServiceUnavailableError,
                         codes['unauthorized']: Forbidden}
    SUCCESS_STATUSES = {codes['created'], codes['ok']}

    def __init__(self, auth, url):
        """ Prepare the connection to the TestRail API

        :param auth: Tuple of username and api_key/password
        :param url: Base url for testrail (e.g. https://<your company>.testrail.net)

        """
        self._auth = auth
        self._url = url

        self._http = requests.Session()
        self._http.headers['Content-Type'] = 'application/json'

    @staticmethod
    def _log_request(**kwargs):
        method = kwargs.get('method', None)
        url = kwargs.get('url', None)
        json = kwargs.get('json', None)
        params = kwargs.get('params', None)
        log.debug('Fetching: {} {}'.format(method, url))
        log.debug('JSON    : {}'.format(json))
        log.debug('Params  : {}'.format(params))

    def _make_request(self, *args, **kwargs):
        kwargs['timeout'] = TIMEOUT
        kwargs['auth'] = self._auth
        response = self._http.request(*args, **kwargs)

        log.debug('Response: {} ({} bytes)'.format(
            response.status_code, response.headers.get('content-length')))

        return response

    @retry(ServiceUnavailableError, tries=17, delay=1, backoff=2)
    @retry(RETRY_EXCEPTIONS, tries=3, delay=1, backoff=2)
    def _request_with_retries(self, *args, **kwargs):
        """  """
        self._log_request(**kwargs)
        response = self._make_request(*args, **kwargs)

        if response.status_code in self.STATUS_EXCEPTIONS:
            log.warning('Caught a ServerError ({0})'.format(response.status_code))
            raise self.STATUS_EXCEPTIONS[response.status_code](response)
        elif response.status_code == codes['no_content']:
            log.warning('Received a response with no content')
            return
        elif response.status_code == self.RATE_LIMIT_STATUS:
            retry_after = int(response.headers['Retry-After'])
            log_msg = 'API rate limit reached. Retrying after {0} seconds'
            log.warning(log_msg.format(retry_after))
            time.sleep(retry_after)
            raise RateLimited(response)
        elif response.status_code not in self.SUCCESS_STATUSES:
            msg = 'Received an unknown response status: {0}'
            log.warning(msg.format(response.status_code))
            raise UnknownStatusCode(response)

        if response.headers.get('content-length') == '0':
            return ''
        else:
            return response.json()

    def close(self):
        """ Close the session """
        self._http.close()

    def request(self, method, path, json=None, params=None):
        """Return the json content from the resource at ``path``.

        :param method: The request verb. E.g., get, post, put.
        :param path: The path of the request. This path will be combined with
            the base TestRail api URL.
        :param json: Object to be serialized to JSON in the body of the
            request.
        :param params: The query parameters to send with the request.

        """
        params = deepcopy(params) or dict()
        url = '/'.join(part.strip('/') for part in [self._url, BASE_API_PATH, path])
        return self._request_with_retries(method=method, json=json, params=params, url=url)
