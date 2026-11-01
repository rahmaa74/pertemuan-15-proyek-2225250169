def tampilkan_laporan(data_siswa, statistik):
    if not data_siswa or statistik is None:
        print("Tidak ada data nilai yang dapat dianalisis.")
        return

    print("\n=== LAPORAN NILAI MATEMATIKA ===")

    for siswa in data_siswa:
        print(
            f"{siswa['nis']} - {siswa['nama']} - "
            f"{siswa['nilai']} - {siswa['status']}"
        )

    print("\nRata-rata:", round(statistik["rata_rata"], 2))
    print("Nilai tertinggi:", statistik["tertinggi"])
    print("Nilai terendah:", statistik["terendah"])


def simpan_laporan(data_siswa, statistik, nama_file):
    if not data_siswa or statistik is None:
        return

    with open(nama_file, "w") as file:
        file.write("LAPORAN NILAI MATEMATIKA\n\n")

        for siswa in data_siswa:
            file.write(
                f"{siswa['nis']}, {siswa['nama']}, "
                f"{siswa['nilai']}, {siswa['status']}\n"
            )

        file.write("\nRata-rata: " + str(round(statistik["rata_rata"], 2)))
        file.write("\nNilai tertinggi: " + str(statistik["tertinggi"]))
        file.write("\nNilai terendah: " + str(statistik["terendah"]))

    print("\nLaporan berhasil disimpan.")