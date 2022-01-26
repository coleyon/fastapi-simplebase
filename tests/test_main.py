from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_help():
    response = client.get("/help")
    assert response.status_code == 200
    assert response.json() == {"message": "Help"}


def test_login():
    response = client.get("/login")
    assert response.status_code == 200
    assert response.json() == {"message": "Login"}


def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"message": "Info"}
