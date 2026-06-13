## Nama Aplikasi
Rencana Belajar AI: Personal Learning Plan Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai perancang kurikulum pribadi. Pengguna memasukkan sebuah topik atau keahlian besar yang ingin dipelajari, dan AI akan membuat rencana belajar mingguan yang terstruktur, logis, dan bertahap dari tingkat dasar hingga mahir.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Rencana Belajar AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Topik Apa yang Ingin Anda Pelajari?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Rencana Belajar". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Merancang Kurikulum...".
4.  **Area Output:**
    *   Judul (H3): "Rencana Belajar Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh rencana.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan topik dan mengklik tombol "Buat Rencana Belajar".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli perancang kurikulum dan tutor berpengalaman yang mampu memecah topik kompleks menjadi langkah-langkah yang mudah dipelajari.

    Berdasarkan topik besar berikut:
    """
    [Topik dari input pengguna]
    """

    Tugas Anda adalah membuat rencana belajar mingguan yang terstruktur dan realistis. Rencana ini harus membawa seseorang dari tingkat pemula absolut hingga memiliki pemahaman yang kuat.

    Strukturkan rencana per minggu (misalnya, Minggu 1, Minggu 2, dst.). Untuk setiap minggu, sertakan:
    - **Fokus Utama:** Tema atau tujuan utama untuk minggu tersebut.
    - **Topik yang Dipelajari:** Daftar poin-poin konsep atau keterampilan spesifik yang harus dipelajari.
    - **Proyek/Latihan Praktis:** Saran tugas kecil atau proyek untuk menerapkan pengetahuan yang baru dipelajari.

    Pastikan urutan topiknya logis, dimulai dari dasar-dasar fundamental sebelum beralih ke konsep yang lebih mahir. Gunakan format Markdown untuk kejelasan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan rencana belajar yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Topik Apa yang Ingin Anda Pelajari?" dengan:**
    `Belajar Python dari Nol`
---