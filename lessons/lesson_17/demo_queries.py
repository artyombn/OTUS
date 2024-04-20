"""
Запросы
"""

from sqlalchemy import select
from sqlalchemy import text
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import update
from sqlalchemy import func

from sqlalchemy.orm import DeclarativeBase, Session

from db import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

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


def create_tables():
    Base.metadata.create_all(engine)


def example_calc(session: Session):
    result = session.execute(select(1))
    print()
    print(result)
    # print("result_all:", result.all())  # вернет список из всех результатов
    # print(result.one())  # вернет одну запись (когда ожидается только один рез-т запроса
    print(result.scalar())  # для получения скалярного значения из результата запроса

    # SELECT 1 + 2;
    result = session.execute(select(text("1 + 2")))
    print(result.scalar())


# Добавление пользователей в таблицу:
def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print("created_user:", user)
    return user


def create_several_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    print()
    print("prepared users:", users)
    print()
    session.commit()
    print()
    print("created users:", users)
    return users


# Запрос вывода всех полей таблицы Users
def fetch_all_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


# Запрос вывода пользователя по id
def fetch_user_by_id(session: Session, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    user = session.scalar(stmt)
    print()
    print("User:", user)
    print()
    return user


# Запрос вывода пользователя по username
def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)
    print()
    print("User:", user)
    print()
    return user

# Обновление email пользователей
def update_users_emails(
    session: Session,
    username_len: int,
    email_domain: str,
):
    stmt = (
        update(User)
        .where(
            User.email.is_(None),
            func.length(User.username) > username_len,
        )
        .values(
            {
                User.email: func.concat(
                    func.lower(User.username), email_domain.lower()
                ),
                # User.username: 'Qwery',
            }
        )
    )

    result = session.execute(stmt)
    # print(result)
    session.commit()


def fetch_user_for_domain(session: Session, domain: str) -> list[User]:
    stmt = select(User).where(User.email.ilike(f"%{domain.lower()}"))
    users = session.scalars(stmt).all()
    print(f"Users for domain {domain}:", users)
    return users


def main():
    create_tables()

    with Session(engine) as session:
        # example_calc(session)
        # create_user(session, "John", "john@example.com")
        # create_user(session, "Sam", "sam@example.com")
        # create_several_users(
        #     session,
        #     "Bob",
        #     "Alice",
        #     "Nick",
        # )
        fetch_all_users(session)
        # fetch_user_by_id(session, 1)
        # fetch_user_by_id(session, 0)  # None
        # fetch_user_by_username(session, "John")
        # fetch_user_by_username(session, "David")  # None
        # fetch_user_by_username(session, "Sam")

        # update_users_emails(session, 3, email_domain="@ya.ru")
        # update_users_emails(session, 1, email_domain="@example.ru")
        fetch_all_users(session)
        fetch_user_for_domain(session, domain="@example.ru")
        fetch_user_for_domain(session, domain="@ya.ru")
        fetch_user_for_domain(session, domain="@example.com")


if __name__ == "__main__":
    main()
