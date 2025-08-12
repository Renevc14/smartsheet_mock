from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict
from ..deps import auth_dep, paging
from ..models import CreateSheetRequest, Sheet, Column
from ..storage import list_sheets, save_sheets, load_columns, save_columns, load_rows, save_rows, next_id
from ..utils import paginate

router = APIRouter(prefix="/sheets", tags=["Sheets"])

@router.get("")
def list_all(_: bool = Depends(auth_dep), pg=Depends(paging)):
    sheets = list_sheets()
    return paginate(sheets, pg["page"], pg["pageSize"])

@router.post("", status_code=status.HTTP_201_CREATED)
def create_sheet(payload: CreateSheetRequest, _: bool = Depends(auth_dep)):
    sheets = list_sheets()
    new_id = next_id([s["id"] for s in sheets], start=1001)
    sheet = {
        "id": new_id,
        "name": payload.name,
        "columns": [c.model_dump() for c in payload.columns],
    }
    sheets.append(sheet)
    save_sheets(sheets)
    save_columns(new_id, sheet["columns"])  
    save_rows(new_id, [])            
    return sheet

@router.get("/{sheet_id}")
def get_sheet(sheet_id: int, _: bool = Depends(auth_dep)):
    sheets = list_sheets()
    found = next((s for s in sheets if s["id"] == sheet_id), None)
    if not found:
        raise HTTPException(status_code=404, detail="Sheet not found")
    cols = load_columns(sheet_id)
    rows = load_rows(sheet_id)
    return {**found, "columns": cols, "rows": rows}

@router.delete("/{sheet_id}", status_code=204)
def delete_sheet(sheet_id: int, _: bool = Depends(auth_dep)):
    sheets = list_sheets()
    before = len(sheets)
    sheets = [s for s in sheets if s["id"] != sheet_id]
    if len(sheets) == before:
        raise HTTPException(status_code=404, detail="Sheet not found")
    save_sheets(sheets)
    return