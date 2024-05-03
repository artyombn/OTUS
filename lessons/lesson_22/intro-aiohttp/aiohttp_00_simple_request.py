import asyncio
import logging

import aiohttp
from common import configure_logging

log = logging.getLogger(__name__)


HTTPBIN_URL = "http://httpbin.org/get"


async def fetch_api(url: str, params: dict | None = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()


async def main():
    configure_logging()
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_api(HTTPBIN_URL))
        task2 = tg.create_task(
            fetch_api(
                HTTPBIN_URL,
                params={
                    "name": "OTUS",
                    "foo": ["bar", "baz"],
                    "spam": "eggs",
                },
            )
        )

    log.info("Fetch data (1): %s", task1.result())
    log.info("Fetch data (2): %s", task2.result())

    data = await fetch_api(
        HTTPBIN_URL,
        params={
            "name": "OTUS",
            "foo": ["bar", "baz"],
            "spam": "eggs",
        },
    )
    log.info("Fetch data %s", data)


if __name__ == "__main__":
    asyncio.run(main())
