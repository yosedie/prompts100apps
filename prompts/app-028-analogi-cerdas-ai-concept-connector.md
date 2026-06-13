## Nama Aplikasi
Analogi Cerdas AI: Concept Connector

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web kreatif yang membantu pengguna memahami hubungan antara dua konsep yang berbeda dengan menciptakan analogi yang cerdas. Pengguna memasukkan dua konsep, dan AI akan membuat sebuah perumpamaan yang mudah dipahami untuk menjelaskan bagaimana keduanya terhubung.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Analogi Cerdas AI".
2.  **Form Input Pengguna:**
    *   **Input Konsep 1:** Sebuah kolom input teks dengan label "Konsep Pertama:".
    *   **Input Konsep 2:** Sebuah kolom input teks dengan label "Konsep Kedua:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Analogi". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menghubungkan Ide...".
4.  **Area Output:**
    *   Judul (H3): "Analogi yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan analogi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan dua konsep dan mengklik tombol "Buat Analogi".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang guru dan pemikir kreatif yang sangat ahli dalam membuat analogi untuk menjelaskan konsep-konsep yang sulit.

    Berdasarkan dua konsep berikut:
    - Konsep 1: [Teks dari input pengguna 1]
    - Konsep 2: [Teks dari input pengguna 2]

    Tugas Anda adalah menciptakan sebuah analogi yang cerdas dan mudah dipahami untuk menjelaskan hubungan atau kesamaan fungsional antara kedua konsep tersebut.

    Struktur jawaban Anda harus:
    1.  Sajikan analoginya dalam satu kalimat pembuka yang jelas (Contoh: "[Konsep 1] itu seperti [Konsep 2]").
    2.  Jelaskan MENGAPA analogi itu cocok dalam beberapa kalimat berikutnya, dengan menyoroti kesamaan peran atau prosesnya.

    Gunakan format Markdown untuk penekanan jika diperlukan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan analogi yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Konsep Pertama:" dengan:**
    `API (Application Programming Interface)`
*   **Isi kolom "Konsep Kedua:" dengan:**
    `Pelayan di restoran`
---