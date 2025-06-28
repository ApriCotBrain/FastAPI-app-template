from typing import Literal

import pydantic
import pydantic_settings


class BaseSettings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_nested_delimiter="__", env_file=".env", use_enum_values=True, extra="ignore"
    )


class DatabaseSettings(pydantic.BaseModel):
    dsn: pydantic.PostgresDsn
    engine_pool_size: int = pydantic.Field(default=20)
    engine_max_overflow: int = pydantic.Field(default=0)
    engine_pool_ping: bool = pydantic.Field(default=False)
    engine_pool_timeout: int = pydantic.Field(default=30)


class ServerSettings(pydantic.BaseModel):
    port: int = pydantic.Field(default=8000)
    workers: pydantic.PositiveInt = pydantic.Field(default=1)
    reload: bool = pydantic.Field(default=True)
    root_path: str = pydantic.Field(default="")


class SystemSettings(pydantic.BaseModel):
    environment: Literal["dev", "stage", "prod"] = pydantic.Field(description="Environment", default="dev")
    home_url: pydantic.HttpUrl = pydantic.Field(description="Path to home site")


class ApiSettings(BaseSettings):
    # Source
    database: DatabaseSettings

    # Server and System Settings
    server: ServerSettings
    system: SystemSettings

    # Logging
    logging_level: str = pydantic.Field(default="DEBUG")
