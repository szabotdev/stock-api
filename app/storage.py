import json
import os
from flask import current_app

def load_tickers():
    try:
        with open(current_app.config["TICKERS_FILE"], "r") as f:
            return json.load(f)
    except:
        return current_app.config["DEFAULT_TICKERS"].copy()

def save_tickers(tickers):
    path = current_app.config["TICKERS_FILE"]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(tickers, f)