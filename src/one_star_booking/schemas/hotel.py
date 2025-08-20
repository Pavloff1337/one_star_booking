from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class HotelRoomCreate(BaseModel):
    description: str
    price_per_night: Decimal

class HotelRoomResponse(BaseModel):
    id: int
    description: str
    price_per_night: Decimal
    created_at: datetime

    model_config = {"from_attributes": True}
