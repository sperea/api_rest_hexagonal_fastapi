from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.domain.services import UserService

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: UserCreate):
    user_service = UserService()
    new_user_id = user_service.create_user(user.name, user.email)
    return new_user_id

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user_service = UserService()
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    user_service = UserService()
    updated_user = user_service.update_user(user_id, user.name, user.email)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user_service = UserService()
    user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}

router = app.router