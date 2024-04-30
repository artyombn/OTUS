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
    d = {}
    for i in range(7_000):
        d[i] = i**i
        # Получаем синхронное действие, которое только на CPU
        if i % 100 == 0:
            await asyncio.sleep(0)  # для передачи информации через каждые i % 100

    log.info("For real get currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():  # не возвращает результат выполнения ф-ции
    configure_logging()
    log.info("Star step 7")

    coro_currencies = get_currencies()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(get_weather())
        tg.create_task(coro_currencies)

    log.info("End step 7")


if __name__ == "__main__":
    asyncio.run(main())
