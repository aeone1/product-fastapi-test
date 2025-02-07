"""Products get service"""
from collections import namedtuple
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy_filters import apply_pagination

from database.tables import Product as ProductModel
from .schema import Product as ProductSchema
from . import helper, schema

# ToDO: Fix Duplicte
Pagination = namedtuple(
    'Pagination',
    ['page_number', 'page_size', 'num_pages', 'total_results']
)

class ProductsGetService():
    """Get products from storage"""

    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
        self._model = ProductModel

    def get_products(
            self,
            page_number: int,
            page_size: int,
            sort_by_created_at: Optional[schema.SortEnum],
            sort_by_name: Optional[schema.SortEnum],
            sort_by_description: Optional[schema.SortEnum]
        ) -> tuple[list[ProductSchema], Pagination]:
        products_query = self._db_session.query(self._model)

        products_query = helper.sort_query(
            field=self._model.created_at,
            query=products_query,
            sorter=sort_by_created_at
        )

        products_query = helper.sort_query(
            field=self._model.name,
            query=products_query,
            sorter=sort_by_name
        )

        products_query = helper.sort_query(
            field=self._model.description,
            query=products_query,
            sorter=sort_by_description
        )
        
        products_query, pagination = apply_pagination(products_query, page_number=page_number, page_size=page_size)

        products_from_db = products_query.all()

        
        return [ProductSchema(**product_from_db.__dict__) for product_from_db in products_from_db], pagination
