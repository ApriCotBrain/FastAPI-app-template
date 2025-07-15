import uuid

import pydantic

from app.api.globals import schemas as global_schemas


# CREATE
class TemplateData(pydantic.BaseModel):
    name: str


class CreatedTemplate(TemplateData):
    id: uuid.UUID


class CreatedTemplateResponse(pydantic.BaseModel):
    response: CreatedTemplate


# GET BY ID
class Template(pydantic.BaseModel):
    id: uuid.UUID
    name: str


class GetTemplateByIdResponse(pydantic.BaseModel):
    response: Template


# GET LIST
class GetTemplatesListResponse(pydantic.BaseModel):
    response: list[Template]
    paginator: global_schemas.Paginator
