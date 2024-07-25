from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from .base import Base


class Post(Base):

    title = Column(
        String(80),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(Text, nullable=False, default="")

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        # to class name
        "User",
        # how to access to this model[s]: user.`posts`
        back_populates="posts",
        # author can be only one due to single `user_id`
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"title={self.title!r}, "
            f"user_id={self.user_id!r}, "
            f"body={self.body!r}"
            f")"
        )
