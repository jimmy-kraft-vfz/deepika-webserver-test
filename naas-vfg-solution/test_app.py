# test_app.py
from app import app
import json

def test_root_returns_200():
    with app.test_client() as client:
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = json.loads(resp.get_data(as_text=True))
    assert data["status"] == "ok"
