import uuid

import fastapi
import pydantic

from app.api import globals as api_globals
from app.api.v1.template.base import exceptions, schemas, service


class TemplateBaseRouter:
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
            responses=api_globals.exceptions.generate_exc_responses(
                exceptions.TemplateAlreadyExistsError,
            ),
            status_code=fastapi.status.HTTP_201_CREATED,
        )
        async def create_template(data: schemas.TemplateData) -> schemas.CreatedTemplateResponse:
            return await self._template_service.create_template(data=data)

        @router.get(
            path="/{template_id}",
            description="Get template by id",
            response_model=schemas.GetTemplateByIdResponse,
            responses=api_globals.exceptions.generate_exc_responses(
                exceptions.TemplateNotFoundError,
            ),
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
        async def get_templates_list(
            limit: pydantic.PositiveInt = fastapi.Query(default=20, le=100),
            offset: pydantic.PositiveInt = fastapi.Query(default=0),
        ) -> schemas.GetTemplatesListResponse:
            tags, paginator = await self._template_service.get_templates_list(limit=limit, offset=offset)
            return schemas.GetTemplatesListResponse(response=tags, paginator=paginator)
