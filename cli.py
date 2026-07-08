import argparse
from bot.clients import TradingClient
from bot.orders import OrderManager
from bot.validators import validate_orders


def main():
    # 1. Setup cli parser
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")
    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", required=True,
                        choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument('--type',
                        choices=['MARKET', 'LIMIT',
                                 'STOP', 'TAKE_PROFIT_LIMIT'],
                        required=True,
                        help='Order type')
    parser.add_argument("--quantity", required=True,
                        type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float,
                        help="Price (Required for limit orders)")
    parser.add_argument("--stopPrice", type=float, help="Stop price for trigger")

    args = parser.parse_args()

    # 2. validate the inputs
    try:
        validate_orders(args.symbol, args.side, args.type,
                        args.quantity, args.price)
    except ValueError as e:
        print(f"Validation Error: {e}")
        return  # Stop the bot if validation fails
    # 3. Initialize the client
    bot_client = TradingClient()
    bot_client.start()

    # 3. Initialize the ordermanager with the client
    if bot_client.client:
        manager = OrderManager(bot_client.client)

        # 4. Execute the order
        # In cli.py, where you call the order manager:
        manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stopPrice
        )
    else:
        print("Failed to initialize client. Order placement aborted.")


if __name__ == "__main__":
    main()
