import httpx
from typing import Dict, List, Optional

class SmartsheetClient:
    def __init__(self, base_url: str = "http://localhost:8000/api/2.0", token: str = "FAKE_TOKEN"):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {token}"}
        self._http = httpx.Client(timeout=10)

    def list_sheets(self, page: int = 1, pageSize: int = 100) -> Dict:
        r = self._http.get(f"{self.base_url}/sheets", headers=self.headers, params={"page": page, "pageSize": pageSize})
        r.raise_for_status()
        return r.json()

    def create_sheet(self, name: str, columns: List[Dict]) -> Dict:
        body = {"name": name, "columns": columns}
        r = self._http.post(f"{self.base_url}/sheets", headers=self.headers, json=body)
        r.raise_for_status()
        return r.json()

    def get_sheet(self, sheet_id: int) -> Dict:
        r = self._http.get(f"{self.base_url}/sheets/{sheet_id}", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def add_rows(self, sheet_id: int, rows: List[Dict], toBottom: bool = True) -> Dict:
        body = {"toBottom": toBottom, "rows": rows}
        r = self._http.post(f"{self.base_url}/sheets/{sheet_id}/rows", headers=self.headers, json=body)
        r.raise_for_status()
        return r.json()

    def update_row(self, row_id: int, cells: List[Dict]) -> Dict:
        body = {"cells": cells}
        r = self._http.put(f"{self.base_url}/rows/{row_id}", headers=self.headers, json=body)
        r.raise_for_status()
        return r.json()

    def delete_row(self, row_id: int) -> None:
        r = self._http.delete(f"{self.base_url}/rows/{row_id}", headers=self.headers)
        r.raise_for_status()
        return None

    def search(self, query: str) -> Dict:
        r = self._http.get(f"{self.base_url}/search", headers=self.headers, params={"query": query})
        r.raise_for_status()
        return r.json()
