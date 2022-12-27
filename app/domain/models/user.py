from typing import List, Dict


class User:

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class UserRepository:
    def create_user(self, user: User) -> int:
        raise NotImplementedError()

    def get_user(self, user_id: int) -> User:
        raise NotImplementedError()

    def update_user(self, user: User) -> User:
        raise NotImplementedError()

    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError()
