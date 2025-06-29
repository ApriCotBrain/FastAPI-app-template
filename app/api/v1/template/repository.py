import typing
import uuid

import sqlalchemy

from app.api.v1.template import schemas
from app.core import database
from app.core.database import models


class TemplateRepository:
    def __init__(self, db: database.Database):
        self._db = db

    async def create_template(self, data: schemas.TemplateData) -> sqlalchemy.RowMapping:
        query = (
            sqlalchemy.insert(models.Template)
            .values(**data.model_dump())
            .returning(models.Template.id, models.Template.name)
        )
        async for session in self._db.get_session():
            result = await session.execute(query)
            await session.commit()
        return result.mappings().first()

    async def get_template_by_id(self, template_id: uuid.UUID) -> sqlalchemy.RowMapping:
        query = sqlalchemy.select(models.Template.id, models.Template.name).where(
            models.Template.id == template_id
        )
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.mappings().first()

    async def get_templates_list(self) -> typing.Sequence[sqlalchemy.RowMapping]:
        query = sqlalchemy.select(models.Template.id, models.Template.name)
        async for session in self._db.get_session():
            result = await session.execute(query)
        return result.mappings().all()
