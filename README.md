# Bybit-api
I didn't like the original Bybit python api connection package (many reasons, but there are major bugs) so I decided to create my own, more intuitive and that makes sense.
Currently working only for BTCUSDT endpoints.

**Update:** This project its not finished because recently ByBit release the Documentation and the Python library doesn't have major bugs anymore. Although I much prefer the architecture of my version, there is not reason for me to continue development for these api connection.

# How to use it

## To create the object that connects to bybit:
##### import Bybit_api
##### client = Bybit_api.BybitClient(api_key, api-secret)

I separate the code in different files for better readibility and a clean code, but you can still use the function as they are under one file
ex:
##### res = client.get_positions(symbol="BTCUSDT")

Even though the method get_positions() is in another file. You can still use it in this way because of the imports of the fucntion to the main file (\_\_init__.py).

