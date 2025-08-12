from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

# Hoja demo con id 1001
sheets = [
    {"id": 1001, "name": "Demo Projects", "columns": [
        {"id": 1, "title": "Name", "type": "TEXT_NUMBER", "primary": True},
        {"id": 2, "title": "Owner", "type": "CONTACT_LIST", "primary": False},
        {"id": 3, "title": "Status", "type": "PICKLIST", "primary": False}
    ]}
]
(DATA / "sheets.json").write_text(json.dumps(sheets, indent=2))

columns = [
    {"id": 1, "title": "Name", "type": "TEXT_NUMBER", "primary": True},
    {"id": 2, "title": "Owner", "type": "CONTACT_LIST", "primary": False},
    {"id": 3, "title": "Status", "type": "PICKLIST", "primary": False}
]
(DATA / "columns_1001.json").write_text(json.dumps(columns, indent=2))

rows = [
    {"id": 2001, "cells": [
        {"columnId": 1, "value": "Website Redesign"},
        {"columnId": 2, "value": "ana@acme.com"},
        {"columnId": 3, "value": "In Progress"}
    ]},
    {"id": 2002, "cells": [
        {"columnId": 1, "value": "Mobile App"},
        {"columnId": 2, "value": "bob@acme.com"},
        {"columnId": 3, "value": "Pending"}
    ]}
]
(DATA / "rows_1001.json").write_text(json.dumps(rows, indent=2))

print("Seed completed: sheet 1001 with sample columns & rows")