from flask import Blueprint, render_template
from ..storage import load_tickers
from ..config import display_ticker

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def index():
    tickers = [
        {"symbol": symbol, "label": display_ticker(symbol)}
        for symbol in load_tickers()
    ]
    return render_template("index.html", tickers=tickers)
