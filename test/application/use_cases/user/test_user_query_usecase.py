from unittest.mock import Mock

def test_fetch_user_by_id():
    # Create a mock for the user query service
    user_query_service = Mock()

    # Define the behavior of the mock
    user_query_service.find_by_id.return_value = UserReadModel(
        id="123",
        username="johndoe",
        password="password",
        email="johndoe@example.com"
    )

    user_query_use_case = UserQueryUseCaseImpl(user_query_service)

    # Fetch the user by idclass UserCreateModel(BaseModel):
    """UserCreateModel represents a write model to create a user."""

    username: str = Field(example="testusername")
    password: str = Field(example="testusername")
    email: str = Field(example="testusername@domain.com")
    user = user_query_use_case.fetch_user_by_id("123")
    assert isinstance(user, UserReadModel)
    assert user.id == "123"
    assert user.username == "johndoe"
    assert user.password == "password"
    assert user.email == "johndoe@example.com"


    
def test_fetch_user_by_id_not_found():
    user_query_use_case = UserQueryUseCaseImpl(user_query_service)

    # Set up an empty list of users in the query service
    user_query_service.users = []

    # Try to fetch a user that does not exist
    try:
        user_query_use_case.fetch_user_by_id("123")
        assert False, "Exception not raised"
    except UserNotFoundError:
        assert True
    except:
        assert False, "Wrong exception raised"
        
        

def test_fetch_users(user_query_service):
    user_query_use_case = UserQueryUseCaseImpl(user_query_service)

    # Set up a list of users in the query service
    user_query_service.users = [
        UserReadModel(
            id="123",
            username="johndoe",
            password="password",
            email="johndoe@example.com"
        ),
        UserReadModel(
            id="456",
            username="janedoe",
            password="password",
            email="janedoe@example.com"
        )
    ]

    # Fetch the users
    users = user_query_use_case.fetch_users()

    # Assert that the list of users is a list
    assert isinstance(users, list)

    # Assert that the list of users has the correct size
    assert len(users) == 2