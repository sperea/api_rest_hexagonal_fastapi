from application.domain.user.user import User

class UserRepository(ABC):

    @abstractmethod
    def create(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_username(self, id: str) -> Optional[User]:
        raise NotImplementedErrorUser