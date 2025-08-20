import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL БД берём из ENV (или дефолт для локалки)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://user:password@localhost:5432/hotel_db",
)

class Base(DeclarativeBase):
    """Базовый класс декларативных моделей (SQLAlchemy 2.0)."""
    pass

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

def get_db():
    """Dependency для FastAPI: создаёт/закрывает сессию."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
