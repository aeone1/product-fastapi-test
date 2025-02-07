
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
    id: Optional[UUID] = None
    name: str
    description: Optional[str] = None
    price: float
    created_at: Optional[datetime] = None


class ProductUpdate(BaseModel):
    id: UUID
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None


class ProductsGetFilter(BaseModel):
    page_number: Optional[int] = 1
    page_size: Optional[int] = 10
    sort_by_created_at: Optional[SortEnum] = None
    sort_by_name: Optional[SortEnum] = None
    sort_by_description: Optional[SortEnum] = None

class ErrorResponse(BaseModel):
    code: int
    message: str
