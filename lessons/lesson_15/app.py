from fastapi import FastAPI

from views.users import router as user_router
from views.trades import router as trades_router

app = FastAPI(
    title="Trading app",
)
app.include_router(user_router)
app.include_router(trades_router)


@app.get("/")
def main():
    return {"Hello": "World"}
