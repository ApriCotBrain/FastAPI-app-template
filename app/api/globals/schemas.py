import pydantic

from app.api.globals import consts


class ErrorMessage(pydantic.BaseModel):
    field: str | None = None
    message: str
    type: consts.ErrorType


class ErrorsContent(pydantic.BaseModel):
    errors: list[ErrorMessage]


class Paginator(pydantic.BaseModel):
    limit: int
    offset: int
    total: int
