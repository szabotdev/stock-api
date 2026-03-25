from flask import Blueprint, render_template
from ..routes.tickers import serialize_ticker
from ..storage import load_tickers

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def index():
    tickers = [
        serialize_ticker(symbol)
        for symbol in load_tickers()
    ]
    return render_template("index.html", tickers=tickers)
