## Nama Aplikasi
README Generator AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang secara otomatis menghasilkan file README.md yang terstruktur dan profesional untuk proyek perangkat lunak. Pengguna memberikan nama proyek, deskripsi singkat, dan bahasa/teknologi yang digunakan, lalu AI akan membuat template README yang lengkap.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "README Generator AI".
2.  **Form Input Pengguna:**
    *   **Input Nama Proyek:** Sebuah kolom input teks dengan label "Nama Proyek Anda:".
    *   **Input Deskripsi:** Sebuah area teks (textarea) dengan label "Deskripsi Singkat Proyek Anda:".
    *   **Input Teknologi:** Sebuah kolom input teks dengan label "Bahasa/Teknologi Utama (pisahkan dengan koma):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate README.md". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menulis Dokumentasi...".
4.  **Area Output:**
    *   Judul (H3): "Pratinjau README.md Anda:"
    *   Sebuah area konten tunggal untuk menampilkan pratinjau README yang sudah di-render.
    *   **Tombol Salin Markdown:** Harus ada tombol "Salin Kode Markdown" yang akan menyalin teks Markdown mentah ke clipboard, siap untuk di-paste ke GitHub.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI untuk pratinjau. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown menjadi elemen HTML yang diformat dengan benar.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail proyek dan mengklik tombol "Generate README.md".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang developer senior dan kontributor open-source yang ahli dalam membuat dokumentasi proyek yang jelas dan profesional.

    Berdasarkan informasi proyek berikut:
    - Nama Proyek: [Nama dari input pengguna]
    - Deskripsi: [Deskripsi dari input pengguna]
    - Teknologi: [Teknologi dari input pengguna]

    Tugas Anda adalah membuat konten untuk file README.md yang terstruktur dengan baik. Gunakan format Markdown. Template harus mencakup bagian-bagian standar berikut:

    - Judul Proyek (H1)
    - Deskripsi Singkat
    - Fitur Utama (daftar poin)
    - Teknologi yang Digunakan (daftar poin)
    - Cara Instalasi (blok kode placeholder)
    - Cara Penggunaan (blok kode placeholder)
    - Lisensi (placeholder)

    PENTING: Respons Anda HARUS HANYA berisi teks Markdown mentah untuk file README.md dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.pro**.
4.  Setelah menerima respons, aplikasi menyimpan teks Markdown mentah untuk fungsi "Salin".
5.  Aplikasi merender konten Markdown dari respons tersebut menjadi HTML dan menampilkannya di area pratinjau.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Proyek Anda:" dengan:**
    `TaskMaster Pro`
*   **Isi kolom "Deskripsi Singkat Proyek Anda:" dengan:**
    `Sebuah aplikasi to-do list sederhana yang dibangun untuk membantu pengguna mengelola tugas harian mereka dengan lebih efisien.`
*   **Isi kolom "Bahasa/Teknologi Utama (pisahkan dengan koma):" dengan:**
    `React, Node.js, Express, MongoDB`
---