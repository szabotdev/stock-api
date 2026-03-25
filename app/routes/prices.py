from flask import Blueprint, jsonify
from ..storage import load_tickers
from ..config import display_ticker
import yfinance as yf

prices_bp = Blueprint("prices", __name__)

def _get_quote(symbol):
    """Fetch current price and daily change for one symbol."""
    try:
        hist = yf.Ticker(symbol).history(period="2d")
        if len(hist) >= 2:
            prev = hist["Close"].iloc[-2]
            curr = hist["Close"].iloc[-1]
            change = ((curr - prev) / prev) * 100
        elif len(hist) == 1:
            curr, change = hist["Close"].iloc[-1], 0.0
        else:
            return {"price": 0, "change": 0}
        return {
            "price":  round(float(curr), 2),
            "change": round(float(change), 2)
        }
    except:
        return {"price": 0, "change": 0}

@prices_bp.route("/prices")
def prices():
    return jsonify({
        display_ticker(symbol): _get_quote(symbol)
        for symbol in load_tickers()
    })

@prices_bp.route("/sparkline/<symbol>")
def sparkline(symbol):
    try:
        hist   = yf.Ticker(symbol).history(period="1mo", interval="1d")
        closes = [round(float(v), 2) for v in hist["Close"].tolist()]
        return jsonify({"symbol": symbol, "closes": closes})
    except Exception as e:
        return jsonify({"symbol": symbol, "closes": [], "error": str(e)})
