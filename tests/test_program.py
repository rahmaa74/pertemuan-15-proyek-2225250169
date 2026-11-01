import unittest
from src.proses import hitung_statistik, tentukan_kelulusan


class TestProgramNilai(unittest.TestCase):

    def test_hitung_rata_rata(self):
        data = [
            {"nis": "A001", "nama": "Andi", "nilai": 80},
            {"nis": "A002", "nama": "Budi", "nilai": 70},
            {"nis": "A003", "nama": "Citra", "nilai": 90}
        ]

        hasil = hitung_statistik(data)
        self.assertEqual(hasil["rata_rata"], 80)

    def test_nilai_tertinggi(self):
        data = [
            {"nis": "A001", "nama": "Andi", "nilai": 80},
            {"nis": "A002", "nama": "Budi", "nilai": 100}
        ]

        hasil = hitung_statistik(data)
        self.assertEqual(hasil["tertinggi"], 100)

    def test_nilai_terendah(self):
        data = [
            {"nis": "A001", "nama": "Andi", "nilai": 80},
            {"nis": "A002", "nama": "Budi", "nilai": 0}
        ]

        hasil = hitung_statistik(data)
        self.assertEqual(hasil["terendah"], 0)

    def test_kelulusan(self):
        data = [
            {"nis": "A001", "nama": "Andi", "nilai": 80},
            {"nis": "A002", "nama": "Budi", "nilai": 55}
        ]

        hasil = tentukan_kelulusan(data)

        self.assertEqual(hasil[0]["status"], "Lulus")
        self.assertEqual(hasil[1]["status"], "Tidak Lulus")

    def test_data_kosong(self):
        hasil = hitung_statistik([])
        self.assertIsNone(hasil)


if __name__ == "__main__":
    unittest.main()