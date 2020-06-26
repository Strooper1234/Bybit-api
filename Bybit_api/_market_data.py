from . import _endpoints as endpoints

def get_kline(self, symbol, interval, from_time, limit=200):
    """ Gets the KLine of the symbol, which is the historic data
    Parameters
    ----------
    symbol : str
        The symbol from which to get the KLine
    interval : str
        The minute interval to get, '1', '3', '5', '10', '15' ...
    from_time : int
        The time in Unix UTC format from when to start
    limit : int, optional
        The number of data point to get, this endpoint has a max return of 200 points
        (default is 200)
    
    Returns
    -------
    json
        The json response from the endpoint.
    """
    url = self.base_endpoint + endpoints.kline
    params = {
        'symbol': symbol,
        'interval': interval,
        'from': from_time,
        'limit': limit
    }

    return self._send_request(method='GET', url=url, params=params)

def get_symbol_info(self, symbol):

    url = self.base_endpoint + endpoints.symbol_info

    params = {
        'symbol':symbol
    }

    return self._send_request(method='GET', url=url, params=params)