
def hitung_rekap(data_nilai):
    if not data_nilai:
        raise ValueError("Data nilai kosong.")

    daftar_nilai = [
        siswa["nilai"] for siswa in data_nilai
    ]

    kkm = 75

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    tertinggi = max(daftar_nilai)
    terendah = min(daftar_nilai)

    tuntas = sum(1 for nilai in daftar_nilai if nilai >= kkm)
    belum_tuntas = len(daftar_nilai) - tuntas

    return {
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "tuntas": tuntas,
        "belum_tuntas": belum_tuntas,
        "kkm": kkm
    }
