from typing import Annotated
from fastapi import APIRouter, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


data = {
    "data": [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ]
}


@router.get("/")
def get_item_list():
    return data


@router.get("/{item_id}")
def get_item(item_id: Annotated[int, Path(lt=1_000_000, gt=0)]):
    return {
        "data": {
            "id": item_id,
            "name": f"Item {item_id}",
        },
    }


class ItemCreate(BaseModel):
    name: str
    description: str


@router.post("")
def create_item(
    item: ItemCreate,
):
    return {
        "data": {
            "id": 0,
            "name": item.name,
            "description": item.description,
        },
    }
