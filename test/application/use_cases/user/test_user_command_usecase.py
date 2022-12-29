from unittest.mock import Mock

def test_user_command_use_case(user_repository):
    uow = Mock()
    uow.user_repository = user_repository

    user_command_use_case = UserCommandUseCaseImpl(uow)

    # Create a user
    create_model = UserCreateModel(
        username="johndoe",
        password="password",
        email="johndoe@example.com"
    )
    user = user_command_use_case.create_user(create_model)
    assert isinstance(user, UserReadModel)
    assert user.username == "johndoe"
    assert user.password == "password"
    assert user.email == "johndoe@example.com"
    assert user_repository.find_by_id(user.id) is not None