from typing import List
from decimal import Decimal
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, func, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..backend.session import Base

class HotelRoom(Base):
    __tablename__ = "hotel_rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price_per_night: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    bookings: Mapped[List["Booking"]] = relationship(
        back_populates="hotel_room",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
