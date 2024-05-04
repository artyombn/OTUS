"""
Движок для подключения/взаимодействия
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from lessons.lesson_22.config import DB_URL, DB_ECHO

from lessons.lesson_22 import config

async_engine = create_async_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)
