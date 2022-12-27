import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .repositories import create_user, read_user, update_user, delete_user
from .domain import User
from .infrastructure import Base, User as UserModel

# Crea la conexión a la base de datos y la sesión
DATABASE_URI = "postgresql://user:password@localhost/database"
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def test_create_user():
    # Crea un usuario
    user_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "password": "password"
    }
    user = User(**user_data)
    user_id = create_user(user)

    # Comprueba que se ha creado el usuario en la base de datos
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    assert user is not None
    assert user.name == user_data["name"]
    assert user.email == user_data["email"]
    assert user.password == user_data["password"]


def test_read_user():
    # Crea un usuario
    user_data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "password": "password"
    }
    user = User(**user_data)
    user_id = create_user(user)

    # Obtiene el usuario
    user = read_user(user_id)
    assert user.id == user_id
    assert user.name == user_data["name"]
    assert user.email == user_data["email"]


def test_update_user():
    # Crea un usuario
    user_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "password": "password"
    }
    user = User(**user_data)
    user_id = create_user(user)

    # Actualiza el usuario
    new_user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "new_password"
    }
    new_user = User(**new_user_data)
    update_user(user_id, new_user)

    # Comprueba que se ha actualizado el usuario en la base de datos
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    assert user is not None
    assert user.name == new_user_data["name"]
    assert user.email == new_user_data["email"]
    assert user.password == new_user_data["password"]


def test_delete_user():
    # Crea un usuario
    user_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "password": "password"
    }
    user = User(**user_data)
    user_id = create_user(user)

    # Elimina el usuario
    delete_user(user_id)

    # Comprueba que el usuario ya no existe en la base de datos
    user = session.query(UserModel).filter(UserModel.id == user_id).first()
    assert user is None
