import pytest
from fastapi.testclient import TestClient

from .controllers import app

client = TestClient(app)

def test_create_user():
    # Crea un usuario
    user_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "password": "password"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"id": 1}

def test_read_user():
    # Crea un usuario
    user_data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "password": "password"
    }
    client.post("/users/", json=user_data)

    # Obtiene el usuario
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane@example.com"
    }

def test_update_user():
    # Crea un usuario
    user_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "password": "password"
    }
    client.post("/users/", json=user_data)

    # Actualiza el usuario
    new_user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "new_password"
    }
    response = client.put("/users/1", json=new_user_data)
    assert response.status_code == 200
    assert response.json() == {"id": 1}

def test_delete_user():
    # Crea un usuario
    user_data = {
        "name": "John Smith",
        "email": "john@example.com",
        "password": "password"
    }
    client.post("/users/", json=user_data)

    # Elimina el usuario
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1}