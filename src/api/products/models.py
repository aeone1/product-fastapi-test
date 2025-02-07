
from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

from app.product_service.schema import Product, SortEnum


class ProductPagination(BaseModel):
    items: List[Product] = []
    itemsPerPage: int
    page: int
    total: int


class ProductCreate(Product):
    id: Optional[UUID]
    name: str
    description: Optional[str]
    price: float


class ProductUpdate(Product):
    id: UUID
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    in_stock: Optional[bool]


class ProductsGetFilter(BaseModel):
    page_number: Optional[int] = 1
    page_size: Optional[int] = 10
    sort_by_created_at: Optional[SortEnum]
    sort_by_name: Optional[SortEnum]
    sort_by_description: Optional[SortEnum]
