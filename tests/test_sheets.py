from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
HEAD = {"Authorization": "Bearer FAKE_TOKEN"}

def test_list_sheets_unauthorized():
    r = client.get("/api/2.0/sheets")
    assert r.status_code == 401

def test_list_sheets_ok():
    r = client.get("/api/2.0/sheets", headers=HEAD)
    assert r.status_code == 200
    body = r.json()
    assert "data" in body


def test_create_and_get_sheet():
    new_sh = {
        "name": "My Tasks",
        "columns": [
            {"id": 11, "title": "Task", "type": "TEXT_NUMBER", "primary": True},
            {"id": 12, "title": "Assignee", "type": "CONTACT_LIST", "primary": False},
        ],
    }
    r = client.post("/api/2.0/sheets", headers=HEAD, json=new_sh)
    assert r.status_code == 201
    sh = r.json()

    r2 = client.get(f"/api/2.0/sheets/{sh['id']}", headers=HEAD)
    assert r2.status_code == 200
    assert r2.json()["name"] == "My Tasks"
