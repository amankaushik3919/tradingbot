import datetime
import os
from binance.exceptions import BinanceAPIException, BinanceOrderException


class OrderManager:
    def __init__(self, client_instance):
        self.client = client_instance

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        # 1. Ensure logs directory exists
        if not os.path.exists('logs'):
            os.makedirs('logs')

        # 2. Generate a unique filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"logs/order_{timestamp}.log"

        # 3. Prepare parameters
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': float(quantity)
        }

        if order_type.upper() in ['LIMIT', 'STOP', 'TAKE_PROFIT_LIMIT']:
            if price is None:
                raise ValueError("Price is required for this order type.")
            params['price'] = str(price)
            params['timeInForce'] = 'GTC'

        if stop_price is not None:
            params['stopPrice'] = str(stop_price)
        # 4. Open file and log execution
        with open(filename, 'w') as f:
            def log_and_print(message):
                print(message)
                f.write(message + '\n')

            log_and_print(f"--- Order Request Summary ---")
            log_and_print(
                f"Request: {params['type']} {params['side']} {params['symbol']} Qty: {params['quantity']} Stop Price: {params['stopPrice']}")
            if 'price' in params:
                log_and_print(f"Price: {params['price']}")
            log_and_print("------------------------------")

            try:
                # Actual execution on Binance Futures Testnet [cite: 6, 18]
                response = self.client.futures_create_order(**params)

                log_and_print("\n--- Order Response Details ---")
                log_and_print(f"OrderID: {response.get('orderId')}")
                log_and_print(f"Status: {response.get('status')}")
                log_and_print(f"Executed Qty: {response.get('executedQty')}")
                log_and_print(f"Avg Price: {response.get('avgPrice')}")
                log_and_print("Message: Success")
                return response

            except (BinanceAPIException, BinanceOrderException) as e:
                log_and_print(f"\n[FAILURE] API Error: {e.message}")
            except Exception as e:
                log_and_print(f"\n[FAILURE] Unexpected error: {e}")
