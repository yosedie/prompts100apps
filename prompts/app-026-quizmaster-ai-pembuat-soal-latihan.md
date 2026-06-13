## Nama Aplikasi
QuizMaster AI: Pembuat Soal Latihan

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang secara otomatis membuat soal-soal latihan dari sebuah teks atau materi pelajaran. Pengguna menempelkan materi, memilih jenis dan jumlah soal, dan AI akan menghasilkan kuis yang relevan untuk menguji pemahaman.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "QuizMaster AI".
2.  **Form Input Pengguna:**
    *   **Input Materi:** Sebuah area teks (textarea) yang besar dengan label "Tempelkan Teks atau Materi Pelajaran di Sini:".
    *   **Pilihan Tipe Soal:** Sebuah menu dropdown (select) dengan label "Pilih Tipe Soal:" dan opsi: "Pilihan Ganda", "Esai", "Campuran (5 PG, 5 Esai)".
    *   **Input Jumlah Soal:** Sebuah kolom input angka (type="number") dengan label "Jumlah Soal:" dan nilai default 10.
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Soal Latihan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun Soal...".
4.  **Area Output:**
    *   Judul (H3): "Soal Latihan yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh soal.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan materi, memilih tipe dan jumlah soal, lalu mengklik tombol.
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli perancang kurikulum dan pembuat soal ujian yang sangat teliti.

    Berdasarkan materi pelajaran berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah membuat [Jumlah dari input pengguna] soal latihan dengan tipe [Tipe dari pilihan pengguna]. Semua pertanyaan dan jawaban HARUS didasarkan HANYA pada informasi yang ada di dalam teks yang diberikan.

    Gunakan format Markdown yang ketat sebagai berikut:
    - **Untuk Pilihan Ganda:**
      1. Pertanyaan...
         A. Opsi A
         B. Opsi B
         C. Opsi C
         D. Opsi D
      **Jawaban: [Huruf Jawaban]**

    - **Untuk Esai:**
      1. Pertanyaan esai...

    - **Untuk Campuran:** Buat 5 soal Pilihan Ganda terlebih dahulu, diikuti oleh 5 soal Esai.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan soal-soal yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Teks atau Materi Pelajaran di Sini:" dengan:**
    `Fotosintesis adalah proses di mana tumbuhan hijau dan beberapa organisme lain mengubah energi cahaya menjadi energi kimia. Selama fotosintesis, tumbuhan menggunakan energi matahari untuk mengubah karbon dioksida (CO2) dan air (H2O) menjadi glukosa (gula sebagai makanan) dan oksigen (O2) sebagai produk sampingan. Proses ini terjadi di dalam kloroplas dan sangat bergantung pada klorofil, pigmen hijau yang menangkap energi cahaya.`
*   **Atur pilihan "Pilih Tipe Soal:" ke:**
    `Campuran (5 PG, 5 Esai)`
*   **Atur "Jumlah Soal:" ke:**
    `10`
---