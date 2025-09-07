Чтобы запустить сервер uvicorn нужно использовать 
poetry run uvicorn src.one_star_booking.main:app
Так же в .env нужно помять подключение к бд тк как щас подключение идет к бд которая находится в контейнере  
DATABASE_URL=postgresql+psycopg2://admin:12345@db:5432/booking данное подключение контейнерное 
DATABASE_URL=postgresql+psycopg2://admin:12345@localhost:5432/booking локальное подключение к бд на пк 

Так же для проверки работы swagger нужно заходить по адресу http://127.0.0.1:8000/docs#/
 

Для запуска через powershell нужно перейти по пути C:\Users\pawa2\PycharmProjects\one_star_booking
и запустить команду make dev-up


