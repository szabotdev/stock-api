import os

class Config:
    TICKERS_FILE   = os.environ.get("TICKERS_FILE", "/data/tickers.json")
    DEFAULT_TICKERS = ["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X"]

DISPLAY_NAMES = {
    "EURHUF=X": "EUR/HUF",
    "USDHUF=X": "USD/HUF",
}

def display_ticker(symbol):
    return DISPLAY_NAMES.get(symbol, symbol)
