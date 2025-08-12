from fastapi import APIRouter, Depends
from ..deps import auth_dep

router = APIRouter(prefix="/sheets/{sheet_id}/rows/{row_id}/attachments", tags=["Attachments"]) 

@router.get("")
def list_attachments(sheet_id: int, row_id: int, _: bool = Depends(auth_dep)):
    # demo: no persistimos; devolvemos simulado
    return [{"id": 1, "name": "link", "url": "https://example.com"}]

@router.post("")
def add_attachment(sheet_id: int, row_id: int, _: bool = Depends(auth_dep)):
    return {"id": 2, "message": "attachment created (mock)"}