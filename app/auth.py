from fastapi import Header, HTTPException, status
from typing import Optional

EXPECTED_TOKEN = "FAKE_TOKEN"

async def verify_bearer(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Bearer token")
    token = authorization.split(" ", 1)[1]
    if token != EXPECTED_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return True