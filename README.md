 # Binance Futures Testnet Trading Bot

Lightweight CLI trading bot for Binance Futures (testnet). Intended for testing and learning only — do not use with real funds without careful review.

**What this project contains**
- `cli.py`: command-line entrypoint to place MARKET and LIMIT orders.
- `requirements.txt`: Python dependencies used by the project.
 - `binanceApp/`: not committed — virtual environment is not included. Create a local virtual environment instead (see Local setup).
- `bot/` package:
	- `__init__.py`
	- `clients.py` — creates the Binance client configured for testnet
	- `orders.py` — builds and sends order requests
	- `validators.py` — input validation helpers
	- `logging_config.py` — reads `bot/secrets.txt` and exposes API keys
	- `secrets.txt` (not committed) — expected location for API keys
- `logs/`: directory for runtime logs

**Prerequisites**
- Python 3.8 or newer

**Local setup (recommended)**
1. Create and activate a local virtual environment (recommended):

```bash
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate.bat
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Add your testnet API credentials to `bot/secrets.txt` (two lines — key then secret):

```
YOUR_TESTNET_API_KEY
YOUR_TESTNET_API_SECRET
```

Notes:
- The project is configured to use Binance testnet. Ensure you use testnet keys/endpoints.
- If you prefer not to store secrets on disk, modify `bot/logging_config.py` to read from environment variables.
 - Example files: `bot/secrets.txt.example` and `.env.example` are included to show required keys without exposing secrets.
	 - Use `bot/secrets.txt` (two lines) or a `.env` file with `BINANCE_API_KEY` and `BINANCE_API_SECRET`.

**Using environment variables**
- Copy `.env.example` to `.env` and fill in your keys, or export the variables in your shell:

```bash
# from `.env` (requires a tool like `python-dotenv` or your shell to load the file)
export BINANCE_API_KEY=YOUR_TESTNET_API_KEY
export BINANCE_API_SECRET=YOUR_TESTNET_API_SECRET
```

Or on Windows PowerShell:

```powershell
$env:BINANCE_API_KEY = 'YOUR_TESTNET_API_KEY'
$env:BINANCE_API_SECRET = 'YOUR_TESTNET_API_SECRET'
```

**Running the CLI**
Run commands from the repository root. Examples:

```powershell
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# LIMIT order example:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

Command notes:
- `--symbol`: trading pair (e.g., `BTCUSDT`)
- `--side`: `BUY` or `SELL`
- `--type`: `MARKET` or `LIMIT`
- `--quantity`: order quantity
- `--price`: required for `LIMIT` orders

**Key files (quick links)**
- [cli.py](cli.py)
- [requirements.txt](requirements.txt)
- [bot/clients.py](bot/clients.py)
- [bot/orders.py](bot/orders.py)
- [bot/validators.py](bot/validators.py)
- [bot/logging_config.py](bot/logging_config.py)

**Troubleshooting**
- If keys fail to load, ensure `bot/secrets.txt` has exactly two non-empty lines with no extra whitespace.
- Run the CLI from the project root so imports resolve (`python cli.py ...`).

**Security**
- `bot/secrets.txt` is plain text for convenience in this repo — do not commit it.
- For production use, load secrets from environment variables or a secrets manager.

**License**
- No license file is included. Add a `LICENSE` if you plan to distribute this project.
