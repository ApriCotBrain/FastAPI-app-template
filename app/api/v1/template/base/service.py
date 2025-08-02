import asyncio
import uuid

from app.api.globals import schemas as global_schemas
from app.api.v1.template.base import exceptions, repository, schemas


class TemplateService:
    def __init__(self, template_repository: repository.TemplateRepository):
        self._repository = template_repository

    async def create_template(self, data: schemas.TemplateData) -> schemas.CreatedTemplateResponse:
        existed_template = await self._repository.select_exists_template_by_name(name=data.name)
        if existed_template:
            raise exceptions.TemplateAlreadyExistsError
        created_template = await self._repository.insert_template(data=data)
        return schemas.CreatedTemplateResponse(response=created_template)

    async def get_template_by_id(self, template_id: uuid.UUID) -> schemas.GetTemplateByIdResponse:
        is_template_exists = await self._repository.select_exists_template_by_id(template_id=template_id)
        if not is_template_exists:
            raise exceptions.TemplateNotFoundError
        template = await self._repository.select_template_by_id(template_id=template_id)
        return schemas.GetTemplateByIdResponse(response=template)

    async def get_templates_list(self, limit: int, offset: int) -> schemas.GetTemplatesListResponse:
        templates, total = await asyncio.gather(
            self._repository.select_templates_list(limit=limit, offset=offset),
            self._repository.select_total_templates(),
        )
        return (
            [schemas.Template(**template) for template in templates],
            global_schemas.Paginator(limit=limit, offset=offset, total=total),
        )
