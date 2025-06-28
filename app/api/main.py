import punq

from app.api import application, bootstrap
from app.core import settings

config = settings.ApiSettings()
resources = bootstrap.resolve_resources(config=config)
resources.register(
    service=application.Application, factory=application.Application, scope=punq.Scope.singleton
)
app = resources.resolve(service_key=application.Application).app
