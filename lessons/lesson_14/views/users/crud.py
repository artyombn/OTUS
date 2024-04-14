"""
CRUD functions for users

Create
Read
Update
Delete
"""

from fastapi import APIRouter
from pydantic import BaseModel
from users_schemas import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["CRUD users"],
)


class Storage(BaseModel):
    users: dict[int, User] = {}
    last_id: int = 0

    def create_user(self, user_in: UserCreate) -> User:
        user = User(**user_in.model_dump())
        self.users[user.id] = user
        return user
