"""
Пример синхронного подхода
То есть общее время выполнения всех операций = время 1 + время 2
"""

import logging
from time import sleep

from common import configure_logging

log = logging.getLogger(__name__)


def get_weather():
    log.info("Start getting weather...")
    sleep(1)
    log.info("Done, got weather")


def get_currencies():
    log.info("Start getting currencies...")
    sleep(1)
    log.info("Done, got currencies")


def main():
    configure_logging()
    log.info("Star step 0")

    get_weather()
    get_currencies()

    log.info("End step 0")


if __name__ == "__main__":
    main()
