

def test_find_by_id(session):
    user_query_service = UserQueryServiceImpl(session)

    # Insert a user into the database
    user_dto = UserDTO(
        id="123",
        username="johndoe",
        password="password",
        email="johndoe@example.com",
        created_at=unixtimestamp(),
        updated_at=unixtimestamp()
    )
    session.add(user_dto)
    session.commit()

    # Find the user by id
    user = user_query_service.find_by_id("123")
    assert isinstance(user, UserReadModel)
    assert user.id == "123"
    assert user.username == "johndoe"
    assert user.password == "password"
    assert user.email == "johndoe@example.com"
    
    
def test_find_by_id_not_found(session):
    user_query_service = UserQueryServiceImpl(session)

    # Find a user that does not exist
    user = user_query_service.find_by_id("123")
    assert user is None
    
    
def test_find_all(session):
    user_query_service = UserQueryServiceImpl(session)

    # Insert several users into the database
    user_dtos = [
        UserDTO(
            id="123",
            username="b",
            password="password",
            email="b@example.com",
            created_at=unixtimestamp(),
            updated_at=unixtimestamp()
        ),
        UserDTO(
            id="456",
            username="a",
            password="password",
            email="a@example.com",
            created_at=unixtimestamp(),
            updated_at=unixtimestamp()
        ),
        UserDTO(
            id="789",
            username="c",
            password="password",
            email="c@example.com",
            created_at=unixtimestamp(),
            updated_at=unixtimestamp()
        )
    ]
    for user_dto in user_dtos:
        session.add(user_dto)
    session.commit()

    # Find all users
    users = user_query_service.find_all()

    # Assert that the list of users has the correct size
    assert len(users) == 3

    # Assert that the users are sorted by username
    assert users[0].id == "456"
    assert users[1].id == "123"
    assert users[2].id == "789"