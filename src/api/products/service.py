
from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.product_service import ProductSaveService
from app.product_service import ProductUpdateService
from app.product_service import ProductDeleteService
from app.product_service import ProductGetService
from app.product_service import ProductsGetService
from app.product_service.exceptions import ProductNameAlreadyExists
from app.product_service.schema import Product

from .models import ErrorResponse, ProductCreate, ProductPagination, ProductUpdate, ProductsGetFilter



def create(db_session: Session, product_in: ProductCreate) -> Product:
    """Creates a product"""
    try:
        product_save_service = ProductSaveService(db_session)
        product_data = product_in.model_dump(exclude_unset=True, exclude={"id"})
        product = product_save_service.save(Product(**product_data))
        product = Product(**product.__dict__)

        return product
    except ProductNameAlreadyExists as ex:
        error_response = ErrorResponse(
            code=400,
            message=f"Product name '{product_in.name}' already exists."
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_response.model_dump()
        )


def update(db_session: Session, product_to_update: ProductUpdate) -> Product:
    """Updates a product"""
    product_save_service = ProductUpdateService(db_session)
    product_data = product_to_update.model_dump(exclude_unset=True)
    print(f"{product_data=}")
    product = product_save_service.update(**product_data)

    return product


def delete_product_by_id(db_session: Session, product_id: UUID) -> None:
    """Deletes a product"""
    product_delete_service = ProductDeleteService(db_session)
    product_delete_service.delete_product_by_id(product_id)


def get_by_id(db_session: Session, product_id: UUID) -> Product:
    """Gets a product"""
    product_get_service = ProductGetService(db_session)
    product = product_get_service.get_product_by_id(product_id)

    return product


def get_all(db_session: Session, product_get_filter: ProductsGetFilter) -> ProductPagination:
    """Gets all products"""
    products_get_service = ProductsGetService(db_session)
    products, pagination = products_get_service.get_products(
        page_number=product_get_filter.page_number,
        page_size=product_get_filter.page_size,
        sort_by_created_at=product_get_filter.sort_by_created_at,
        sort_by_name=product_get_filter.sort_by_name,
        sort_by_description=product_get_filter.sort_by_description
    )

    # 'page_number', 'page_size', 'num_pages', 'total_results'

    result = ProductPagination(
        items=products,
        itemsPerPage=pagination.page_size,
        page=pagination.page_number,
        total=pagination.total_results
    )

    return result
