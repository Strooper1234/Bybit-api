from . import _endpoints as endpoints

def get_wallet_balance(self, coin):
    
    url = self.base_endpoint + endpoints.wallet_balance

    params = {
        'coin': coin
    }

    return self._send_request(method='GET', url=url, params=params, auth=True)