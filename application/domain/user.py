import uuid
import abc
from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class User:

    vote_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def save(self, user_repository: 'UserRepository'):
        return user_repository.add(self)

    def __hash__(self):
        return hash(self.user_id)


class UserRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
