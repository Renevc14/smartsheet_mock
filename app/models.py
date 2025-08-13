from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime

class Column(BaseModel):
    id: int
    title: str
    type: str = "TEXT_NUMBER"
    primary: bool = False

class Cell(BaseModel):
    columnId: int
    value: Optional[Any] = None

class Row(BaseModel):
    id: int
    cells: List[Cell] = Field(default_factory=list)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    modifiedAt: datetime = Field(default_factory=datetime.utcnow)

class Sheet(BaseModel):
    id: int
    name: str
    columns: List[Column] = Field(default_factory=list)
    createdAt: datetime = Field(default_factory=datetime.utcnow)

class CreateSheetRequest(BaseModel):
    name: str
    columns: List[Column]

class AddRowsRequest(BaseModel):
    toBottom: bool = True
    rows: List[Row]

class UpdateRowRequest(BaseModel):
    cells: List[Cell]

class SearchResult(BaseModel):
    sheetId: int
    rowId: int
    columnId: int
    value: Any
