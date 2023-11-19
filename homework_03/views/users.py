from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/users", tags=["Users"])

class User(BaseModel):
    id: int
    role: str
    name: str
    email: EmailStr


user_list = [
    {"id": 1, "role": "admin", "name": "Ivan", "email": "Ivan@example.com"},
    {"id": 2, "role": "student", "name": "Dima", "email": "Dima@example.com"},
    {"id": 3, "role": "tester", "name": "Boris", "email": "Boris@example.com"},
]

@router.get("/get_users/")
def get_all_users():
    return [f"{user['id']}: {user['name']} ({user['role']}) ({user['email']})" for user in user_list]

@router.get("/{user_id}/", response_model=List[User])
def get_user(user_id: int = 0):
    return [user for user in user_list if user['id'] == user_id]

@router.put("/{user_id}/")
def change__name(user_id: int, new_name: str):
    last_list = user_list
    current_user = list(filter(lambda user: user.get("id") == user_id, user_list))[0]
    current_user["name"] = new_name
    return {"message": f"User name has been changed. Last name: {[user.get('name') for user in last_list if user.get('id') == user_id][0]}. New name: {new_name}"}

@router.post("/create/")
def create_user(user: User):
    user_list.append(user.model_dump())
    return {"message": f"New user has been added ({user.model_dump()['id']} {user.model_dump()['name']} {user.model_dump()['role']} {user.model_dump()['email']})"}

@router.delete("/delete/{user_id}/")
def delete_user(user_id: int):
    a = [user for user in user_list if user['id'] == user_id]
    user_list.remove(a[0])
    return {"message": f"User_id ({user_id}) has been deleted"}

