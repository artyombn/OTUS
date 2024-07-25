"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models_p.user import User
from models_p.post import Post

from models import async_engine, Session
from models_p.base import Base


from sqlalchemy import (
    select,
)


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(
    session: AsyncSession,
    name: str,
    username: str,
    email: str | None = None,
    refresh_after_commit: bool = False,
) -> User:
    user = User(name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    if refresh_after_commit:
        await session.refresh(user)
    print("created user:", user)
    return user


async def create_posts(
    session: AsyncSession,
    *titles: str,
    user_id: int,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in titles]
    session.add_all(posts)
    await session.commit()
    print("created posts:", posts)
    return posts


async def fetch_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    res = await session.scalars(stmt)
    users = res.all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


async def fetch_all_posts(
    session: AsyncSession,
) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    res = await session.scalars(stmt)
    posts = res.all()
    posts_list = list(posts)
    for post in posts_list:
        print(post)
    return posts_list


async def demo(session: AsyncSession) -> None:

    user_john: User = await create_user(
        session, "john", "johny", "john@example.com", refresh_after_commit=True
    )
    user_sam: User = await create_user(session, "sam", "samsam", "sam@example.com")
    user_nick: User = await create_user(session, "nick", "sarnick", "nick@example.com")

    await create_posts(
        session,
        "Fintech",
        "Health",
        "Wealth",
        user_id=user_sam.id,
    )

    await create_posts(
        session,
        "Love",
        "Society",
        "Kids",
        user_id=user_john.id,
    )

    await create_posts(
        session,
        "Dogs",
        "Robots",
        "People",
        user_id=user_nick.id,
    )


async def async_main():
    await init_db()

    async with Session() as session:
        await demo(session)
        await fetch_all_users(session)
        await fetch_all_posts(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
