from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api/v1/quotes")

class QuoteRequest(BaseModel):
    quote_id: str
    product: str
    currency: str
    notional: float
    maturity: str
    strike: float

class QuoteValidationResponse(BaseModel):
    valid: bool
    errors: List[str]
    quote_id: str

@router.post("/validate", response_model=QuoteValidationResponse)
async def validate_quote(quote: QuoteRequest):
    print(quote.quote_id)
    return {
        "valid": True,
        "errors": [],
        "quote_id": "",
    }
