import uuid

import pydantic


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
