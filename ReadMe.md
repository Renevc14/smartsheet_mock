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

## 📂 Project Structure

smartsheet_mock/
├─ app/
│ ├─ main.py
│ ├─ auth.py
│ ├─ deps.py
│ ├─ models.py
│ ├─ storage.py
│ ├─ utils.py
│ └─ routers/
├─ client/
│ └─ smartsheet_client.py
├─ data/
├─ scripts/
│ └─ seed_data.py
├─ tests/
└─ requirements.txt

---

## ⚙️ Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your_username/smartsheet_mock.git
    cd smartsheet_mock
2. **Create Virtual Enviroment**
   ```bash
    python -m venv .venv
#### Activate the environment
Linux/Mac:
    source .venv/bin/activate
    # Windows:
    .venv\Scripts\activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Load sample data (seed)**
    python scripts/seed_data.py