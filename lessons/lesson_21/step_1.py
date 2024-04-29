"""
Пример асинхронного подхода
"""

import asyncio
import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather...")
    await asyncio.sleep(1)
    log.info("Done, got weather")


async def get_currencies():
    log.info("Start getting currencies...")
    await asyncio.sleep(1)
    log.info("Done, got currencies")


async def main():  # не возвращает результат выполнения ф-ции
    configure_logging()
    log.info("Star step 1")

    await get_weather()
    await get_currencies()

    log.info("End step 1")


if __name__ == "__main__":
    asyncio.run(main())
