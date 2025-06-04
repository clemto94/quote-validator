from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

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
    assert "value is not a valid enumeration member" in body["errors"][0] or "Notional must be" in body["errors"][0]
    assert body["quote_id"] == "Q002"
