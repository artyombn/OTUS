"""
CRUD functions for users

Create
Read
Update
Delete
"""

from fastapi import APIRouter
from sqlalchemy.orm import Session

from .users_schemas import User, UserCreate
from models import User


router = APIRouter(
    prefix="/users",
    tags=["CRUD users"],
)


# Делаем все через сессию
class UsersStorage:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_user(self, user_in: UserCreate) -> User:
        user = User(**user_in.model_dump())
        self.session.add(user)
        self.session.commit()
        return user

    def get_users(self) -> list[User]:
        return list(self.users.values())

    def get_user(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def delete_user(self, user_id: int) -> None:
        del self.users[user_id]
        return "User deleted"

    # def create_user(session: Session, user_in: UserCreate) -> User:
    #     user = User(id=self.next_id, **user_in.model_dump())
    #     self.users[user.id] = user
    #     return user
    #
    # def get_users(session: Session) -> list[User]:
    #     return list(self.users.values())
    #
    # def get_user(session: Session, user_id: int) -> User | None:
    #     return self.users.get(user_id)
