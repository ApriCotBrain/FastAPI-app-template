import fastapi

import app.api.globals.schemas
from app.api.globals import consts, exceptions


class TemplateAlreadyExistsError(exceptions.ApiError):
    status_code = fastapi.status.HTTP_409_CONFLICT
    content = app.api.globals.schemas.ErrorsContent(
        errors=[
            app.api.globals.schemas.ErrorMessage(
                field="name",
                message="Template already exists",
                type=consts.ErrorType.TEMPLATE_ALREADY_EXISTS,
            )
        ]
    )


class TemplateNotFoundError(exceptions.ApiError):
    status_code = fastapi.status.HTTP_404_NOT_FOUND
    content = app.api.globals.schemas.ErrorsContent(
        errors=[
            app.api.globals.schemas.ErrorMessage(
                field="template_id",
                message="Template not found",
                type=consts.ErrorType.TEMPLATE_NOT_FOUND,
            )
        ]
    )
