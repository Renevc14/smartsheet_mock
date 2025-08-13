from pathlib import Path
import json

# Define the base directory for saving data
BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

# Create the sheet with the specified columns
sheet = {
    "id": 1001,
    "name": "Mock API Smartsheet",
    "columns": [
        {"id": 1, "title": "Task ID", "type": "TEXT_NUMBER", "primary": True},
        {"id": 2, "title": "Task Name", "type": "TEXT_NUMBER", "primary": False},
        {"id": 3, "title": "Assignee", "type": "CONTACT_LIST", "primary": False},
        {"id": 4, "title": "Status", "type": "PICKLIST", "primary": False},
        {"id": 5, "title": "Priority", "type": "PICKLIST", "primary": False},
        {"id": 6, "title": "Start Date", "type": "DATE", "primary": False},
        {"id": 7, "title": "Due Date", "type": "DATE", "primary": False},
        {"id": 8, "title": "Notes", "type": "TEXT_NUMBER", "primary": False}
    ]
}

# Save the sheet data to the sheets.json file
sheets_file = DATA / "sheets.json"
sheets = [sheet]
sheets_file.write_text(json.dumps(sheets, indent=2))

# Create columns for the sheet (this is to persist columns separately)
columns = sheet["columns"]
columns_file = DATA / "columns_1001.json"
columns_file.write_text(json.dumps(columns, indent=2))

# Create the rows (tasks) for the sheet
rows = [
    {
        "id": 2,
        "cells": [
            {"columnId": 1, "value": "2"},
            {"columnId": 2, "value": "Design the API structure"},
            {"columnId": 3, "value": "Ana"},
            {"columnId": 4, "value": "In Progress"},
            {"columnId": 5, "value": "High"},
            {"columnId": 6, "value": "2025-08-02"},
            {"columnId": 7, "value": "2025-08-07"},
            {"columnId": 8, "value": "Design the basic structure of the API, including endpoints and parameters."}
        ]
    },
    {
        "id": 3,
        "cells": [
            {"columnId": 1, "value": "3"},
            {"columnId": 2, "value": "Implement authentication in the API"},
            {"columnId": 3, "value": "Carlos"},
            {"columnId": 4, "value": "Pending"},
            {"columnId": 5, "value": "High"},
            {"columnId": 6, "value": "2025-08-08"},
            {"columnId": 7, "value": "2025-08-14"},
            {"columnId": 8, "value": "Implement token-based authentication (JWT) for the API."}
        ]
    },
    {
        "id": 4,
        "cells": [
            {"columnId": 1, "value": "4"},
            {"columnId": 2, "value": "Create endpoints for user management"},
            {"columnId": 3, "value": "Juan"},
            {"columnId": 4, "value": "Not Started"},
            {"columnId": 5, "value": "Medium"},
            {"columnId": 6, "value": "2025-08-10"},
            {"columnId": 7, "value": "2025-08-20"},
            {"columnId": 8, "value": "Develop endpoints for adding, editing, and deleting users."}
        ]
    },
    {
        "id": 5,
        "cells": [
            {"columnId": 1, "value": "5"},
            {"columnId": 2, "value": "Write API documentation"},
            {"columnId": 3, "value": "Laura"},
            {"columnId": 4, "value": "Pending"},
            {"columnId": 5, "value": "Medium"},
            {"columnId": 6, "value": "2025-08-12"},
            {"columnId": 7, "value": "2025-08-15"},
            {"columnId": 8, "value": "Create detailed documentation for the API, including usage examples."}
        ]
    },
    {
        "id": 6,
        "cells": [
            {"columnId": 1, "value": "6"},
            {"columnId": 2, "value": "Perform unit tests for the API"},
            {"columnId": 3, "value": "Pedro"},
            {"columnId": 4, "value": "Not Started"},
            {"columnId": 5, "value": "High"},
            {"columnId": 6, "value": "2025-08-16"},
            {"columnId": 7, "value": "2025-08-22"},
            {"columnId": 8, "value": "Write and execute unit tests to ensure the functionality of the endpoints."}
        ]
    }
]

# Save the rows data to the rows_1001.json file
rows_file = DATA / "rows_1001.json"
rows_file.write_text(json.dumps(rows, indent=2))

print("Seed completed: sheet 1001 with sample columns & rows")
