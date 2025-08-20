from logging.config import fileConfig
import os
import sys

from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

# ----------------------------------------------------------------------
# Пути
# ----------------------------------------------------------------------
# Папка проекта (корень, где лежит alembic.ini и src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")

# Добавляем src/ в sys.path, чтобы видеть backend и models
if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

# ----------------------------------------------------------------------
# Загружаем переменные окружения (.env)
# ----------------------------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Alembic Config
config = context.config
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Логирование
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ----------------------------------------------------------------------
# Импорт моделей
# ----------------------------------------------------------------------
from src.one_star_booking.backend.session import Base
from src.one_star_booking.model import hotel, booking  # просто импортируем, чтобы alembic их увидел

target_metadata = Base.metadata

# ----------------------------------------------------------------------
# Миграции
# ----------------------------------------------------------------------
def run_migrations_offline() -> None:
    """Запуск миграций в offline-режиме"""
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
    """Запуск миграций в online-режиме"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()