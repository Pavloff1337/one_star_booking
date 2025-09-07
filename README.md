Чтобы запустить сервер uvicorn нужно использовать 
poetry run uvicorn src.one_star_booking.main:app
Так же в .env нужно помять подключение к бд тк как щас подключение идет к бд которая находится в контейнере  
DATABASE_URL=postgresql+psycopg2://admin:12345@db:5432/booking данное подключение контейнерное 
DATABASE_URL=postgresql+psycopg2://admin:12345@localhost:5432/booking локальное подключение к бд на пк 

 




