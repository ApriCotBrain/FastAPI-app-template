import asyncio

import pydantic_settings
import pytest
import respx
import sqlalchemy

from app.core import database, settings


@pytest.fixture(scope="session")
async def test_config():
    class TestConfig(pydantic_settings.BaseSettings):
        model_config = pydantic_settings.SettingsConfigDict(
            env_nested_delimiter="__", env_file=".env", use_enum_values=True, extra="ignore"
        )
        # Source
        database: settings.DatabaseSettings
        server: settings.ServerSettings
        system: settings.SystemSettings

    yield TestConfig()


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_database(test_config):
    db = database.Database(config=test_config.database)
    yield db
    await db.shutdown()


@pytest.fixture
def mock_external_service():
    with respx.mock(base_url="http://0.0.0.0") as respx_mock:
        yield respx_mock


@pytest.fixture(scope="session")
async def clean_table(test_database: database.Database, clean_table: tuple):
    async for session in test_database.get_session():
        for table in clean_table:
            await session.execute(sqlalchemy.text(f'TRUNCATE "{table}" CASCADE'))
            await session.commit()


@pytest.fixture(autouse=True)
async def cleanup_table(test_database: database.Database):
    clean_table = ("template",)
    async for session in test_database.get_session():
        for table in clean_table:
            await session.execute(sqlalchemy.text(f'TRUNCATE "{table}" CASCADE;'))
            await session.commit()
