import pytest
from fastapi import status

@pytest.mark.integration
def test_create_quote(client, valid_quote_data):
    """
    Test d'intégration pour la création d'un devis via l'API
    """
    response = client.post("/api/v1/quotes/validate", json=valid_quote_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("valid") == True


@pytest.mark.integration
def test_invalid_quote_creation(client):
    """
    Test d'intégration pour la validation des données de devis invalides
    """
    invalid_quote = {
        "quote_id": "Q002",
        "product": "SWAP",
        "currency": "INVALID",
        "notional": -1000000,
        "maturity": "50Y",
        "strike": -10
    }
    response = client.post("/api/v1/quotes/validate", json=invalid_quote)
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("valid") == False