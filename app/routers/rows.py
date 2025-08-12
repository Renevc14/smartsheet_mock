from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from datetime import datetime
from ..deps import auth_dep
from ..models import AddRowsRequest, UpdateRowRequest
from ..storage import load_rows, save_rows, load_columns

router = APIRouter(prefix="/sheets/{sheet_id}/rows", tags=["Rows"])

@router.post("", status_code=status.HTTP_201_CREATED)
def add_rows(sheet_id: int, body: AddRowsRequest, _: bool = Depends(auth_dep)):
    rows = load_rows(sheet_id)
    cols = load_columns(sheet_id)
    col_ids = {c["id"] for c in cols}

    # validar columnas
    for r in body.rows:
        for cell in r.cells:
            if cell.columnId not in col_ids:
                raise HTTPException(status_code=400, detail=f"Unknown columnId {cell.columnId}")

    # insertar (simple: siempre al final si toBottom)
    for r in body.rows:
        payload = r.model_dump()
        payload["createdAt"] = datetime.utcnow().isoformat()
        payload["modifiedAt"] = payload["createdAt"]
        rows.append(payload)

    save_rows(sheet_id, rows)
    return {"message": "rows added", "inserted": len(body.rows)}

# endpoints de fila individual para update/delete

from fastapi import APIRouter as _AR  # evitar colisión de router
row_router = _AR(prefix="/rows", tags=["Rows (ID)"])

@row_router.put("/{row_id}")
def update_row(row_id: int, body: UpdateRowRequest, _: bool = Depends(auth_dep)):
    # buscar fila en cualquier sheet (simple)
    from ..storage import DATA, rows_file
    for rf in DATA.glob("rows_*.json"):
        rows = load_rows(int(rf.stem.split("_")[1]))
        for r in rows:
            if r["id"] == row_id:
                r["cells"] = [c.model_dump() for c in body.cells]
                r["modifiedAt"] = datetime.utcnow().isoformat()
                save_rows(int(rf.stem.split("_")[1]), rows)
                return {"message": "row updated"}
    raise HTTPException(status_code=404, detail="Row not found")

@row_router.delete("/{row_id}", status_code=204)
def delete_row(row_id: int, _: bool = Depends(auth_dep)):
    from ..storage import DATA, rows_file
    for rf in DATA.glob("rows_*.json"):
        sid = int(rf.stem.split("_")[1])
        rows = load_rows(sid)
        new_rows = [r for r in rows if r["id"] != row_id]
        if len(new_rows) != len(rows):
            save_rows(sid, new_rows)
            return
    raise HTTPException(status_code=404, detail="Row not found")