from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
HEAD = {"Authorization": "Bearer FAKE_TOKEN"}


def test_add_rows_and_search():
    body = {
        "toBottom": True,
        "rows": [
            {"id": 3001, "cells": [
                {"columnId": 1, "value": "Data Pipeline"},
                {"columnId": 2, "value": "carlos@acme.com"},
                {"columnId": 3, "value": "Done"}
            ]}
        ]
    }
    r = client.post("/api/2.0/sheets/1001/rows", headers=HEAD, json=body)
    assert r.status_code == 201

    r2 = client.get("/api/2.0/search", headers=HEAD, params={"query": "Pipeline"})
    assert r2.status_code == 200
    assert r2.json()["total"] >= 1


def test_update_and_delete_row():
    # update row 2001
    r = client.put("/api/2.0/rows/2001", headers=HEAD, json={
        "cells": [
            {"columnId": 1, "value": "Website Redesign (v2)"},
            {"columnId": 2, "value": "ana@acme.com"},
            {"columnId": 3, "value": "In Review"}
        ]
    })
    assert r.status_code == 200

    # delete row 2002
    r2 = client.delete("/api/2.0/rows/2002", headers=HEAD)
    assert r2.status_code == 204