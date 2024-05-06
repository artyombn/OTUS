"""
FastAPI
https://fastapi.tiangolo.com/ru/

Запустить можно через код или через терминал посредством gunicorn
https://gunicorn.org

Для асинхронной работы с кодом нужно использовать uvicorn
https://www.uvicorn.org

CRUD functions for users
Create
Read
Update
Delete

"""

__all__ = ("app",)
from app import app

# uvicorn main:app
# запускать нужно с каталога, где находится main
# или: uvicorn lessons.lesson_14.main:app
