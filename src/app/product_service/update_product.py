"""Group Update service"""
from typing import Optional

from uuid import UUID
from sqlalchemy.orm import Session

from database.tables import Product as ProductModel
from .schema import Product as ProductSchema
from .exceptions import ProductNotFound

class ProductUpdateService():
    """Updates a Product """
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
        self._model = ProductModel

    # ToDO: Create Schema for Update
    def update(
            self,
            product_id: UUID,
            product_name: Optional[str],
            product_description: Optional[str],
            product_price: Optional[float],
            product_in_stock: Optional[bool]
        ) -> ProductSchema:
        product_from_db = self._db_session.query(self._model)\
            .filter(self._model.id == product_id).first()

        if product_from_db:
            if product_name is not None:
                product_from_db.name = product_name
            if product_description is not None:
                product_from_db.description = product_description
            if product_price is not None:
                product_from_db.price = product_price
            if product_in_stock is not None:
                product_from_db.in_stock = product_in_stock

            try:
                self._db_session.add(product_from_db)
                self._db_session.commit()
                return ProductSchema(
                    id=product_from_db.id,
                    name=product_from_db.name,
                )
            except Exception as update_product_exception:
                self._db_session.rollback()
                raise update_product_exception
        raise ProductNotFound(f"Product {product_id} not found")
