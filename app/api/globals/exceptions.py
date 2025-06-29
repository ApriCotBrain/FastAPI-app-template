import typing

import fastapi

from app.api.globals import consts, schemas


class ApiError(Exception):
    status_code: int = fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR
    content: schemas.ErrorsContent | None = None
    headers: dict[str, str] | None = None
    media_type: str = "application/json"

    def __init__(self, status_code: int | None = None, content: schemas.ErrorsContent | None = None):
        if status_code is not None:
            self.status_code = status_code
        if content is not None:
            self.content = content


def handle_exception(
    request: fastapi.Request | Exception,  # noqa: ARG001
    exc: ApiError,
) -> fastapi.responses.ORJSONResponse:
    return fastapi.responses.ORJSONResponse(
        content=(
            exc.content.model_dump(exclude_none=True)
            if isinstance(exc.content, schemas.ErrorsContent)
            else None
        ),
        status_code=exc.status_code,
        headers=exc.headers,
        media_type=exc.media_type,
    )


def generate_exc_responses(*errors: ApiError) -> dict[int, dict[str, typing.Any]]:
    return dict(_parse_error(error) for error in errors)


def _parse_error(error: ApiError) -> tuple[int, dict[str, typing.Any]]:
    error_example = schemas.ErrorsContent(
        errors=[
            schemas.ErrorMessage(
                field="Error location", message="Error description", type=consts.ErrorType.DEFAULT
            )
        ]
    )
    return error.status_code, {
        "content": {error.media_type: {"example": error_example.model_dump()}},
    }
