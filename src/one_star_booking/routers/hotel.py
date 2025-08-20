from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..backend.session import get_db
from ..model.hotel import HotelRoom
from ..schemas import HotelRoomCreate, HotelRoomResponse

router = APIRouter(prefix="/hotels", tags=["Hotels"])

@router.post("/", response_model=int)
def add_hotel_room(data: HotelRoomCreate, db: Session = Depends(get_db)):
    room = HotelRoom(**data.model_dump())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room.id

@router.delete("/{room_id}")
def delete_hotel_room(room_id: int, db: Session = Depends(get_db)):
    db.query(HotelRoom).filter(HotelRoom.id == room_id).delete(synchronize_session=False)
    db.commit()
    return {"status": "deleted"}

@router.get("/", response_model=list[HotelRoomResponse])
def list_hotel_rooms(
    sort_by: str = "created_at",  # "price" | "created_at"
    order: str = "asc",           # "asc" | "desc"
    db: Session = Depends(get_db),
):
    q = db.query(HotelRoom)
    if sort_by == "price":
        q = q.order_by(
            HotelRoom.price_per_night.asc() if order == "asc" else HotelRoom.price_per_night.desc()
        )
    else:
        q = q.order_by(
            HotelRoom.created_at.asc() if order == "asc" else HotelRoom.created_at.desc()
        )
    return q.all()
