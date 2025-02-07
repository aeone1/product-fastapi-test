"""Query delete service"""

from uuid import UUID
from sqlalchemy.orm import Session

from database.tables import Product as ProductModel
from .exceptions import ProductNotFound

class ProductDeleteService():
    """Deletes a Query-Group relationship"""
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
        self._product_model = ProductModel

    def delete_product_by_id(self, product_id: UUID) -> bool:
        product_from_db = self._db_session.query(self._product_model)\
            .filter(self._product_model.id == product_id).first()

        if not product_from_db:
            raise ProductNotFound(f"Product with id {product_id} not found.")

        try:
            self._db_session.delete(product_from_db)
            self._db_session.commit()
            return True
        except Exception as delete_exception:
            raise delete_exception
