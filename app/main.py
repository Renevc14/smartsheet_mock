from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import sheets, columns, rows, attachments, search
from .routers.rows import row_router

app = FastAPI(title="Smartsheet Mock API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api = FastAPI()
api.include_router(sheets.router)
api.include_router(columns.router)
api.include_router(rows.router)
api.include_router(row_router)
api.include_router(attachments.router)
api.include_router(search.router)

app.mount("/api/2.0", api)
