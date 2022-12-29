from typing import cast
from pydantic import BaseModel, Field
from application.domain.user.user import User


class UserReadModel(BaseModel):
    """UserReadModel represents data structure as a read model."""

    id: str = Field(example="vytxeTZskVKR7C7WgdSP3d")
    username: str = Field(example="XXX")
    password: str = Field(example="XXX")
    email: str = Field(example="XXX")

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(user: User) -> "UserReadModel":
        return UserReadModel(
            id=user.id,
            username=user.username,
            password=user.password,
            email=user.email,
        )