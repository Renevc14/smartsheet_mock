import json
from pathlib import Path
from typing import Dict, List
from .models import Sheet, Row, Column

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

SHEETS_FILE = DATA / "sheets.json"

def _load_json(path: Path, default):
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def _save_json(path: Path, payload):
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

# Sheets

def list_sheets() -> List[Dict]:
    return _load_json(SHEETS_FILE, [])

def save_sheets(sheets: List[Dict]):
    _save_json(SHEETS_FILE, sheets)

# Per-sheet files

def rows_file(sheet_id: int) -> Path:
    return DATA / f"rows_{sheet_id}.json"

def columns_file(sheet_id: int) -> Path:
    return DATA / f"columns_{sheet_id}.json"

def load_rows(sheet_id: int) -> List[Dict]:
    return _load_json(rows_file(sheet_id), [])

def save_rows(sheet_id: int, rows: List[Dict]):
    _save_json(rows_file(sheet_id), rows)

def load_columns(sheet_id: int) -> List[Dict]:
    return _load_json(columns_file(sheet_id), [])

def save_columns(sheet_id: int, cols: List[Dict]):
    _save_json(columns_file(sheet_id), cols)


def next_id(existing: List[int], start: int = 1000) -> int:
    n = max(existing) + 1 if existing else start
    return n