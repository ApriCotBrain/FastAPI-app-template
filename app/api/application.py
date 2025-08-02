from contextlib import asynccontextmanager

import fastapi

from app.api import health_checks, v1
from app.api.globals import exceptions
from app.core import database


class Application:
    def __init__(
        self,
        v1_router: v1.router.V1Router,
        health_checks_router: health_checks.router.HealthChecksRouter,
        db: database.Database,
    ):
        self._db = db
        self._health_checks_router = health_checks_router
        self._v1_router = v1_router
        self._app = None

    @property
    def app(self) -> fastapi.FastAPI:
        if self._app is not None:
            return self._app

        @asynccontextmanager
        async def lifespan(app: fastapi.FastAPI):  # noqa: ARG001
            yield
            await self._db.shutdown()

        server = fastapi.FastAPI(
            title="Template Api",
            version="1.0.0",
            lifespan=lifespan,
            root_path="/app",
            openapi_url="/openapi.json",
        )
        self._set_up(server=server)
        self._app = server

        return server

    def _set_up(self, server: fastapi.FastAPI) -> None:
        server.add_exception_handler(
            exc_class_or_status_code=exceptions.ApiError,
            handler=exceptions.handle_exception,
        )
        server.include_router(self._v1_router.router)
        server.include_router(self._health_checks_router.router)
