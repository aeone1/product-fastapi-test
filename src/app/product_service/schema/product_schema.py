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
    description: Optional[str]
    price: float
    in_stock: bool
    created_at: Optional[datetime]
    
    # def __hash__(self):
    #     return hash((self.id, self.name))
