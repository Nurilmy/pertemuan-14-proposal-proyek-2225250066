
from data_io import input_data
from analisis import hitung_rekap
from utilitas import tampilkan_rekap, simpan_laporan


def main():
    print("====================================")
    print("       PROGRAM REKAP NILAI SISWA")
    print("====================================")

    try:
        data_nilai = input_data()

        if not data_nilai:
            print("Tidak ada data nilai yang valid.")
            return

        while True:
            print("\nMENU PROGRAM")
            print("1. Tampilkan Rekap Nilai")
            print("2. Simpan Laporan")
            print("3. Keluar")

            pilihan = input("Pilih menu (1-3): ")

            if pilihan == "1":
                hasil = hitung_rekap(data_nilai)
                tampilkan_rekap(data_nilai, hasil)

            elif pilihan == "2":
                hasil = hitung_rekap(data_nilai)
                simpan_laporan(data_nilai, hasil)

            elif pilihan == "3":
                print("Terima kasih telah menggunakan program.")
                break

            else:
                print("Pilihan tidak valid!")

    except FileNotFoundError:
        print("File data/nilai_contoh.txt tidak ditemukan.")

    except ValueError as error:
        print("Kesalahan:", error)


if __name__ == "__main__":
    main()
