from .domain import User, UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: User) -> int:
        return self.repository.create_user(user)

    def get_user(self, user_id: int) -> User:
        return self.repository.get_user(user_id)

    def update_user(self, user: User) -> User:
        return self.repository.update_user(user)

    def delete_user(self, user_id: int) -> None:
        return self.repository.delete_user(user_id)