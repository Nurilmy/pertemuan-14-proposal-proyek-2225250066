

import os


def input_data():
    lokasi_file = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "nilai_contoh.txt"
    )

    daftar_siswa = []

    with open(lokasi_file, "r", encoding="utf-8") as file:
        for baris in file:
            bagian = baris.strip().split(",")

            if len(bagian) != 2:
                continue

            nama = bagian[0].strip()

            try:
                nilai = float(bagian[1])

                if nama and 0 <= nilai <= 100:
                    daftar_siswa.append({
                        "nama": nama,
                        "nilai": nilai
                    })

            except ValueError:
                continue

    return daftar_siswa
