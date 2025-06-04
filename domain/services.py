from pydantic import ValidationError

from .models import Quote

class ValidationService:
    def __init__(self):
        self.quote = None

    def validate_quote(self, data: dict) -> dict:
        try:
            self.quote = Quote(**data)
            return {
                "valid": True,
                "errors": [],
                "quote_id": self.quote.quote_id
            }
        except ValidationError as e:
            return {
                "valid": False,
                "errors": [err['msg'] for err in e.errors()],
                "quote_id": data.get("quote_id", "")
            }
