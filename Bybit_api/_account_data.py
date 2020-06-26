from . import _endpoints as endpoints

def place_order(self, symbol, side, order_type, qty, price=None, 
    time_in_force='GoodTillCancel', take_profit=None, stop_loss=None,
    reduce_only=False, close_on_trigger=False, order_link_id=None):
    """ Place an active order,

        Parameters
        ----------
        symbol : str
            The symbol on which to execute the order
        side : str
            The side of the order, 'Buy', 'Sell'
        order_type : str
            The type of the order. 'Market', 'Limit'
        qty : int
            The Order quantity in BTC (if is a USDT contract).
            Or usd if an inverse contract.
        price : float, Optional
            The price of the order. REQUIRED if order_type = 'Limit'
            (default is None)
        time_in_force : str, optional
            The time in force for the order.
            (default is 'GoodTillCancel')
        take_profit : float, optional
            Take profit price. Only takes effect after opening the position
            (default is None)
        stop_loss : float, optional
            It is the price at which to stop the order, only take effect after
            opening the position.
            (default is None)
        reduce_only : bool, optional
            True means your position can only reduce in size if this order is triggered
            (default is False)
        close_on_trigger : bool, optional
            For a closing order. It can only reduce your position, not increase it. 
            If the account has insufficient available balance when the closing order
            is triggered, then other active orders of similar contracts will be cancelled
            or reduced. It can be used to ensure your stop loss reduces your position
            regardless of current available margin.
            (default is False)
        order_link_id : str, optional
            Customize your order ID. The max is at 36 char. Order ID must be unique

        Returns
        -------
            Response from endpoint
    
    """
    
    url = self.base_endpoint + endpoints.place_order
    params = {
        'side': side,
        'symbol': symbol,
        'order_type': order_type,
        'qty': qty,
        'price': price,
        'time_in_force': time_in_force,
        'take_profit': take_profit,
        'stop_loss': stop_loss,
        'reduce_only': reduce_only,
        'close_on_trigger': close_on_trigger,
        'order_link_id': order_link_id
    }

    return self._send_request(method="POST", url=url, params=params, auth=True)

def get_active_order(self, symbol, order_id=None, order_link_id=None, order=None,
    page=1, limit=200, order_status=None):

    url = self.base_endpoint + endpoints.get_order

    params = {
        'order_id': order_id,
        'order_link_id': order_link_id,
        'symbol': symbol,
        'order': order,
        'page': page,
        'limit': limit,
        'order_status': order_status
    }

    return self._send_request(method="GET", url=url, params=params, auth=True)

def cancel_all_orders(self, symbol):

    url = self.base_endpoint + endpoints.cancel_all_orders

    params = {
        'symbol': symbol
    }

    return self._send_request(method="POST", url=url, params=params, auth=True)

def replace_order(self, order_id, symbol, p_r_qty=None, p_r_price=None):

    url = self.base_endpoint + endpoints.replace_order

    params = {
        'order_id': order_id,
        'symbol': symbol,
        'p_r_qty': p_r_qty,
        'p_r_price': p_r_price
    }

    return self._send_request(method='POST', url=url, params=params, auth=True)

def set_trading_stop(self, symbol, side, take_profit=None, stop_loss=None,
    trailing_stop=None):

    url = self.base_endpoint + endpoints.set_trading_stop

    params = {
        'symbol': symbol,
        'side': side,
        'take_profit': take_profit,
        'stop_loss': stop_loss,
        'trailing_stop': trailing_stop
    }

    return self._send_request(method='POST', url=url, params=params, auth=True)

def cross_isolated_switch(self, symbol, is_isolated, buy_leverage, sell_leverage):
    
    url = self.base_endpoint + endpoints.cross_isolated_margin_switch

    params = {
        'symbol': symbol,
        'is_isolated': is_isolated,
        'buy_leverage': buy_leverage,
        'sell_leverage': sell_leverage
    }

    return self._send_request(method='POST', url=url, params=params, auth=True)

def get_positions(self, symbol):
    url = self.base_endpoint + endpoints.positions

    params = {
        'symbol': symbol
    }

    return self._send_request(method='GET', url=url, params=params, auth=True)
