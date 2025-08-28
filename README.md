# Redmine Bulk Import Projects

Script Python untuk melakukan bulk insert project ke Redmine menggunakan REST API.
Berisi langkah-langkah setup API, konfigurasi script, isi CSV, dan eksekusi script.

## Setup REST API & API Key (Step 1-3)
1. Login ke Redmine sebagai admin.
2. Masuk ke `Administration -> Settings -> Authentication` dan centang `Enable REST web service`, lalu Save.
3. Login sebagai user biasa, masuk ke `My account -> API access key` dan copy API key.

## Persiapan CSV dan Script
- Buat file `projects.csv` dengan format berikut:
```
name,identifier,description,is_public
Project A,project-a,First test project,true
Project B,project-b,Second test project,false
Project C,project-c,Another project,true
```
- Pastikan field `identifier` unik, huruf kecil, angka, dash atau underscore.
- Bisa juga menggunakan `.env` untuk menyimpan `REDMINE_URL` dan `API_KEY` agar lebih aman.

## Cara Menjalankan Script
1. Masuk ke folder repository:
```
cd redmine-bulk-import
```
2. Install dependency Python:
```
pip install requests python-dotenv
```
3. Jalankan script:
```
python3 bulk_import_projects.py
```
4. Cek output di terminal:
```
[OK] Project 'Project A' berhasil dibuat.
[FAIL] Project 'Project B' gagal dibuat. Status: 422, Error: {"errors":["Identifier has already been taken"]}
```
