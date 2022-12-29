import uuid

from app.domain.user import User


def test_user_existing_user_id():
    user_id = str(uuid.uuid4())
    assert User(user_id).user_id == user_id


def test_vote_defaults():
    user_id = str(uuid.uuid4())
    assert User().user_id != user_id
