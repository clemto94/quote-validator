from pydantic import ValidationError
from typing import Optional

from infrastructure.messaging import quote_queue
from .models import Quote, QuoteValidationResponse

class ValidationService:
    def __init__(self)->None:
        self.quote: Optional[Quote] = None

    def validate_quote(self, data: dict) -> QuoteValidationResponse:
        print("Validating quote...")
        try:
            self.quote = Quote(**data)
            self.publish_quote(self.quote)
            return QuoteValidationResponse(
                valid=True,
                errors=[],
                quote_id=self.quote.quote_id
            )
        except ValidationError as e:
            return QuoteValidationResponse(
                valid=False,
                errors=[err['msg'] for err in e.errors()],
                quote_id=data.get("quote_id", "")
            )

    @staticmethod
    def publish_quote(data: Quote)->None:
        quote_queue.put(data)
        return