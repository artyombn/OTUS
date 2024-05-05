from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from .base import Base


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

    bio = Column(
        String(200),
        nullable=True,
        unique=False,
    )

    posts = relationship(
        # to class name
        "Post",
        # how to access to this model[s]: post.'author'
        back_populates="author",
        # user can have any number of posts
        uselist=True,
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
