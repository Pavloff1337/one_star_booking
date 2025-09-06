from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..backend.session import get_db
from ..model.booking import Booking
from ..schemas import BookingCreate, BookingResponse

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/create", response_model=dict)
def add_booking(data: BookingCreate, db: Session = Depends(get_db)):
    """Добавить бронь"""
    booking = Booking(**data.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return {"booking_id": booking.id}


@router.delete("/delete/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    """Удалить бронь"""
    db.query(Booking).filter(Booking.id == booking_id).delete(synchronize_session=False)
    db.commit()
    return {"status": "deleted"}


@router.get("/list", response_model=list[BookingResponse])
def list_bookings(room_id: int, db: Session = Depends(get_db)):
    """Получить список броней по номеру"""
    return (
        db.query(Booking)
        .filter(Booking.hotel_room_id == room_id)
        .order_by(Booking.start_date.asc())
        .all()
    )
