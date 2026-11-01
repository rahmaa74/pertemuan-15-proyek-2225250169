# Catatan Perbaikan Bug

| ID | Gejala | Penyebab | Perbaikan | Status |
|---|---|---|---|---|
| BUG01 | Program gagal membaca file yang tidak ditemukan | File tidak tersedia pada lokasi yang ditentukan | Menambahkan penanganan FileNotFoundError | Diperbaiki |
| BUG02 | Nilai di luar rentang tidak diproses | Nilai harus berada pada rentang 0–100 | Menambahkan validasi nilai | Diperbaiki |