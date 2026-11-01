KKM = 60


def hitung_statistik(data_siswa):
    if not data_siswa:
        return None

    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    return {
        "rata_rata": rata_rata,
        "tertinggi": nilai_tertinggi,
        "terendah": nilai_terendah
    }


def tentukan_kelulusan(data_siswa):
    for siswa in data_siswa:
        if siswa["nilai"] >= KKM:
            siswa["status"] = "Lulus"
        else:
            siswa["status"] = "Tidak Lulus"

    return data_siswa