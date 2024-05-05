from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello user"],
)


@router.get("/")
def hello_user(name: str, age: int):
    return {"message": f"Hello, {name}! Your age is {age}"}


@router.get("/{name}")
def hello_name_path(name: str):
    return {"message": f"Hello {name}!"}
