from fastapi import APIRouter, Depends, Query
from typing import List
from ..deps import auth_dep
from ..models import SearchResult
from ..storage import DATA, load_rows, load_columns

router = APIRouter(prefix="/search", tags=["Search"]) 

@router.get("")
def search(query: str = Query(..., min_length=1), _: bool = Depends(auth_dep)):
    results: List[SearchResult] = []
    for rf in DATA.glob("rows_*.json"):
        sid = int(rf.stem.split("_")[1])
        rows = load_rows(sid)
        cols = {c["id"]: c for c in load_columns(sid)}
        for r in rows:
            for cell in r.get("cells", []):
                val = cell.get("value")
                if val is not None and query.lower() in str(val).lower():
                    results.append({
                        "sheetId": sid,
                        "rowId": r["id"],
                        "columnId": cell["columnId"],
                        "value": val,
                    })
    return {"query": query, "total": len(results), "results": results[:200]}