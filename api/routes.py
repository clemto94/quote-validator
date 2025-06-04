from fastapi import APIRouter

from domain.models import QuoteRequest, QuoteValidationResponse
from domain.services import ValidationService

router = APIRouter(prefix="/api/v1/quotes")


@router.post("/validate", response_model=QuoteValidationResponse)
async def validate_quote(quote: QuoteRequest):
    return ValidationService().validate_quote(quote.model_dump())
