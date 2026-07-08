from binance.client import Client
from bot import logging_config as lc
import shutil


class TradingClient:
    def __init__(self):
        self.api_key = lc.API_KEY
        self.api_secret = lc.API_SECRET_KEY
        self.client = None

    def some(self):
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True,
            demo=True
        )
        # Temporary debug
        print(self.client.futures_exchange_info()['symbols'][0]['orderTypes'])

obj = TradingClient()
obj.some()
