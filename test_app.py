import pytest
import json
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
    assert b"Flask demo application" in response.data


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["status"] == "healthy"
    assert "message" in data


def test_app_info(client):
    response = client.get("/info")
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data["app_name"] == "Flask CI/CD Demo"
    assert data["version"] == "1.0.0"
    assert "environment" in data


def test_nonexistent_route(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404
