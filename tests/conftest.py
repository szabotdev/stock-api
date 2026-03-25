import pytest

from app import create_app


@pytest.fixture()
def app(tmp_path):
    app = create_app()
    app.config.update(
        TESTING=True,
        TICKERS_FILE=str(tmp_path / "tickers.json"),
        DEFAULT_TICKERS=["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X"],
    )
    return app


@pytest.fixture()
def client(app):
    return app.test_client()
