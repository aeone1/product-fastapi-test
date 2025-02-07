"""Product get service"""

from uuid import UUID

from sqlalchemy.orm import Session

from database.tables import Product as ProductModel
from .schema import Product as ProductSchema
from .exceptions import ProductNotFound


class ProductGetService():
    """Get product from storage"""

    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
        self._model = ProductModel

    def get_product_by_id(self, product_id: UUID) -> ProductSchema | None:
        product_from_db = self._db_session.query(self._model)\
            .filter(self._model.id == product_id).first()

        if not product_from_db:
            raise ProductNotFound(f"Product with id {product_id} not found")
        
        return ProductSchema(**product_from_db.__dict__)
