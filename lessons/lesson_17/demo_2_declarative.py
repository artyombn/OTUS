"""
Объекты в Python будут представлять собой таблички в БД
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase

from db import engine


class Base(DeclarativeBase):
    pass


"""
Декларативный стиль в SQLAlchemy позволяет определять классы, которые соответствуют таблицам базы данных, 
без явного описания структуры таблицы. Вместо этого вы определяете классы, которые являются подклассами DeclarativeBase, 
и используете специальные атрибуты класса для описания структуры таблицы.
"""


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)


# Base.metadata


"""
CREATE TABLE authors (
	id SERIAL NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (usernamename), 
	UNIQUE (email)
);
"""


def main():
    print()
    print("Base_MetaData:", Base.metadata.tables)
    print()
    print("Authors_Table:", Author.__table__, repr(Author.__table__))
    print()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
