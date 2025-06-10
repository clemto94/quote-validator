import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """
    Fixture qui fournit un client de test FastAPI
    """
    return TestClient(app)

@pytest.fixture
def valid_quote_data():
    """
    Fixture qui fournit des données de devis valides pour les tests
    """
    return {
        "quote_id": "Q001",
        "product": "SWAP",
        "currency": "USD",
        "notional": 5000000,
        "maturity": "5Y",
        "strike": 102.5
    } 