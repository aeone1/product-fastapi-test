from typing import Optional

import sqlalchemy as sa
from sqlalchemy import orm as sa_orm

from . import schema


def sort_query(
        field: sa.Column,
        query: sa_orm.Query,
        sorter: Optional[schema.SortEnum] = None
    ) -> sa_orm.Query:
    if sorter:
        if sorter == schema.SortEnum.asc:
            query = query.order_by(field)
        else:
            query = query.order_by(field.desc())
    return query


def limit_offset(limit: int, offset: int, query: sa_orm.Query) -> sa_orm.Query:
    return query.limit(limit=limit).offset(offset=offset)
