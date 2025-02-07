"""
Product Schema
"""


from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    """Product App Schema"""
    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool
    created_at: Optional[datetime] = Field(default_factory=datetime.now)

    def __hash__(self):
        return hash((self.id, self.name))
