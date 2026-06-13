## Nama Aplikasi
Trivia Forge AI: Custom Trivia Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pembuat kuis trivia kustom. Pengguna memasukkan topik yang sangat spesifik, memilih jumlah pertanyaan dan tingkat kesulitan, lalu AI akan menghasilkan satu set pertanyaan trivia yang menantang, lengkap dengan jawabannya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Trivia Forge AI".
2.  **Form Input Pengguna:**
    *   **Input Topik:** Sebuah kolom input teks dengan label "Masukkan Topik Trivia Spesifik Anda:".
    *   **Input Jumlah Pertanyaan:** Sebuah kolom input angka (type="number") dengan label "Jumlah Pertanyaan:" dan nilai default 10.
    *   **Pilihan Tingkat Kesulitan:** Sebuah menu dropdown (select) dengan label "Tingkat Kesulitan:" dan opsi: "Mudah", "Sedang", "Sulit".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Pertanyaan Trivia!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Fakta...".
4.  **Area Output:**
    *   Judul (H3): "Set Trivia Kustom Anda:"
    *   Sebuah area konten tunggal untuk menampilkan daftar pertanyaan dan jawaban.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail trivia dan mengklik tombol "Buat Pertanyaan Trivia!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang 'Quizmaster' dan peneliti yang ahli dalam menemukan fakta-fakta menarik dan obskur tentang berbagai topik.

    Berdasarkan kriteria berikut:
    - Topik: [Topik dari input pengguna]
    - Jumlah Pertanyaan: [Jumlah dari input pengguna]
    - Tingkat Kesulitan: [Tingkat kesulitan dari pilihan pengguna]

    Tugas Anda adalah membuat satu set pertanyaan trivia.
    - Pertanyaan harus sesuai dengan tingkat kesulitan yang diminta.
    - Untuk setiap pertanyaan, berikan jawabannya.

    Gunakan format Markdown yang ketat sebagai berikut:
    1.  **Pertanyaan:** [Teks pertanyaan Anda]?
        **Jawaban:** [Teks jawaban Anda].
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan set trivia yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Topik Trivia Spesifik Anda:" dengan:**
    `Sejarah dan karakter dalam film The Lord of the Rings`
*   **Atur "Jumlah Pertanyaan:" ke:**
    `10`
*   **Atur pilihan "Tingkat Kesulitan:" ke:**
    `Sedang`
---