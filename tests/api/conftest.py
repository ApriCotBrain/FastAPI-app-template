import httpx
import punq
import pytest

from app.api import application, health_checks, v1
from app.api.v1 import template
from app.core import database


@pytest.fixture(scope="package")
def test_app(
    test_database,
    test_config,  # noqa: ARG001
):
    container = punq.Container()

    # Source
    container.register(service=database.Database, instance=test_database)

    # Template App
    container.register(service=template.base.router.TemplateBaseRouter)
    container.register(service=template.base.service.TemplateService)
    container.register(service=template.base.repository.TemplateRepository)

    # High Level Routers
    container.register(service=v1.router.V1Router)
    container.register(service=health_checks.router.HealthChecksRouter)
    container.register(service=application.Application)

    return container.resolve(service_key=application.Application).app


@pytest.fixture(scope="package")
async def test_client(test_app):
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=test_app), base_url="http://test"
    ) as client:
        yield client
