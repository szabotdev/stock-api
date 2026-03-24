from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

TICKERS = ["WEBN.DE", "VWCE.DE", "SPY"]

@app.route("/prices")
def prices():
    result = {}
    for symbol in TICKERS:
        try:
            t = yf.Ticker(symbol)
            hist = t.history(period="2d")
            if len(hist) >= 2:
                prev   = hist["Close"].iloc[-2]
                curr   = hist["Close"].iloc[-1]
                change = ((curr - prev) / prev) * 100
            elif len(hist) == 1:
                curr, change = hist["Close"].iloc[-1], 0.0
            else:
                curr, change = 0.0, 0.0
            result[symbol] = {
                "price":  round(float(curr), 2),
                "change": round(float(change), 2)
            }
        except Exception as e:
            result[symbol] = {"price": 0, "change": 0}
    return jsonify(result)

@app.route("/sparkline/<symbol>")
def sparkline(symbol):
    """Return last 30 daily closes for a ticker as a simple list."""
    try:
        # yfinance uses ^ prefix for indices, but we pass clean symbols
        t = yf.Ticker(symbol)
        # Use 1mo period, 1d interval for a clean 30-point sparkline
        hist = t.history(period="1mo", interval="1d")
        closes = [round(float(v), 2) for v in hist["Close"].tolist()]
        return jsonify({"symbol": symbol, "closes": closes})
    except Exception as e:
        return jsonify({"symbol": symbol, "closes": [], "error": str(e)})

if __name__ == "__main__":
    # 0.0.0.0 makes it reachable from the CYD on your local network
    app.run(host="0.0.0.0", port=5001)