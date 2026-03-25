from app.routes import prices as prices_module


class FakeSeries:
    def __init__(self, values):
        self._values = values
        self.iloc = self

    def __getitem__(self, index):
        return self._values[index]

    def tolist(self):
        return list(self._values)


class FakeHistory:
    def __init__(self, closes):
        self._closes = FakeSeries(closes)

    def __len__(self):
        return len(self._closes.tolist())

    def __getitem__(self, key):
        if key != "Close":
            raise KeyError(key)
        return self._closes


class FakeTicker:
    def __init__(self, closes_by_symbol, symbol):
        self._closes_by_symbol = closes_by_symbol
        self.symbol = symbol

    def history(self, period=None, interval=None):
        return FakeHistory(self._closes_by_symbol[self.symbol])


def test_prices_route_returns_quotes_for_all_tickers(client, app, monkeypatch):
    app.config["DEFAULT_TICKERS"] = ["EURHUF=X", "USDHUF=X"]

    def fake_ticker(symbol):
        return FakeTicker({"EURHUF=X": [380.0, 382.5], "USDHUF=X": [350.0, 355.0]}, symbol)

    monkeypatch.setattr(prices_module.yf, "Ticker", fake_ticker)

    response = client.get("/prices")

    assert response.status_code == 200
    assert response.get_json() == {
        "EUR/HUF": {"price": 382.5, "change": 0.66},
        "USD/HUF": {"price": 355.0, "change": 1.43},
    }


def test_sparkline_route_returns_closes(client, monkeypatch):
    def fake_ticker(symbol):
        return FakeTicker({"AAA": [1.0, 2.0, 3.0]}, symbol)

    monkeypatch.setattr(prices_module.yf, "Ticker", fake_ticker)

    response = client.get("/sparkline/AAA")

    assert response.status_code == 200
    assert response.get_json() == {"symbol": "AAA", "closes": [1.0, 2.0, 3.0]}
