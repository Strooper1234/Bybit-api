import json, requests

from . import _endpoints as endpoints # all enpoints here!

VERSION = '1.0.0'
class BybitClient:

    """ Import all the functions that this class will have """
    from ._helper import _auth, _send_request, get_server_time
    from ._market_data import get_kline, get_symbol_info
    from ._account_data import place_order, replace_order, get_active_order, cancel_all_orders, set_trading_stop, cross_isolated_switch, get_positions
    from ._wallet_data import get_wallet_balance

    def __init__(self, api_key=None, api_secret=None, timeout=3):
        # Set the base endpoint and the api keys
        self.base_endpoint = endpoints.base_endpoint
        self.api_key = api_key
        self.api_secret = api_secret

        self.timeout = timeout

        # Initialize the requests session
        self.session = requests.Session()
        self.session.headers.update(
            {
                'User-Agent': 'BybitApi-' + VERSION,
                "Content-Type": 'application/json',
                'Accept': 'application/json',
            }
        )
    
    def exit(self):
        ''' Closes the requests session'''
        self.session.close()

    

    
