from flask import Blueprint, jsonify, request
from ..storage import load_tickers, save_tickers

tickers_bp = Blueprint("tickers", __name__)

@tickers_bp.route("/tickers", methods=["GET"])
def get_tickers():
    return jsonify(load_tickers())

@tickers_bp.route("/tickers", methods=["POST"])
def add_ticker():
    data = request.get_json()
    symbol = data.get("symbol", "").strip().upper()

    if not symbol:
        return jsonify({"error": "No symbol provided"}), 400

    tickers = load_tickers()
    if symbol in tickers:
        return jsonify({"error": "{} already exists".format(symbol)}), 400

    tickers.append(symbol)
    save_tickers(tickers)
    return jsonify({"ok": True, "tickers": tickers})

@tickers_bp.route("/tickers/<symbol>", methods=["DELETE"])
def remove_ticker(symbol):
    tickers = load_tickers()
    symbol = symbol.upper()

    if symbol not in tickers:
        return jsonify({"error": "Not found"}), 404

    tickers.remove(symbol)
    save_tickers(tickers)
    return jsonify({"ok": True, "tickers": tickers})