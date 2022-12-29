

def test_user_read_model(user):
    user_read_model = UserReadModel(
        id=user.id,
        username=user.username,
        password=user.password,
        email=user.email,
    )

    user_from_entity = UserReadModel.from_entity(user)
    assert user_from_entity.id == user_read_model.id
    assert user_from_entity.username == user_read_model.username
    assert user_from_entity.password == user_read_model.password
    assert user_from_entity.email == user_read_model.email