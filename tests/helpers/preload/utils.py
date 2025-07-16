from typing import Any

import sqlalchemy

from app.core import database


async def get_one_or_none(test_database: database.Database, model, **filters) -> Any:
    async for session in test_database.get_session():
        stmt = sqlalchemy.select(model).filter_by(**filters)
        result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def insert_into(test_database: database.Database, record: Any):
    async for session in test_database.get_session():
        session.add(record)
        await session.commit()
    return record.id
