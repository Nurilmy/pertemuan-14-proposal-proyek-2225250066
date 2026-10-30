
# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## 1. Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program sederhana berbasis Python yang dirancang untuk membantu guru mengolah dan menganalisis data nilai siswa.

Program dapat membaca data nilai dari file teks, memvalidasi nilai, menghitung statistik nilai, menentukan ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta menyimpan hasil rekap ke dalam file laporan.

## 2. Tujuan Proyek

1. Mempermudah proses pengolahan data nilai siswa.
2. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
3. Mengetahui jumlah siswa yang tuntas dan belum tuntas.
4. Menerapkan konsep pemrograman Python dalam pengolahan data.
5. Menghasilkan laporan rekap nilai secara otomatis.

## 3. Fitur Program

- Membaca data nilai siswa dari file teks.
- Memvalidasi nilai dalam rentang 0 sampai 100.
- Menghitung nilai rata-rata kelas.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
- Menampilkan hasil analisis nilai.
- Menyimpan laporan hasil rekap ke file teks.

## 4. Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Editor kode: Visual Studio Code
- Version control: Git
- Repository: GitHub

## 5. Struktur Folder

```text
pertemuan-14-proposal-proyek/
|
|-- README.md
|-- proposal.md
|-- .gitignore
|-- data/
|   `-- nilai_contoh.txt
|-- src/
|   |-- main.py
|   |-- data_io.py
|   |-- analisis.py
|   `-- utilitas.py
|-- tests/
|   `-- test_case.md
`-- output/
    `-- .gitkeep
```

## 6. Format Data

Data nilai disimpan dalam file `data/nilai_contoh.txt`.

Setiap baris berisi nama siswa dan nilai yang dipisahkan dengan tanda koma.

Contoh:

```text
Andi,90
Budi,80
Citra,75
Dina,65
Eko,50
```

## 7. Cara Menjalankan Program

1. Buka folder proyek menggunakan Visual Studio Code.
2. Pastikan Python sudah terpasang.
3. Buka terminal pada folder utama proyek.
4. Jalankan perintah berikut:

```bash
python src/main.py
```

5. Program membaca data nilai dari file.
6. Program melakukan validasi dan analisis nilai.
7. Program menampilkan hasil rekap dan menyimpan laporan.

## 8. Contoh Hasil Analisis

Berdasarkan data contoh dengan KKM 75, hasil yang diharapkan adalah:

- Jumlah siswa: 10
- Rata-rata nilai: 71,00
- Nilai tertinggi: 95
- Nilai terendah: 40
- Jumlah siswa tuntas: 6
- Jumlah siswa belum tuntas: 4

## 9. Pengujian Program

Pengujian dilakukan berdasarkan skenario yang terdapat pada file `tests/test_case.md`.

Pengujian meliputi data normal, nilai batas, data tidak valid, file tidak ditemukan, dan ketepatan hasil analisis.

## 10. Pengembang

Nama Tim: [Nama Tim]

Anggota:
1. [Nama Anggota 1]
2. [Nama Anggota 2]
3. [Nama Anggota 3]

## 11. Penutup

Program ini diharapkan dapat membantu proses pengolahan dan analisis nilai matematika siswa secara lebih terstruktur. Proyek ini juga menjadi sarana penerapan konsep pemrograman Python, khususnya file input/output, list, dictionary, fungsi, validasi, dan pengolahan data.
