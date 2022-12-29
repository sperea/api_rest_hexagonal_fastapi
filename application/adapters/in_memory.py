from typing import List

from application.domain.user import User
from application.domain.user import UserRepository


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