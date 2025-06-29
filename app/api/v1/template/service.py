import uuid

from app.api.v1.template import repository, schemas


class TemplateService:
    def __init__(self, template_repository: repository.TemplateRepository):
        self._repository = template_repository

    async def create_template(self, data: schemas.TemplateData) -> schemas.CreatedTemplateResponse:
        created_template = await self._repository.create_template(data=data)
        return schemas.CreatedTemplateResponse(response=created_template)

    async def get_template_by_id(self, template_id: uuid.UUID) -> schemas.GetTemplateByIdResponse:
        response = await self._repository.get_template_by_id(template_id=template_id)
        return schemas.GetTemplateByIdResponse(response=response)

    async def get_templates_list(self) -> schemas.GetTemplatesListResponse:
        response = await self._repository.get_templates_list()
        return schemas.GetTemplatesListResponse(response=response)
