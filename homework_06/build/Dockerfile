FROM tiangolo/uwsgi-nginx-flask:python3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip "poetry==1.8.2"

RUN poetry config virtualenvs.create false --local

RUN poetry install

COPY ./build/prestart.sh /prestart.sh

COPY ../app/ ./

EXPOSE 5000

RUN chmod +x /prestart.sh

CMD ["/prestart.sh"]




