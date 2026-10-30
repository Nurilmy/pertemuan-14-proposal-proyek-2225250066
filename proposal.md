
# PROPOSAL PROYEK
# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas Berbasis Python.

## 2. Latar Belakang

Dalam kegiatan pembelajaran, guru perlu mengolah nilai siswa untuk mengetahui hasil belajar dan tingkat ketuntasan kelas. Pengolahan nilai secara manual membutuhkan waktu dan berpotensi menimbulkan kesalahan dalam perhitungan.

Permasalahan tersebut dapat dibantu dengan menggunakan program sederhana berbasis Python. Program dirancang untuk membaca data nilai siswa dari file, memvalidasi data, menghitung statistik nilai, menentukan ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), dan menyimpan hasil analisis dalam bentuk laporan teks.

Dengan adanya program ini, proses rekapitulasi nilai diharapkan menjadi lebih mudah, cepat, dan terstruktur.

## 3. Pengguna dan Tujuan

### A. Pengguna

Pengguna utama program adalah:
1. Guru mata pelajaran matematika.
2. Mahasiswa Pendidikan Matematika.
3. Pengguna yang membutuhkan pengolahan data nilai siswa.

### B. Tujuan

1. Membantu guru melakukan rekapitulasi nilai siswa.
2. Menghitung rata-rata, nilai minimum, dan maksimum.
3. Mengetahui jumlah siswa yang tuntas dan belum tuntas.
4. Memvalidasi data nilai agar berada dalam rentang 0–100.
5. Menghasilkan laporan rekap nilai secara otomatis.

## 4. Ruang Lingkup

### A. Fitur Wajib

1. Membaca data nilai siswa dari file teks.
2. Memvalidasi nama dan nilai siswa.
3. Memastikan nilai berada dalam rentang 0–100.
4. Menghitung rata-rata nilai kelas.
5. Menentukan nilai tertinggi dan terendah.
6. Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
7. Menampilkan hasil analisis.
8. Menyimpan laporan ke file teks.

### B. Batasan Proyek

1. Program menggunakan bahasa Python.
2. Program dijalankan melalui terminal atau console.
3. Data siswa disimpan dalam file teks.
4. Nilai siswa berada dalam rentang 0–100.
5. KKM awal ditetapkan sebesar 75.
6. Program tidak menggunakan database.
7. Program tidak menggunakan tampilan grafis (GUI).

## 5. Kebutuhan Program

### A. Kebutuhan Fungsional

1. Program dapat membaca data dari file `nilai_contoh.txt`.
2. Program dapat memeriksa kelengkapan data siswa.
3. Program dapat menolak nilai di luar rentang 0–100.
4. Program dapat menghitung rata-rata nilai.
5. Program dapat menentukan nilai tertinggi dan terendah.
6. Program dapat menghitung jumlah siswa tuntas dan belum tuntas.
7. Program dapat menampilkan hasil rekapitulasi.
8. Program dapat menyimpan hasil rekap ke file laporan.

### B. Kebutuhan Nonfungsional

1. Program menggunakan Python.
2. Program dapat dijalankan melalui Visual Studio Code.
3. Program memiliki struktur kode modular.
4. Program mudah digunakan dan dipahami.
5. Program memiliki dokumentasi dan test case.
6. Program dapat menangani kesalahan pembacaan file dan input data.

## 6. Analisis IPO (Input, Process, Output)

| Komponen | Keterangan |
|---|---|
| Input | File teks berisi nama siswa dan nilai, serta nilai KKM. |
| Process | Membaca data, memvalidasi nilai, menghitung rata-rata, minimum, maksimum, dan ketuntasan siswa. |
| Output | Daftar rekap nilai, statistik kelas, jumlah siswa tuntas dan belum tuntas, serta laporan teks. |

### Rumus Perhitungan

**1. Rata-rata Nilai**

Rata-rata = Jumlah seluruh nilai / Banyak siswa

**2. Nilai Tertinggi**

Nilai tertinggi = Maksimum dari seluruh nilai.

**3. Nilai Terendah**

Nilai terendah = Minimum dari seluruh nilai.

**4. Ketuntasan**

- Tuntas: nilai >= KKM.
- Belum tuntas: nilai < KKM.

KKM yang digunakan dalam rancangan ini adalah 75.

## 7. Algoritma dan Pseudocode

### A. Algoritma Program

1. Mulai program.
2. Tentukan lokasi file data nilai.
3. Baca data nilai siswa dari file.
4. Periksa apakah file tersedia.
5. Validasi nama dan nilai setiap siswa.
6. Pastikan nilai berada dalam rentang 0–100.
7. Jika data valid, kumpulkan nilai siswa.
8. Hitung rata-rata nilai kelas.
9. Tentukan nilai tertinggi dan terendah.
10. Hitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
11. Tampilkan hasil rekapitulasi.
12. Simpan laporan ke file teks.
13. Selesai.

### B. Pseudocode

```text
MULAI

Tentukan lokasi file data nilai
Tentukan KKM = 75

Baca data dari file

JIKA file tidak ditemukan:
    Tampilkan pesan kesalahan
    SELESAI

Validasi setiap data siswa

JIKA data tidak valid:
    Tampilkan informasi kesalahan
    Abaikan data yang tidak valid

JIKA tidak ada data valid:
    Tampilkan pesan bahwa data kosong
    SELESAI

Hitung jumlah seluruh nilai
Hitung rata-rata nilai
Cari nilai tertinggi
Cari nilai terendah

Hitung jumlah siswa tuntas
Hitung jumlah siswa belum tuntas

Tampilkan hasil rekapitulasi

Simpan laporan ke file teks

SELESAI
```

## 8. Struktur Program

Program dibagi menjadi beberapa modul berdasarkan tanggung jawabnya.

| File | Fungsi |
|---|---|
| main.py | Mengatur alur utama program. |
| data_io.py | Membaca data dari file dan melakukan validasi. |
| analisis.py | Menghitung statistik dan ketuntasan nilai. |
| utilitas.py | Menampilkan dan menyimpan laporan. |
| nilai_contoh.txt | Menyimpan data contoh nilai siswa. |
| test_case.md | Menyimpan skenario pengujian program. |

### Rancangan Struktur Folder

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

## 9. Struktur Data

Struktur data yang digunakan dalam program adalah:

### A. List

List digunakan untuk menyimpan kumpulan data nilai siswa.

Contoh:

```python
daftar_nilai = [90, 80, 75, 65, 50]
```

### B. Dictionary

Dictionary digunakan untuk menyimpan identitas dan nilai setiap siswa.

Contoh:

```python
data_siswa = {
    "nama": "Andi",
    "nilai": 90
}
```

### C. File

File teks digunakan untuk menyimpan data awal siswa dan laporan hasil analisis.

Struktur data tersebut dipilih agar pengolahan data nilai dapat dilakukan secara terorganisasi.

## 10. Rancangan Test Case

Pengujian dirancang untuk mencakup kondisi normal, batas, dan tidak valid.

| No. | Skenario | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Membaca data normal | Andi,90 | Data berhasil dibaca. |
| TC02 | Nilai batas minimum | Siswa,0 | Nilai diterima. |
| TC03 | Nilai batas maksimum | Siswa,100 | Nilai diterima. |
| TC04 | Nilai melebihi batas | Siswa,110 | Data ditolak. |
| TC05 | Nilai negatif | Siswa,-5 | Data ditolak. |
| TC06 | Format data salah | Andi tanpa nilai | Data ditandai tidak valid. |
| TC07 | File tidak ditemukan | File tidak tersedia | Program menampilkan pesan kesalahan. |
| TC08 | Perhitungan statistik | 90,80,70,60 | Rata-rata 75, maksimum 90, minimum 60. |
| TC09 | Perhitungan ketuntasan | Nilai 90,80,70,60; KKM 75 | 2 siswa tuntas dan 2 belum tuntas. |
| TC10 | Penyimpanan laporan | Data valid | Laporan berhasil dibuat. |

Dokumentasi pengujian lebih lanjut disimpan pada `tests/test_case.md`.

## 11. Pembagian Tugas

| No. | Peran | Tanggung Jawab | PIC |
|---|---|---|---|
| 1 | Koordinator | Mengatur ruang lingkup dan integrasi proyek. | [Nama] |
| 2 | Programmer Data I/O | Membuat fungsi membaca dan memvalidasi file. | [Nama] |
| 3 | Programmer Logika | Membuat fungsi statistik dan ketuntasan. | [Nama] |
| 4 | Tester/QA | Menyusun dan melakukan pengujian. | [Nama] |
| 5 | Dokumentasi | Menyusun README dan dokumentasi proyek. | [Nama] |

Catatan: Jika jumlah anggota kelompok lebih sedikit, satu anggota dapat memegang lebih dari satu peran.

## 12. Jadwal Pelaksanaan

| Tahapan | Kegiatan | Target |
|---|---|---|
| Pertemuan 14 | Perancangan proyek | Proposal, struktur folder, pseudocode, dan test case. |
| Antara P14–P15 | Implementasi awal | Pembuatan modul dan fitur wajib. |
| Pertemuan 15 | Integrasi dan pengujian | Testing, debugging, dan dokumentasi. |
| Pertemuan 16 | Presentasi dan evaluasi | Demonstrasi program dan evaluasi proyek. |

## 13. Repository GitHub

Nama repository:

`proyek-akhir-nama-tim`

URL Repository:

[Masukkan URL GitHub Kelompok]

Repository GitHub digunakan untuk menyimpan kode program, dokumentasi, dan riwayat perubahan proyek. Setiap anggota kelompok dapat berkontribusi sesuai pembagian tugas.

## PENUTUP

Program Rekap dan Analisis Nilai Matematika Kelas dirancang sebagai solusi sederhana untuk membantu proses pengolahan nilai siswa.

Melalui proyek ini, konsep pemrograman Python seperti list, dictionary, fungsi, percabangan, perulangan, serta file input/output dapat diterapkan dalam permasalahan nyata di bidang pendidikan.

Proposal ini menjadi pedoman implementasi, pengujian, dan pengembangan program pada pertemuan berikutnya.
