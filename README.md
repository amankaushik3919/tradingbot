
# Binance Futures Testnet Trading Bot

Lightweight CLI trading bot for Binance Futures (testnet). Provides a minimal command-line interface to place MARKET and LIMIT orders against the Binance testnet using the python-binance client.

**Features**
- Place MARKET and LIMIT orders on Binance Futures (testnet)
- Simple CLI interface for quick testing and automation
- Basic input validation and order management

**Requirements**
- Python 3.8+ (project includes a virtual environment at `binanceApp`)
- Install dependencies:

```powershell

A small command-line trading tool that uses the Binance Python client to place orders on the Binance Futures testnet. It is intended for testing and learning only — do not use with real funds without careful review.

Quick summary
- Place MARKET and LIMIT orders on Binance Futures (testnet).
- Minimal CLI with input validation and order management.

Prerequisites
- Python 3.8 or newer.
- (Optional) Use the included virtual environment at `binanceApp`.
- Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Setup
1. (Optional) Activate the bundled virtual environment on Windows:

```powershell
.\binanceApp\Scripts\activate
```

2. Install dependencies (if not already installed).

3. Create `bot/secrets.txt` with two lines (no extra whitespace):

- Line 1: API key
- Line 2: API secret

Example (`bot/secrets.txt`):

```
YOUR_TESTNET_API_KEY
YOUR_TESTNET_API_SECRET
```

Usage examples
Run from the repository root:

```powershell
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# LIMIT order example:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

Key files
- [cli.py](cli.py): CLI entrypoint — parses args, validates inputs, initializes the client, and places orders.
- [bot/clients.py](bot/clients.py): `TradingClient` — creates the `binance.Client` with `testnet=True`.
- [bot/logging_config.py](bot/logging_config.py): reads `bot/secrets.txt` and exposes `API_KEY`/`API_SECRET_KEY`.
- [bot/orders.py](bot/orders.py): `OrderManager` — builds order parameters and sends them to the Binance futures API.
- [bot/validators.py](bot/validators.py): input validation helpers.

Troubleshooting
- If the program cannot read keys, ensure `bot/secrets.txt` has exactly two non-empty lines and no extra whitespace.
- Run the CLI from the project root (`python cli.py ...`) so imports resolve correctly.
- The client is configured for testnet; verify keys and endpoints match testnet credentials.

Security
- Secrets are stored in plain text for convenience in this repo. Do not commit `bot/secrets.txt`.
- Use environment variables or a secrets manager for production.

License
- No license file is included. Add a `LICENSE` if you plan to distribute or share the code.

