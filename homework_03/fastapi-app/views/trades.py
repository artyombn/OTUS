from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/trades",
    tags=["trades"],
)


fake_trades = [
    {
        "id": 1,
        "user_id": 1,
        "currency": "BTC",
        "side": "buy",
        "price": 123,
        "amount": 2.12,
    },
    {
        "id": 2,
        "user_id": 1,
        "currency": "BTC",
        "side": "sell",
        "price": 125,
        "amount": 2.12,
    },
]


class Trades(BaseModel):
    id: int
    user_id: int
    currency: str = Field(min_length=3)
    side: str
    price: float = Field(ge=0)
    amount: float = Field(ge=0)


@router.get("/")
def get_trades(limit: int = 2, offset: int = 0):
    return fake_trades[offset:][:limit]


# @router.post("/")
# def create_trade(trade: List[Trades]):
