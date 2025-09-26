# test_app.py
from app import app
import json

def test_root_returns_200():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello DevOps NaaS" in resp.data

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = json.loads(resp.get_data(as_text=True))
    assert data["status"] == "ok"
