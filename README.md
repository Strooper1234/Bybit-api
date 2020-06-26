# Bybit-api
I didn't like the original api for python so I decided to create my own, more intuitive and that makes sense.
Currently working only for BTCUSDT endpoints.

# How to use it

## To create the object that connects to bybit:
import Bybit_api
client = Bybit_api.BybitClient(api_key, api-secret)

I separate the code in different files for better readibility and a clean code, but you can still use the function as they are under one file
ex:
res = client.get_positions(symbol="BTCUSDT")

Even though the method get_positions() is in another file. You can still use it in this way because of the imports of the fucntion to the main file (__init__.py).

