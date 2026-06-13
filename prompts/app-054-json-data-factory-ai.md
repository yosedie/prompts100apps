## Nama Aplikasi
JSON Data Factory AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai generator data sampel (dummy data) dalam format JSON. Pengguna mendeskripsikan skema data yang mereka butuhkan dalam bahasa biasa, dan AI akan menghasilkan array objek JSON yang sesuai, sangat berguna untuk prototyping dan pengujian.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "JSON Data Factory AI".
2.  **Form Input Pengguna:**
    *   **Input Deskripsi Skema:** Sebuah area teks (textarea) yang besar dengan label "Jelaskan Skema Data yang Anda Butuhkan:".
    *   **Input Jumlah Objek:** Sebuah kolom input angka (type="number") dengan label "Jumlah Objek Data yang Diinginkan:" dan nilai default 5.
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate JSON Data". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Generating...".
4.  **Area Output (Blok Kode):**
    *   Judul (H3): "Data JSON yang Dihasilkan:"
    *   Sebuah **kontainer blok kode** khusus (seperti `<pre><code>...</code></pre>`) untuk menampilkan data JSON. Kontainer ini harus memiliki latar belakang gelap dan menggunakan font monospace.
    *   **Tombol Salin Kode (Copy Code):** Di sudut kanan atas kontainer blok kode, **wajib** ada tombol "Copy" yang memungkinkan pengguna menyalin seluruh data JSON ke clipboard dengan satu klik.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Blok Kode dengan Syntax Highlighting:** Aplikasi **wajib** menggunakan library JavaScript seperti `highlight.js` atau `prism.js` untuk merender respons dari AI. Library ini akan secara otomatis mendeteksi format JSON dari Markdown fence (```json) dan memberikan pewarnaan sintaks yang sesuai di dalam kontainer blok kode.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi skema, jumlah objek, dan mengklik tombol "Generate JSON Data".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah sebuah API data generator. Tugas Anda adalah membuat data sampel dalam format JSON berdasarkan deskripsi skema dari pengguna.

    Berdasarkan permintaan berikut:
    - Deskripsi Skema: """[Teks dari input pengguna]"""
    - Jumlah Objek: [Jumlah dari input pengguna]

    Buat sebuah array JSON yang berisi [Jumlah dari input pengguna] objek. Setiap objek harus sesuai dengan skema yang dideskripsikan. Gunakan data acak yang realistis (nama, email, tanggal, dll.).

    PENTING: Respons Anda HARUS HANYA berisi blok kode JSON mentah yang valid dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons (yang hanya berisi blok kode JSON), aplikasi menggunakan library syntax highlighting untuk merendernya menjadi blok kode yang diformat dengan indah di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Skema Data yang Anda Butuhkan:" dengan:**
    `Saya butuh data pengguna. Setiap pengguna harus memiliki:
    - id (nomor unik)
    - nama (nama lengkap acak)
    - email (alamat email acak)
    - tanggal_bergabung (tanggal acak dalam setahun terakhir)`
*   **Atur "Jumlah Objek Data yang Diinginkan:" ke:**
    `5`
---