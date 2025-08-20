from fastapi import FastAPI
from .routers import hotel, booking

app = FastAPI(title="Hotel Booking API")

app.include_router(hotel.router)
app.include_router(booking.router)