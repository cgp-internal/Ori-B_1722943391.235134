from logging.config import fileConfig

from alembic import context
from sqlalchemy.engine import reflection
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from logging.config import fileConfig

config = context.config

fileConfig(config.config_file_name)

target_metadata = None

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        ctx = context.begin_transaction()
        try:
            context.run_migrations(connection=connection, transaction_context=ctx)
            ctx.commit()
        except:
            ctx.rollback()
            raise

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()