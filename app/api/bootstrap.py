import punq

from app.api import health_checks, v1
from app.core import database, settings


def resolve_resources(config: settings.ApiSettings) -> punq.Container:
    container = punq.Container()

    # Sources
    container.register(
        service=database.Database,
        factory=database.Database,
        scope=punq.Scope.singleton,
        config=config.database,
    )

    resolve_high_level_routers(container=container)

    return container


def resolve_high_level_routers(container: punq.Container):
    # container.register(service=v1.router.V1Router)
    container.register(service=health_checks.router.HealthChecksRouter)
