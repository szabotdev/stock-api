def test_get_tickers_uses_default_list_when_file_missing(client):
    response = client.get("/tickers")

    assert response.status_code == 200
    assert response.get_json() == ["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X"]


def test_add_and_remove_ticker_persists_to_disk(client, app, tmp_path):
    response = client.post("/tickers", json={"symbol": "abc"})

    assert response.status_code == 200
    assert response.get_json()["tickers"] == ["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X", "ABC"]

    tickers_file = tmp_path / "tickers.json"
    assert tickers_file.exists()
    assert tickers_file.read_text() == '["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X", "ABC"]'

    response = client.delete("/tickers/abc")

    assert response.status_code == 200
    assert response.get_json()["tickers"] == ["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X"]
    assert tickers_file.read_text() == '["WEBN.DE", "VWCE.DE", "SPY", "EURHUF=X", "USDHUF=X"]'


def test_add_duplicate_ticker_is_rejected(client):
    response = client.post("/tickers", json={"symbol": "SPY"})

    assert response.status_code == 400
    assert response.get_json()["error"] == "SPY already exists"
