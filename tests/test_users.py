from app import schemas
from .database import client, session
import pytest

@pytest.fixture
def test_user(client):
    user_data = {"email": "deadpool@example.com", "password": "chimichangas4life"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    

def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 201, response.text

def test_login_user(client):
    response = client.post(
        "/login",
        data={"username": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 200