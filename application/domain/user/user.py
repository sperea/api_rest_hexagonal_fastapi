import uuid
import abc
from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class User:

    def __init__(
        self,
        id: str,
        username: str,
        password: str,
        email: str
    ):
        self.id: str = id
        self.username: str = username
        self.password: str = password
        self.email: str = email

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id

        return False



