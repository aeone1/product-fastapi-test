"""
Product save service
"""
from sqlalchemy.orm import Session
from loguru import logger

from database.tables import Product as ProductModel

from .schema import Product as ProductSchema


class ProductSaveService():
    """Saves Products """

    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
        self._model = ProductModel

    def save(self, product: ProductSchema) -> ProductModel:
        logger.info(f'Saving product: {product}')
        entity = self._model(**product.model_dump())
        self._db_session.add(entity)
        try:
            self._db_session.commit()
        except Exception as save_to_db_exception:
            self._db_session.rollback()
            raise save_to_db_exception
        
        return entity
