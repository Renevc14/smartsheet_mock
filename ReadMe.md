# 📄 Smartsheet Mock API (FastAPI)

  

A mock API that simulates part of the official Smartsheet API functionality, built with **FastAPI** for technical practice and local development.

It includes endpoints for managing **Sheets**, **Columns**, **Rows**, **Attachments**, and search, along with a Python client and a set of automated tests using `pytest`.

  

---

  

## 🚀 Features

  

- Basic CRUD operations for **Sheets** and **Rows**

- Text search across all sheets

- Simple **Bearer Token** authentication

- JSON file-based persistence

- Python client (`client/smartsheet_client.py`) for interacting with the API

- Seed script to load sample data

- Unit tests with `pytest` for core endpoints

  

---

  

## ⚙️ Installation

  

1.  **Clone the repository**

```bash

git clone https://github.com/your_username/smartsheet_mock.git

cd smartsheet_mock
```

2.  **Install Dependencies**

```bash
pip install -r requirements.txt
```
  

4.  **Load sample data (seed)**
```bash
python scripts/seed_data.py
```
## Running the API

Start the server with:
```bash
uvicorn app.main:app --reload
```
By default, the API will be available at:

http://localhost:8000/api/2.0

Test token:
```bash
Authorization: Bearer FAKE_TOKEN
```
Example request:
```bash
curl -H "Authorization: Bearer FAKE_TOKEN" http://localhost:8000/api/2.0/sheets
```