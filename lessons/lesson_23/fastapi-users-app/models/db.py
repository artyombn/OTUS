"""
Движок для подключения/взаимодействия
"""

from sqlalchemy import create_engine

from lessons.lesson_19 import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,  # только для отладки
)
