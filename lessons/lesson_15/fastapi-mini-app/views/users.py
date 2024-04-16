"""
CRUD users
"""

from typing import List

from fastapi import APIRouter, Body, Query
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

LAST_ID = 1


class Users(BaseModel):
    name: str
    role: str


list_users = []


@router.post("/new", operation_id="1_create_user")
def create_user(user: List[Users]):
    global LAST_ID

    for usr in user:
        us_dict = {}
        us_dict["id"] = LAST_ID
        user_dict = usr.dict()
        us_dict.update(user_dict)
        list_users.append(us_dict)
        LAST_ID += 1

    return f"New user created: {user}"


# @router.post("/new", operation_id="1_create_user")
# def create_user(user: Users):
#     global LAST_ID
#     list_users.append(user.model_dump())
#     LAST_ID += 1
#
#     return f"New user created: {user}"


@router.get("/getall", operation_id="2_get_all_users")
def get_all_users():
    return list_users


@router.get("/get/{user_id}", operation_id="3_get_user")
def get_user(user_id: int):
    for user in list_users:
        if user["id"] == user_id:
            return user
    return "User not found"


@router.put("/updatefull/{user_id}", operation_id="4_full_update_user")
def full_update_user(user_id: int, user: Users):
    for index, usr in enumerate(list_users):
        if usr["id"] == user_id:
            old_user = list_users[index].copy()
            list_users[index]["name"] = user.name
            list_users[index]["role"] = user.role
            return f"User updated from {old_user} into {user}"
    return "User not found"


@router.delete("/delete/{user_id}", operation_id="5_delete_user")
def delete_user(user_id: int):
    for usr in list_users:
        if usr["id"] == user_id:
            k = usr
            list_users.remove(k)
            return f"User deleted: {k}"
    return "User not found"


@router.put("/update/{user_id}", operation_id="6_update_user_characteristic")
def update_user_characteristic(user_id: int, name: str = None, role: str = None):
    for index, usr in enumerate(list_users):
        if usr["id"] == user_id:
            previous_user = list_users[index].copy()
            list_users[index]["name"] = name if name is not None else usr["name"]
            list_users[index]["role"] = role if role is not None else usr["role"]
            return f"User updated from {previous_user} into {list_users[index]}"
    return "User not found"


@router.delete("/delete-several/", operation_id="5_delete_several_users")
def delete_several_users(user_ids: List[int] = Query(None)):
    users_to_delete = []
    users_not_found = []

    for user_id in user_ids:
        found = False
        for usr in list_users:
            if usr["id"] == user_id:
                users_to_delete.append(usr)
                found = True
                break
        if not found:
            users_not_found.append(user_id)

    if users_not_found:
        return f"Some users ({users_not_found}) not found"

    for user in users_to_delete:
        list_users.remove(user)

    return f"Users deleted: {users_to_delete}"
