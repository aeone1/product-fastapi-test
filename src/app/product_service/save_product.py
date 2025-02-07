"""
Product save service
"""
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from loguru import logger

from .exceptions import ProductNameAlreadyExists
from database.tables import Product as ProductModel

from .schema import Product as ProductSchema


class ProductSaveService():
    """Saves Products """

    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session
        self._model = ProductModel

    def save(self, product: ProductSchema) -> ProductSchema:
        logger.info(f'Saving product: {product}')
        entity = self._model(**product.model_dump())
        self._db_session.add(entity)
        try:
            self._db_session.commit()
        except IntegrityError as save_uniq:
            raise ProductNameAlreadyExists(
                f"product name {product.name} already exist")
        except Exception as save_to_db_exception:
            print('-----------------here------------------------')
            self._db_session.rollback()
            raise save_to_db_exception

        return ProductSchema(**entity.__dict__)
