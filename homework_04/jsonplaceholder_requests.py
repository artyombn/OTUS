"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import logging

import aiohttp

from homework_04.common import configure_logging

log = logging.getLogger(__name__)

USERS_DATA_URL = "http://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "http://jsonplaceholder.typicode.com/posts"
USER_ID = 2


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_user_by_id(users, user_id) -> list:
    for user in users:
        if user["id"] == user_id:
            return user
    return None


async def fetch_post_by_user_id(posts, user_id) -> list:
    for post in posts:
        if post["userId"] == user_id:
            return post
    return None


async def main():
    configure_logging()
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_json(USERS_DATA_URL))
        task2 = tg.create_task(fetch_json(POSTS_DATA_URL))
    users = task1.result()
    posts = task2.result()
    # log.info("Fetching users data: %s", users)
    # log.info("Fetching posts data: %s", posts)
    get_user = await fetch_user_by_id(users, USER_ID)
    get_post = await fetch_post_by_user_id(posts, USER_ID)
    log.info("Fetching user data by User id: %s", get_user)
    log.info("Fetching post data by User id: %s", get_post)


if __name__ == "__main__":
    asyncio.run(main())
