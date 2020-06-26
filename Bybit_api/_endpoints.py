base_endpoint = "https://api.bybit.com"

""" Market Data Endpoints """
kline = "/public/linear/kline"  # implemented
symbol_info = "/v2/public/tickers"  # implemented


""" Account Data Endpoints """
''' - Active Orders '''
place_order = "/private/linear/order/create"  # implemented
get_order = "/private/linear/order/list"  # implemented
cancel_order = "/private/linear/order/cancel"
cancel_all_orders = "/private/linear/order/cancel-all"
replace_order = "/open-api/order/replace"  # implemeted, not yet tested with BTCUSDT

''' - Position '''
positions = "/private/linear/position/list" # implemented
set_leverage = "/private/linear/position/set-leverage"  # not impemeted cuz using cross margin
cross_isolated_margin_switch = "/private/linear/position/switch-isolated" # implemented, f*** cross margin
set_trading_stop = "/private/linear/position/trading-stop" #implemented

""" Wallet Data Enpoints """
wallet_balance = "/v2/private/wallet/balance" # implemented

server_time = "/v2/public/time" #implemented