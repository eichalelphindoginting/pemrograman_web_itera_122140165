# Aplikasi API Manajemen Matakuliah

Aplikasi ini adalah API sederhana berbasis Pyramid untuk mengelola data matakuliah. Aplikasi ini menyediakan fitur CRUD (Create, Read, Update, Delete) yang dapat diakses melalui HTTP request menggunakan `curl` atau Postman.

## Fitur

- Menampilkan seluruh data matakuliah (GET)
- Menampilkan data matakuliah berdasarkan ID (GET)
- Menambahkan matakuliah baru (POST)
- Memperbarui matakuliah (PUT)
- Menghapus matakuliah (DELETE)

## Model `Matakuliah`

```python
from sqlalchemy import Column, Integer, Text
from .meta import Base

class MataKuliah(Base):
    __tablename__ = 'matakuliah'
    id = Column(Integer, primary_key=True)
    kode_mk = Column(Text, unique=True, nullable=False)
    nama_mk = Column(Text, nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'kode_mk': self.kode_mk,
            'nama_mk': self.nama_mk,
            'sks': self.sks,
            'semester': self.semester,
        }
1. Clone project
bash
Copy
Edit
git clone <URL_PROJECT_ANDA>
cd pyramid_matakuliah
2. Aktifkan virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # untuk Windows
3. Install dependencies
bash
Copy
Edit
pip install -e .
pip install alembic
4. Inisialisasi database
bash
Copy
Edit
initialize_pyramid_matakuliah_db development.ini
5. Jalankan server
bash
Copy
Edit
pserve development.ini --reload

Contoh CURL Request
POST - Tambah Matakuliah
bash
Copy
Edit
curl -X POST http://localhost:6543/api/matakuliah \
-H "Content-Type: application/json" \
-d '{
  "kode_mk": "IF1234",
  "nama_mk": "Struktur Data",
  "sks": 3,
  "semester": 3
}'
GET - Ambil Semua Matakuliah
bash
Copy
Edit
curl http://localhost:6543/api/matakuliah
GET - Ambil Matakuliah Berdasarkan ID
bash
Copy
Edit
curl http://localhost:6543/api/matakuliah/1
PUT - Update Matakuliah Berdasarkan ID
bash
Copy
Edit
curl -X PUT http://localhost:6543/api/matakuliah/1 \
-H "Content-Type: application/json" \
-d '{
  "kode_mk": "IF1234",
  "nama_mk": "Struktur Data Lanjut",
  "sks": 4,
  "semester": 4
}'
DELETE - Hapus Matakuliah Berdasarkan ID
bash
Copy
Edit
curl -X DELETE http://localhost:6543/api/matakuliah/1

Aplikasi ini dibuat sebagai tugas praktikum Pemrograman Web.
Dibuat oleh: Eichal Elphindo Ginting - 122140165