# DOCKER RUNNING GUIDE:
# Python image: https://hub.docker.com/_/python

# Use this command to run docker:
# docker run -p 8080:8000 -it app

# Result: http://0.0.0.0:8080
# http://localhost:8080

FROM python:3.9-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip "poetry==1.7.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]