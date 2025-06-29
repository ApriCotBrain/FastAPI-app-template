import uuid

import fastapi

from app.api.v1.template import schemas, service


class TemplateRouter:
    def __init__(self, template_service: service.TemplateService):
        self._template_service = template_service

    @property
    def router(self) -> fastapi.APIRouter:
        router = fastapi.APIRouter(
            prefix="/templates",
            tags=["Template API"],
            default_response_class=fastapi.responses.ORJSONResponse,
        )
        self._include_routes(router=router)
        return router

    def _include_routes(self, router: fastapi.APIRouter) -> None:
        @router.post(
            path="",
            description="Create template",
            response_model=schemas.CreatedTemplateResponse,
            status_code=fastapi.status.HTTP_201_CREATED,
        )
        async def create_template(data: schemas.TemplateData) -> schemas.CreatedTemplateResponse:
            return await self._template_service.create_template(data=data)

        @router.get(
            path="/{template_id}",
            description="Get template by id",
            response_model=schemas.GetTemplateByIdResponse,
            status_code=fastapi.status.HTTP_200_OK,
        )
        async def get_template_by_id(template_id: uuid.UUID) -> schemas.GetTemplateByIdResponse:
            return await self._template_service.get_template_by_id(template_id=template_id)

        @router.get(
            path="",
            description="Get templates list",
            response_model=schemas.GetTemplatesListResponse,
            status_code=fastapi.status.HTTP_200_OK,
        )
        async def get_templates_list() -> schemas.GetTemplatesListResponse:
            return await self._template_service.get_templates_list()
