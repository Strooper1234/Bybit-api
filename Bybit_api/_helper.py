""" Helper functions 
    meant to only be used inside the API,
    User should NOT call this functions, unless really needed
"""

import json, requests, hmac, time

from . import _endpoints as endpoints

def _auth(self, method, params, api_key=None, api_secret=None):
    '''Generates authentication signature per Bybit API specifications.
    Notes
    -------------------
    Since the POST method requires a JSONified dict, we need to ensure
    the signature uses lowercase booleans instead of Python's
    capitalized booleans. This is done in the bug fix below.

    Credits to: https://github.com/verata-veritatis/pybit/blob/4d15d44172803d4415493af5f7aa09507f9094b7/pybit/__init__.py#L1181
    
    '''

    if api_key == None:
        api_key = self.api_key

    if api_secret == None:
        api_secret = self.api_secret

    if api_key is None or api_secret is None:
        raise PermissionError('Authenticated endpoints require keys.')

    # Append required parameters.
    params['api_key'] = api_key
    #params['timestamp'] = int(time.time() * 10**3)
    params['timestamp'] = int(self.get_server_time() * 10**3)

    # Sort dictionary alphabetically to create querystring.
    _val = '&'.join(
        [str(k) + '=' + str(v) for k, v in sorted(params.items()) if
            (k != 'sign') and (v is not None)]
        )

    # Bug fix. Replaces all capitalized booleans with lowercase.
    if method == 'POST':
        _val = _val.replace('True', 'true').replace('False', 'false')

    # Return signature.    
    return str(hmac.new(bytes(api_secret, 'utf-8'), 
        bytes(_val, 'utf-8'), digestmod='sha256').hexdigest())

def _send_request(self, method=None, url=None, params=None, auth=False):

    if auth:
        # authenticate if it is a private endpoint
        signature = self._auth(method=method, params=params)
         # Sort the dictionary alphabetically.
        params = dict(sorted(params.items(), key=lambda x: x))

        # Append the signature to the dictionary.
        params['sign'] = signature

    # Define parameters and log the request.
    if params is not None:
        req_params = {k: v for k, v in params.items() if 
            v is not None}
    else:
        req_params = {}

    # Prepare request; use 'params' for GET and 'data' for POST.
    if method == 'GET':
        r = self.session.prepare_request(
            requests.Request(method, url, params=req_params)
        )
    else:
        r = self.session.prepare_request(
            requests.Request(method, url, data=json.dumps(req_params))
        )

    retries = 5
    while retries:
        try:
            # Send request and return headers with body.
            s = self.session.send(r, timeout=self.timeout)
            # Return dict.
            return s.json()
        except requests.exceptions.RequestException as e:
            last_connection_exception = e
            retries -= 1
            if retries <= 0:
                break
    raise last_connection_exception

def get_server_time(self):
    
    url = self.base_endpoint + endpoints.server_time

    params = {} # empty

    resp = self._send_request(method='GET', url=url, params=params)
    return float(resp["time_now"])