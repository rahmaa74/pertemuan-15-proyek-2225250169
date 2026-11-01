def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                bagian = baris.strip().split(",")

                if len(bagian) != 3:
                    continue

                nis, nama, nilai = bagian

                try:
                    nilai = float(nilai)

                    if 0 <= nilai <= 100:
                        data_siswa.append({
                            "nis": nis,
                            "nama": nama,
                            "nilai": nilai
                        })
                except ValueError:
                    continue

    except FileNotFoundError:
        print("File tidak ditemukan.")

    return data_siswa