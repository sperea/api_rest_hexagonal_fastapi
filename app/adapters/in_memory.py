from typing import List

from app.domain.user import User
from app.domain.user import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def add(self, user: User) -> User:
        self.users.append(user)
        return user

    def all(self) -> List[User]:
        return self.users

    def total(self) -> int:
        return len(self.users)