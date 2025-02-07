"""
User table
"""
from sqlalchemy import CheckConstraint, Column, String, Float, Boolean, Text

from ._base import CustomBase
from ..databease_types import IDMixin
from sqlalchemy.orm import relationship, validates


class Product(IDMixin, CustomBase):
    """Product table"""
    __tablename__ = "products"

    name = Column(String(500), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, nullable=False)

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_positive'),
    )

    @validates('price')
    def validate_price(self, key, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price
