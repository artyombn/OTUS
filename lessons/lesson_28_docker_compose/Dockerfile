FROM python:3.11.9-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip "poetry==1.8.2"

RUN poetry config virtualenvs.create false --local

RUN poetry install

COPY . /app

EXPOSE 5000

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]





