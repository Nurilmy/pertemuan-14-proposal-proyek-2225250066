
def tampilkan_rekap(data_nilai, hasil):
    print("\n==============================================")
    print("             REKAP NILAI SISWA")
    print("==============================================")

    print(f"{'No':<5}{'Nama':<20}{'Nilai':<10}{'Status'}")
    print("----------------------------------------------")

    for nomor, siswa in enumerate(data_nilai, start=1):
        status = (
            "Tuntas"
            if siswa["nilai"] >= hasil["kkm"]
            else "Belum Tuntas"
        )

        print(
            f"{nomor:<5}"
            f"{siswa['nama']:<20}"
            f"{siswa['nilai']:<10.2f}"
            f"{status}"
        )

    print("----------------------------------------------")
    print(f"Jumlah Siswa       : {len(data_nilai)}")
    print(f"Nilai Rata-rata    : {hasil['rata_rata']:.2f}")
    print(f"Nilai Tertinggi    : {hasil['tertinggi']:.2f}")
    print(f"Nilai Terendah     : {hasil['terendah']:.2f}")
    print(f"Siswa Tuntas       : {hasil['tuntas']}")
    print(f"Siswa Belum Tuntas : {hasil['belum_tuntas']}")
    print(f"KKM                : {hasil['kkm']}")
    print("==============================================")


def simpan_laporan(data_nilai, hasil):
    import os

    lokasi_folder = os.path.join(
        os.path.dirname(__file__),
        "..",
        "output"
    )

    os.makedirs(lokasi_folder, exist_ok=True)

    lokasi_file = os.path.join(
        lokasi_folder,
        "laporan_rekap.txt"
    )

    with open(lokasi_file, "w", encoding="utf-8") as file:
        file.write("LAPORAN REKAP NILAI SISWA\n")
        file.write("============================\n")

        for nomor, siswa in enumerate(data_nilai, start=1):
            status = (
                "Tuntas"
                if siswa["nilai"] >= hasil["kkm"]
                else "Belum Tuntas"
            )

            file.write(
                f"{nomor}. {siswa['nama']} - "
                f"{siswa['nilai']} - {status}\n"
            )

        file.write("\nRINGKASAN\n")
        file.write(f"Jumlah siswa: {len(data_nilai)}\n")
        file.write(f"Rata-rata: {hasil['rata_rata']:.2f}\n")
        file.write(f"Nilai tertinggi: {hasil['tertinggi']}\n")
        file.write(f"Nilai terendah: {hasil['terendah']}\n")
        file.write(f"Tuntas: {hasil['tuntas']}\n")
        file.write(f"Belum tuntas: {hasil['belum_tuntas']}\n")

    print(f"\nLaporan berhasil disimpan: {lokasi_file}")
