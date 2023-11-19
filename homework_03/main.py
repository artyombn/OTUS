from typing import Annotated
from fastapi import FastAPI, Query
from views import users_router, trades_router


app = FastAPI(
    title="My first FastApi project"
)
app.include_router(users_router)
app.include_router(trades_router)

@app.get("/")
def my_first_function():
    return "This is My First Function!"

@app.get("/hello/")
def hello_user(name: Annotated[str, Query(min_length=3)]):
    return f"Привет {name}! Рад тебя видеть"

@app.get("/ping/")
def ping():
    return {"message": "pong"}
