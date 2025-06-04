from pydantic import ValidationError

from .models import Quote

class ValidationService:
    @staticmethod
    def validate_quote(data: dict) -> dict:
        try:
            quote = Quote(**data)
            return {
                "valid": True,
                "errors": [],
                "quote_id": quote.quote_id
            }
        except ValidationError as e:
            return {
                "valid": False,
                "errors": [err['msg'] for err in e.errors()],
                "quote_id": data.get("quote_id", "")
            }
