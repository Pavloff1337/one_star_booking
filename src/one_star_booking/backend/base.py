# Сборка метаданных для Alembic (импортируем модели, чтобы их видеть в metadata)
from ..backend.session import Base
from ..model.hotel import HotelRoom  # noqa: F401
from ..model.booking import Booking  # noqa: F401

__all__ = ["Base", "HotelRoom", "Booking"]

