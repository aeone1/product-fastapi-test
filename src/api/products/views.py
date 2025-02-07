
from sqlalchemy.orm import Session
from fastapi import APIRouter

from .models import ProductCreate, ProductPagination, ProductUpdate, ProductsGetFilter
from .service import get_all, get_by_id, create, delete_product_by_id, update
from uuid import UUID

from app.product_service.schema import Product


router = APIRouter()


@router.get("", response_model=ProductPagination)
def get_products(db_session: Session, product_get_filter: ProductsGetFilter):
    """Get all products."""
    return get_all(db_session, product_get_filter)


@router.get("/{product_id}", response_model=Product)
def get_product(db_session: Session, product_id: UUID):
    """Get a single project by id."""
    return get_by_id(db_session, product_id)

@router.post("", response_model=Product)
def create_product(db_session: Session, product_in: ProductCreate):
    """Create a new product."""
    return create(db_session, product_in)

@router.delete("/{product_id}", response_model=None)
def delete_product(db_session: Session, product_id: UUID):
    """Delete a product by id."""
    return delete_product_by_id(db_session, product_id)

@router.put("/{product_id}", response_model=Product)
def update_product(db_session: Session, product_to_update: ProductUpdate):
    """Update a product by id."""
    return update(db_session, product_to_update)
