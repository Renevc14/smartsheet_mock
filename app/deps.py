from fastapi import Depends, Query
from .auth import verify_bearer

def auth_dep(ok: bool = Depends(verify_bearer)):
    return True

def paging(page: int = Query(1, ge=1), pageSize: int = Query(100, ge=1, le=500)):
    return {"page": page, "pageSize": pageSize}
