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
from sqlalchemy import select
from models import (
    User,
    Post,
    Base,
    async_engine,
    Session,
)

from jsonplaceholder_requests import (
    USERS_DATA_URL,
    POSTS_DATA_URL,
    fetch_users_data,
    fetch_posts_data,
)


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def fetch_all_data(
    users_url: str = USERS_DATA_URL,
    posts_url: str = POSTS_DATA_URL,
) -> (list[dict], list[dict]):
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(users_url), fetch_posts_data(posts_url)
    )
    return users_data, posts_data


async def create_data(session: AsyncSession):
    users_data, posts_data = await fetch_all_data()

    users = [
        User(name=item["name"], username=item["username"], email=item["email"])
        for item in users_data
    ]
    session.add_all(users)

    posts = [
        Post(title=item["title"], body=item["body"], user_id=item["userId"])
        for item in posts_data
    ]
    session.add_all(posts)

    await session.commit()


async def fetch_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    res = await session.scalars(stmt)
    users = res.all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


async def fetch_all_posts(session: AsyncSession) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    res = await session.scalars(stmt)
    posts = res.all()
    posts_list = list(posts)
    for post in posts_list:
        print(post)
    return posts_list


async def async_main():
    await init_db()

    async with Session() as session:
        await create_data(session)
        await fetch_all_users(session)
        await fetch_all_posts(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
