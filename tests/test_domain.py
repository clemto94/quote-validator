from pydantic import ValidationError
import pytest
from typing import TypedDict

from domain.models import Quote, Currency, QuoteRequest


def test_valid_quote():
    valid_quote = QuoteRequest(
        quote_id="Q001",
        product="SWAP",
        currency="USD",
        notional=5000000,
        maturity="5Y",
        strike=102.5
    )
    quote = Quote(**valid_quote.model_dump())
    assert quote.model_dump() == valid_quote.model_dump()
    assert quote.quote_id == valid_quote.quote_id
    assert quote.currency == valid_quote.currency
    assert quote.maturity == valid_quote.maturity
    assert quote.strike == valid_quote.strike

def test_invalid_notional():
    invalid_quote = QuoteRequest(
        quote_id="Q002",
        product="SWAP",
        currency="INVALID",
        notional=-1000000,
        maturity="50Y",
        strike=-10
    )
    with pytest.raises(ValidationError):
        Quote(**invalid_quote.model_dump())
