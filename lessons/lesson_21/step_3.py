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
    return {"weather": ["sunny", "cloudy", "rainy", "snowy"]}


async def get_currencies():
    log.info("Start getting currencies...")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():  # не возвращает результат выполнения ф-ции
    configure_logging()
    log.info("Star step 3")

    coro_currencies = get_currencies()  # корутина
    log.info("Coro get currencies: %s", coro_currencies)

    res = await asyncio.gather(
        get_weather(),
        coro_currencies,
    )

    res_weather, res_currencies = res
    log.info("Result get weather: %s", res_weather)
    log.info("Result get currencies: %s", res_currencies)

    log.info("End step 3")


if __name__ == "__main__":
    asyncio.run(main())
