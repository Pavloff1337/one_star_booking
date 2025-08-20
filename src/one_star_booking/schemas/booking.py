from pydantic import BaseModel, Field
from datetime import date

class BookingCreate(BaseModel):
    hotel_room_id: int
    start_date: date = Field(..., description="YYYY-MM-DD")
    end_date: date

class BookingResponse(BaseModel):
    id: int
    start_date: date
    end_date: date

    model_config = {"from_attributes": True}
