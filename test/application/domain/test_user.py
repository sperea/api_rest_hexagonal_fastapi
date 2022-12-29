import uuid

from app.domain.user import User


def test_create_user():
    user = User("123", "johndoe", "password", "johndoe@example.com")
    assert user.id == "123"
    assert user.username == "johndoe"
    assert user.password == "password"
    assert user.email == "johndoe@example.com"
    
def test_user_equality():
    user1 = User("123", "johndoe", "password", "johndoe@example.com")
    user2 = User("123", "janedoe", "password123", "janedoe@example.com")
    assert user1 == user2
    
def test_user_inequality():
    user1 = User("123", "johndoe", "password", "johndoe@example.com")
    user2 = User("456", "janedoe", "password123", "janedoe@example.com")
    assert user1 != user2
    
def test_user_equality_with_other_object():
    user = User("123", "johndoe", "password", "johndoe@example.com")
    other_object = {"id": "123"}
    assert user != other_object