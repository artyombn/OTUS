# Асинхронная работа с сетью и БД

**_HTTPX_** - это асинхронный HTTP клиент/сервер для Python, который основан на библиотеке asyncio. 
Предоставляет простой и эффективный способ для выполнения HTTP-запросов и создания веб-серверов в асинхронном режиме.
_https://www.python-httpx.org_

**_HTTPIE_** - инструмент командной строки для выполнения HTTP запросов. Он предоставляет удобный интерфейс для отправки запросов на серверы и просмотра ответов, прямо из терминала
_https://httpie.io_

**_AIOHTTP_** - это асинхронный фреймворк для работы с HTTP в Python, который основан на библиотеке asyncio. 
Позволяет создавать асинхронные веб-серверы, клиенты и веб-приложения
_https://docs.aiohttp.org/en/stable/_

`pip install aiohttp`

`asyncpgsa` - связка asyncpg движка и alchemy, но только в core режиме
_https://github.com/CanopyTax/asyncpgsa_

Для работы Alchemy с Async _(добавляем через poetry, файл pyproject.toml)_:  
`poetry add aiohttp`  
`poetry add "sqlalchemy[asyncio]"`  
`poetry add asyncpg`  


`alembic init -t async alembic` - сделать асинхронный alembic  



