import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def test_migrations_apply_and_downgrade(test_config):
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", str(test_config.database.dsn))

    try:
        command.downgrade(alembic_cfg, "base")
        command.upgrade(alembic_cfg, "head")
    except Exception as e:  # noqa: BLE001
        pytest.fail(f"Ошибка при тестировании миграций: {e}")


def test_reflect_tables(test_config):
    from app.core.database import Base

    engine = create_engine(str(test_config.database.dsn))
    try:
        Base.metadata.reflect(engine)
    except SQLAlchemyError as e:
        pytest.fail(f"Есть ошибки с таблицами: {e}")

    assert Base.metadata.tables, "Метаданные не содержат ни одной таблицы!"


def test_relationships_are_valid():
    from sqlalchemy.orm import configure_mappers

    try:
        configure_mappers()
    except Exception as e:  # noqa: BLE001
        pytest.fail(f"Ошибка в связях или маппинге: {e}")
