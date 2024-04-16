FROM python:3.12.2-bookworm
#Посмотреть версию https://hub.docker.com/_/python/tags?page=&page_size=&ordering=&name=3.12.2
#Установить укзаанную версию сразу при запуске

ENV PYTHONUNBUFFERED=1
# Небуферизованный режим вывода.
#Вывод будет сразу отображаться на стандартном выводе (stdout) без задержки

WORKDIR /app
#Задать рабочую директорию

RUN pip install --upgrade pip poetry==1.8.2

RUN poetry config virtualenvs.create false --local
# Оключить создание venv при создании образа

COPY pyproject.toml poetry.lock ./
# ./ - копировать в рабочую директорию, которая WORKDIR

RUN poetry install --only main

COPY fastapi-mini-app ./

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
#Запустить команду при старте, --host 0.0.0.0 указываем, чтобы получить доступ внешне через заданный хост