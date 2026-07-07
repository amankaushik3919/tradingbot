def validate_orders(symbol, side, order_type, quantity, price=None):
    """ Basic input check that user inputs are correct. """
    if quantity<=0:
        raise ValueError("Quantity must be greater than zero.")
    
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    if order_type.upper()=="LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders.")
    return True