from flask import Flask
from .config import Config
from .routes.ui import ui_bp
from .routes.tickers import tickers_bp
from .routes.prices import prices_bp

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    app.register_blueprint(ui_bp)
    app.register_blueprint(tickers_bp)
    app.register_blueprint(prices_bp)

    return app