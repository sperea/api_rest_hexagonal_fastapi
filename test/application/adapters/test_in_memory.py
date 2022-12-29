from app.adapters.in_memory import InMemoryUserRepository
from app.domain.user import User


def test_user_save():
    user = User()
    user_repository = InMemoryUserRepository()

    assert user.save(user_repository).user_id == user.user_id


def test_user_repository_all():
    user_repository = InMemoryUserRepository()
    user1 = User().save(user_repository)
    user2 = User().save(user_repository)

    assert set(user_repository.all()) == {user1, user2}


def test_user_repository_total():
    user_repository = InMemoryUserRepository()
    User().save(user_repository)
    User().save(user_repository)

    assert user_repository.total() == 2