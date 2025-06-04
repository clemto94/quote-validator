from pydantic import ValidationError
import pytest

from domain.models import Quote

def test_valid_quote():
    valid_quote = {
        "quote_id": "Q001",
        "product": "SWAP",
        "currency": "USD",
        "notional": 5000000,
        "maturity": "5Y",
        "strike": 102.5
    }
    quote = Quote(**valid_quote)
    assert quote.model_dump() == valid_quote
    assert quote.quote_id == valid_quote["quote_id"]
    assert quote.currency == valid_quote["currency"]
    assert quote.maturity == valid_quote["maturity"]
    assert quote.strike == valid_quote["strike"]

def test_invalid_notional():
    invalid_quote = {
        "quote_id": "Q002",
        "product": "SWAP",
        "currency": "INVALID",
        "notional": -1000000,
        "maturity": "50Y",
        "strike": -10
    }
    with pytest.raises(ValidationError):
        Quote(**invalid_quote)
