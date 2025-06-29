from sqlalchemy import String, Float, Enum as SAEnum
from sqlalchemy.orm import mapped_column, Mapped
from infrastructure.db import Base
from domain.schemas import Currency

class QuoteModel(Base):
    __tablename__ = "quote"
    quote_id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    product: Mapped[str] = mapped_column(String, nullable=False)
    currency: Mapped[Currency] = mapped_column(SAEnum(Currency), nullable=False)
    notional: Mapped[float] = mapped_column(Float, nullable=False)
    maturity: Mapped[str] = mapped_column(String, nullable=False)
    strike: Mapped[float] = mapped_column(Float, nullable=False) 