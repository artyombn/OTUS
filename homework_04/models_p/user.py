from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    String,
)

from .base import Base


class User(Base):

    name = Column(String(32), nullable=False, unique=False)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    posts = relationship(
        # to class name
        "Post",
        # how to access to this model[s]: post.`user`
        back_populates="user",
        # user can have any number of posts
        uselist=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            f")"
        )
