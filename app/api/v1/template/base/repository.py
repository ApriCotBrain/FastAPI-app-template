import typing
import uuid

import sqlalchemy

from app.api.v1.template.base import schemas
from app.core import database
from app.core.database import models


class TemplateRepository:
    def __init__(self, db: database.Database):
        self._db = db

    async def select_exists_template_by_name(self, name: str) -> bool | None:
        query = sqlalchemy.select(sqlalchemy.exists().where(models.Template.name == name))
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.scalar()

    async def select_exists_template_by_id(self, template_id: uuid.UUID) -> bool | None:
        query = sqlalchemy.select(sqlalchemy.exists().where(models.Template.id == template_id))
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.scalar()

    async def insert_template(self, data: schemas.TemplateData) -> sqlalchemy.RowMapping:
        query = (
            sqlalchemy.insert(models.Template)
            .values(**data.model_dump())
            .returning(models.Template.id, models.Template.name)
        )
        async for session in self._db.get_session():
            result = await session.execute(query)
            await session.commit()
        return result.mappings().first()

    async def select_template_by_id(self, template_id: uuid.UUID) -> sqlalchemy.RowMapping:
        query = sqlalchemy.select(models.Template.id, models.Template.name).where(
            models.Template.id == template_id
        )
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.mappings().first()

    async def select_templates_list(self, limit: int, offset: int) -> typing.Sequence[sqlalchemy.RowMapping]:
        query = sqlalchemy.select(models.Template.id, models.Template.name).limit(limit).offset(offset)
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.mappings().all()

    async def select_total_templates(self) -> int:
        query = sqlalchemy.select(sqlalchemy.func.count(models.Template.id))
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.scalar_one()
