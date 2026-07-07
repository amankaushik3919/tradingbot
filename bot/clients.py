from binance.client import Client
import logging_config as lc
import shutil


class TradingClient:
    def __init__(self):
        self.api_key = lc.API_KEY
        self.api_secret = lc.API_SECRET_KEY
        self.client = None

    def start(self):
        try:
            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret,
                testnet=True
            )
            print(
                f"Initialized Successfull!!\nThis is the server time: {self.client.get_server_time()}"
            )
            columns = shutil.get_terminal_size().columns
            print("Welcome to the Bot".center(columns))

        except Exception as e:
            print(f"Connection failed Error: {e}")


if __name__ == "__main__":
    objectClient = TradingClient()
    objectClient.start()
