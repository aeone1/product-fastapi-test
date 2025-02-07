
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Request

from .models import ProductCreate, ProductPagination, ProductUpdate, ProductsGetFilter
from .service import get_all, get_by_id, create, delete_product_by_id, update
from uuid import UUID

from app.product_service.schema import Product


router = APIRouter()


def get_db(request: Request) -> Session:
    """Extracts the database session from request state."""
    return request.state.db

@router.get("", response_model=ProductPagination)
def get_products(product_get_filter: ProductsGetFilter = Depends(), db_session: Session = Depends(get_db)):
    """Get all products."""
    return get_all(db_session, product_get_filter)


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: UUID, db_session: Session = Depends(get_db)):
    """Get a single project by id."""
    return get_by_id(db_session, product_id)

@router.post("", response_model=Product)
def create_product(product_in: ProductCreate, db_session: Session = Depends(get_db)):
    """Create a new product."""
    return create(db_session, product_in)

@router.delete("/{product_id}", response_model=None)
def delete_product(product_id: UUID, db_session: Session = Depends(get_db)):
    """Delete a product by id."""
    return delete_product_by_id(db_session, product_id)

@router.put("/{product_id}", response_model=Product)
def update_product(product_to_update: ProductUpdate, db_session: Session = Depends(get_db)):
    """Update a product by id."""
    return update(db_session, product_to_update)
