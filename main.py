from src.input_data import baca_data
from src.proses import hitung_statistik, tentukan_kelulusan
from src.output import tampilkan_laporan, simpan_laporan


def main():
    nama_file = "data/contoh_data.txt"

    data_siswa = baca_data(nama_file)

    if not data_siswa:
        print("Data siswa kosong atau tidak valid.")
        return

    data_siswa = tentukan_kelulusan(data_siswa)
    statistik = hitung_statistik(data_siswa)

    tampilkan_laporan(data_siswa, statistik)

    simpan_laporan(
        data_siswa,
        statistik,
        "data/laporan_nilai.txt"
    )


if __name__ == "__main__":
    main()