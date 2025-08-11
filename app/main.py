from fastapi import FastAPI
from app.routers import sheet_router, row_router, column_router

app = FastAPI()

# Incluir los routers
app.include_router(sheet_router.router, prefix="/sheets", tags=["Sheets"])
app.include_router(row_router.router, prefix="/rows", tags=["Rows"])
app.include_router(column_router.router, prefix="/columns", tags=["Columns"])

@app.get("/")
async def root():
    return {"message": "Welcome to the mock Smartsheet API"}
