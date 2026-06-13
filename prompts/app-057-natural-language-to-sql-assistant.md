## Nama Aplikasi
Natural Language to SQL Assistant

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai penerjemah bahasa manusia ke query SQL. Pengguna menulis permintaan data dalam kalimat biasa dan mendeskripsikan skema tabel mereka, lalu AI akan menghasilkan query SQL yang sesuai.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Asisten SQL".
2.  **Form Input Pengguna:**
    *   **Input Permintaan:** Sebuah kolom input teks dengan label "Permintaan Data Anda (dalam bahasa biasa):".
    *   **Input Skema Tabel:** Sebuah area teks (textarea) dengan label "Deskripsikan Skema Tabel Anda:". Berikan placeholder seperti "Contoh: Tabel 'users' memiliki kolom id (INT), nama (VARCHAR), email (VARCHAR), tanggal_registrasi (DATETIME)."
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate SQL Query". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Querying...".
4.  **Area Output (Blok Kode):**
    *   Judul (H3): "Query SQL yang Dihasilkan:"
    *   Sebuah **kontainer blok kode** khusus (seperti `<pre><code>...</code></pre>`) untuk menampilkan query SQL. Kontainer ini harus memiliki latar belakang gelap dan menggunakan font monospace.
    *   **Tombol Salin Kode (Copy Code):** Di sudut kanan atas kontainer blok kode, **wajib** ada tombol "Copy" yang memungkinkan pengguna menyalin seluruh query ke clipboard dengan satu klik.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Blok Kode dengan Syntax Highlighting:** Aplikasi **wajib** menggunakan library JavaScript seperti `highlight.js` atau `prism.js` untuk merender respons dari AI. Library ini akan secara otomatis mendeteksi bahasa SQL dari Markdown fence (```sql) dan memberikan pewarnaan sintaks yang sesuai di dalam kontainer blok kode.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan permintaan dan skema, lalu mengklik tombol "Generate SQL Query".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang Data Analyst dan ahli SQL senior. Tugas Anda adalah menerjemahkan permintaan data dalam bahasa manusia menjadi query SQL yang bersih dan efisien.

    Berdasarkan informasi berikut:
    - Permintaan Data: """[Permintaan dari input pengguna]"""
    - Skema Tabel: """[Skema dari input pengguna]"""

    Tulis query SQL yang sesuai untuk mendapatkan data yang diminta. Asumsikan dialek SQL standar.

    PENTING: Respons Anda HARUS HANYA berisi blok kode SQL mentah dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons (yang hanya berisi blok kode SQL), aplikasi menggunakan library syntax highlighting untuk merendernya menjadi blok kode yang diformat dengan indah di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Permintaan Data Anda (dalam bahasa biasa):" dengan:**
    `Tunjukkan nama dan email dari semua pengguna yang mendaftar bulan lalu dan urutkan berdasarkan tanggal registrasi terbaru.`
*   **Isi kolom "Deskripsikan Skema Tabel Anda:" dengan:**
    `Tabel 'users' memiliki kolom id (INT), nama (VARCHAR), email (VARCHAR), tanggal_registrasi (DATETIME).`
---