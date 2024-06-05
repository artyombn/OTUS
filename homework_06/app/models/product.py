from sqlalchemy import String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from .database import db


# Чтобы сделать уникальное поле, нужно добавлять mapped_column
class Product(db.Model):
    name: Mapped[str] = mapped_column(String(100), unique=True)
    price: Mapped[int]
