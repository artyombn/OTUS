from typing import List
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/trades", tags=["Trades"])

class Trades(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    action: str
    price: int = Field(ge=0)
    amount: float


trades_list = [
]

@router.post("/create/")
def create_trade(trade: Trades):
    trades_list.append(trade.model_dump())
    return {"status": 200, "data": trades_list}

@router.get("/get_trades/", response_model=List[Trades])
def get_all_trades():
    return trades_list

@router.get("/{trade_id}/", response_model=List[Trades])
def get_trade(trade_id: int = 0):
    return [trade for trade in trades_list if trade.get("id") == trade_id]

@router.delete("/delete/{trade_id}/")
def delete_trade(trade_id: int):
    a = [trade for trade in trades_list if trade.get("id") == trade_id]
    trades_list.remove(a[0])
    return {"message": f"Trade_id ({trade_id}) has been deleted"}