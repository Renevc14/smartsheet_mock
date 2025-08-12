from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..deps import auth_dep
from ..models import Column
from ..storage import load_columns, save_columns

router = APIRouter(prefix="/sheets/{sheet_id}/columns", tags=["Columns"])

@router.get("")
def list_columns(sheet_id: int, _: bool = Depends(auth_dep)):
    return load_columns(sheet_id)

@router.post("")
def add_columns(sheet_id: int, cols: List[Column], _: bool = Depends(auth_dep)):
    existing = load_columns(sheet_id)
    existing_ids = [c["id"] for c in existing]
    # evitar colisiones simples
    for c in cols:
        if c.id in existing_ids:
            raise HTTPException(status_code=400, detail=f"Column id {c.id} already exists")
    new_cols = existing + [c.model_dump() for c in cols]
    save_columns(sheet_id, new_cols)
    return new_cols