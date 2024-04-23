from sqlalchemy import (
    Column,
    Integer,
    String,
)

from lessons.lesson_18.models.base import Base


class User(Base):
    # __tablename__ = "users" // @declared_attr используется в base.py
    # id = Column(Integer, primary_key=True) // наследуем из базового класса
    username = Column(
        String(32),
        nullable=False,
        unique=True,
    )

    email = Column(
        String,
        nullable=True,
        unique=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"email={self.email!r})"
            f")"
        )
