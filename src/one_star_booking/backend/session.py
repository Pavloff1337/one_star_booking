import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Загружаем переменные окружения (.env)
load_dotenv()

# Берём подключение из переменной окружения
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://admin:12345@localhost:5432/booking",  # fallback если нет .env
)

class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""
    pass

# Движок SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

# Сессия
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

# Dependency для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()