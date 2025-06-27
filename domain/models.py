from typing import List

from pydantic import BaseModel, field_validator
from enum import Enum
import re
from sqlalchemy import Column, String, Float, Enum as SAEnum
from infrastructure.db import Base
from sqlalchemy.orm import mapped_column, Mapped

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

class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"

class Quote(BaseModel):
    quote_id: str
    product: str
    currency: Currency
    notional: float
    maturity: str
    strike: float

    @field_validator("notional")
    @classmethod
    def notional_must_be_valid(cls, value):
        if not (0 < value < 100_000_000):
            raise ValueError("Notional must be > 0 and < 100M")
        return value

    @field_validator("strike")
    @classmethod
    def strike_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("Strike must be positive")
        return value

    @field_validator("maturity")
    @classmethod
    def maturity_must_be_valid(cls, value):
        match = re.match(r"^(\d+)([DY])$", value)
        if not match:
            raise ValueError("Maturity must be in format like '30D' or '5Y'")
        num = int(match.group(1))
        unit = match.group(2)
        if unit == "D" and not (1 <= num <= 365 * 30):
            raise ValueError("Maturity in days must be between 1 and 10950")
        elif unit == "Y" and not (1 <= num <= 30):
            raise ValueError("Maturity in years must be between 1 and 30")
        return value

class QuoteORM(Base):
    __tablename__ = "quote"
    quote_id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    product: Mapped[str] = mapped_column(String, nullable=False)
    currency: Mapped[Currency] = mapped_column(SAEnum(Currency), nullable=False)
    notional: Mapped[float] = mapped_column(Float, nullable=False)
    maturity: Mapped[str] = mapped_column(String, nullable=False)
    strike: Mapped[float] = mapped_column(Float, nullable=False)
