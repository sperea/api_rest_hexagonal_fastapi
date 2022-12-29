
from abc import ABC, abstractmethod
from typing import Optional, cast

import shortuuid

from application.domain.user import (
    User,
    UserIsbnAlreadyExistsError,
    UserNotFoundError,
    UserRepository
)

from .user_command_model import UserCreateModel, UserUpdateModel
from .user_query_model import UserReadModel


class UserCommandUseCaseUnitOfWork(ABC):
    """UserCommandUseCaseUnitOfWork defines an interface based on Unit of Work pattern."""

    user_repository: UserRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class UserCommandUseCase(ABC):
    """UserCommandUseCase defines a command usecase inteface related User entity."""

    @abstractmethod
    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, id: str, data: UserUpdateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_user_by_id(self, id: str):
        raise NotImplementedError


class UserCommandUseCaseImpl(UserCommandUseCase):
    """UserCommandUseCaseImpl implements a command usecases related User entity."""

    def __init__(
        self,
        uow: UserCommandUseCaseUnitOfWork,
    ):
        self.uow: UserCommandUseCaseUnitOfWork = uow

    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        try:
            uuid = shortuuid.uuid()
            user = User(id=uuid, username=data.username,
                        password=data.password, email=data.email)

            existing_user = self.uow.user_repository.find_by_username(
                data.username)
            if existing_user is not None:
                raise UsernameAlreadyExistsError

            existing_user = self.uow.user_repository.find_by_email(data.email)
            if existing_user is not None:
                raise EmailAlreadyExistsError

            self.uow.user_repository.create(user)
            self.uow.commit()

            created_user = self.uow.user_repository.find_by_id(uuid)
        except:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(User, created_user))

    def update_user(self, id: str, data: UserUpdateModel) -> Optional[UserReadModel]:
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            user = User(
                id=id,
                username=existing_user.username,
                password=data.password,
                email=data.email,
            )

            self.uow.user_repository.update(user)

            updated_user = self.uow.user_repository.find_by_id(user.id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(User, updated_user))

    def delete_user_by_id(self, id: str):
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            self.uow.user_repository.delete_by_id(id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class UserCommandUseCase(ABC):
    """UserCommandUseCase defines a command usecase inteface related User entity."""

    @abstractmethod
    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, id: str, data: UserUpdateModel) -> Optional[UserReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_user_by_id(self, id: str):
        raise NotImplementedError


class UserCommandUseCaseImpl(UserCommandUseCase):
    """UserCommandUseCaseImpl implements a command usecases related User entity."""

    def __init__(
        self,
        uow: UserCommandUseCaseUnitOfWork,
    ):
        self.uow: UserCommandUseCaseUnitOfWork = uow

    def create_user(self, data: UserCreateModel) -> Optional[UserReadModel]:
        try:
            uuid = shortuuid.uuid()
            user = User(id=uuid, username=data.username,
                        password=data.password, email=data.email)

            existing_user = self.uow.user_repository.find_by_username(
                data.username)
            if existing_user is not None:
                raise UsernameAlreadyExistsError

            existing_user = self.uow.user_repository.find_by_email(data.email)
            if existing_user is not None:
                raise EmailAlreadyExistsError

            self.uow.user_repository.create(user)
            self.uow.commit()

            created_user = self.uow.user_repository.find_by_id(uuid)
        except:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(User, created_user))

    def update_user(self, id: str, data: UserUpdateModel) -> Optional[UserReadModel]:
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            user = User(
                id=id,
                username=existing_user.username,
                password=data.password,
                email=data.email,
            )

            self.uow.user_repository.update(user)

            updated_user = self.uow.user_repository.find_by_id(user.id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

        return UserReadModel.from_entity(cast(User, updated_user))

    def delete_user_by_id(self, id: str):
        try:
            existing_user = self.uow.user_repository.find_by_id(id)
            if existing_user is None:
                raise UserNotFoundError

            self.uow.user_repository.delete_by_id(id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise
