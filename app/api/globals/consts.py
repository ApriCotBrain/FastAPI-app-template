import enum


class ErrorType(enum.StrEnum):
    DEFAULT = "error_type"
    TEMPLATE_ALREADY_EXISTS = "template_already_exists"
    TEMPLATE_NOT_FOUND = "template_not_found"
