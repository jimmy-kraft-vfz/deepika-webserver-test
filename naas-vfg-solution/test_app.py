# test_app.py
from app import app

def test_root_returns_200():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200

def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
