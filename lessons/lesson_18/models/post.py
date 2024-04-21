from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime,
    Text,
    func,
)

from lessons.lesson_18.models.base import Base


class Post(Base):
    # __tablename__ = "posts" // @declared_attr используется в base.py
    # id = Column(Integer, primary_key=True) // наследуем из базового класса

    title = Column(
        String(100),
        nullable=False,
        default="",  # определяет дефолтное значение в случае если для столбца оно не указано (используется чисто в алхимии)
        server_default="",  # определяет дефолтное значение на стороне БД, а не Python кода
        # предпочтительно использовать тогда, когда значение по умолчанию определяется лучше на стороне БД, чем на стороне Python-кода
    )
    body = Column(
        Text,
        default="",
        server_default="",
    )

    published_at = Column(
        DateTime(timezone=False),
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),  # путь до колонки в табличке users(User)
        unique=False,  # у одного юзера может быть много постов
        nullable=False,  # чтобы не было поста без user
    )
