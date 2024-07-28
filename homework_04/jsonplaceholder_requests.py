"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import logging

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)

USERS_DATA_URL = "http://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "http://jsonplaceholder.typicode.com/posts"
USER_ID = 2


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data(url: str = USERS_DATA_URL) -> list[dict]:
    return await fetch_json(url)


async def fetch_posts_data(url: str = POSTS_DATA_URL) -> list[dict]:
    return await fetch_json(url)


async def fetch_user_by_id(users, user_id) -> dict:
    for user in users:
        if user["id"] == user_id:
            return user
    return None


async def fetch_posts_by_user_id(posts, user_id) -> list:
    return [post for post in posts if post["userId"] == user_id]


async def main():
    configure_logging()

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            users_task = tg.create_task(fetch_users_data())
            posts_task = tg.create_task(fetch_posts_data())

        users = await users_task
        posts = await posts_task

        # log.info("Fetched users data: %s", users)
        # log.info("Fetched posts data: %s", posts)

        get_user = await fetch_user_by_id(users, USER_ID)
        get_posts = await fetch_posts_by_user_id(posts, USER_ID)

        log.info("Fetched user data by User ID: %s", get_user)
        log.info("Fetched posts data by User ID: %s", get_posts)


if __name__ == "__main__":
    asyncio.run(main())
