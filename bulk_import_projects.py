import csv
import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Konfigurasi
REDMINE_URL = os.getenv("REDMINE_URL")
API_KEY = os.getenv("API_KEY")

# Endpoint Redmine API
API_URL = f"{REDMINE_URL}/projects.json"
HEADERS = {
    "Content-Type": "application/json",
    "X-Redmine-API-Key": API_KEY
}

def create_project(row):
    payload = {
        "project": {
            "name": row["name"],
            "identifier": row["identifier"],
            "description": row.get("description", ""),
            "is_public": row.get("is_public", "false").lower() == "true"
        }
    }
    response = requests.post(API_URL, json=payload, headers=HEADERS)
    
    if response.status_code == 201:
        print(f"[OK] Project '{row['name']}' berhasil dibuat.")
    else:
        print(f"[FAIL] Project '{row['name']}' gagal dibuat. Status: {response.status_code}, Error: {response.text}")

def bulk_import(csv_file):
    with open(csv_file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            create_project(row)

if __name__ == "__main__":
    bulk_import("projects.csv")
