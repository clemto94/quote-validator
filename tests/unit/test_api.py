from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)

@pytest.mark.unit
def test_valid_quote():
    valid_quote = {
        "quote_id": "Q001",
        "product": "SWAP",
        "currency": "USD",
        "notional": 5000000,
        "maturity": "5Y",
        "strike": 102.5
    }
    response = client.post("/api/v1/quotes/validate", json=valid_quote)
    assert response.status_code == 200
    body = response.json()
    assert body["valid"] is True
    assert body["errors"] == []
    assert body["quote_id"] == "Q001"

@pytest.mark.unit
def test_invalid_quote():
    invalid_quote = {
        "quote_id": "Q002",
        "product": "SWAP",
        "currency": "INVALID",
        "notional": -1000000,
        "maturity": "50Y",
        "strike": -10
    }
    response = client.post("/api/v1/quotes/validate", json=invalid_quote)
    assert response.status_code == 200
    body = response.json()
    assert body["valid"] is False
    assert (
            "Input should be 'USD', 'EUR', 'GBP' or 'JPY'" in body["errors"] and
            "Value error, Notional must be > 0 and < 100M" in body["errors"] and
            "Value error, Maturity in years must be between 1 and 30" in body["errors"] and
            "Value error, Strike must be positive" in body["errors"]
    )
    assert body["quote_id"] == "Q002"
