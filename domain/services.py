from pydantic import ValidationError

from infrastructure.messaging import quote_queue
from .models import Quote

class ValidationService:
    def __init__(self):
        self.quote = None

    def validate_quote(self, data: dict) -> dict:
        print("Validating quote...")
        try:
            self.quote = Quote(**data)
            self.publish_quote(self.quote)
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

    @staticmethod
    def publish_quote(data: Quote):
        quote_queue.put(data)
        return