import logging

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core import settings
from app.core.database import models  # noqa: F401
from app.core.database import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
main_config = settings.ApiSettings()
sqlalchemy_url = main_config.database.dsn.unicode_string().replace("postgresql", "postgresql+asyncpg")
config.set_main_option("sqlalchemy.url", f"{sqlalchemy_url}?async_fallback=True")

log = logging.getLogger(__name__)

target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")  # noqa: ERA001
# ... etc.


def run_migrations_offline() -> None:
    """Run revisions in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run revisions in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # don't create empty revisions
    def process_revision_directives(context, revision, directives):  # noqa: ARG001
        script = directives[0]
        if script.upgrade_ops.is_empty():
            directives[:] = []
            log.info("No changes found skipping revision creation.")

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
