from datetime import datetime
from typing import Union

from sqlalchemy import Column, Integer, String

from application.domain.user import User
from application.infrastructure.postgresql.database import Base
from application.usecase.user import UserReadModel


def unixtimestamp() -> int:
    return int(datetime.now().timestamp() * 1000)


class UserDTO(Base):
    """UserDTO is a data transfer object associated with User entity."""

    __tablename__ = "user"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    username: Union[str, Column] = Column(String(50), unique=True, nullable=False)
    password: Union[str, Column] = Column(String(50), unique=True, nullable=False)
    email: Union[str, Column] = Column(String(50), unique=True, nullable=False)
    created_at: Union[int, Column] = Column(Integer, index=True, nullable=False)
    updated_at: Union[int, Column] = Column(Integer, index=True, nullable=False)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            username=self.username,
            password=self.password,
            email=self.email,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_read_model(self) -> UserReadModel:
        return UserReadModel(
            id=self.id,
            username=self.username,
            password=self.password,
            email=self.email,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(user: User) -> "UserDTO":
        now = unixtimestamp()
        return UserDTO(
            id=user.id,
            username=user.username,
            password=user.password,
            email=user.email,
            created_at=now,
            updated_at=now,
        )