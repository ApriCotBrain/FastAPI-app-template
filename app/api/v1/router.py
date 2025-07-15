import fastapi

from app.api.v1 import template


class V1Router:
    def __init__(
        self,
        template_base_router: template.base.router.TemplateBaseRouter,
    ):
        self._template_base_router = template_base_router

    @property
    def router(self) -> fastapi.APIRouter:  # noqa: F821
        router = fastapi.APIRouter(prefix="/v1")
        self._update_router(router)
        return router

    def _update_router(self, router: fastapi.APIRouter) -> None:
        router.include_router(self._template_base_router.router)
