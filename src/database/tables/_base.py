from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, DateTime, func


class CustomBase(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


CustomBase = declarative_base(cls=CustomBase)
