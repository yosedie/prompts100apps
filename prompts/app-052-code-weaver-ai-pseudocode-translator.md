## Nama Aplikasi
Code Weaver AI: Pseudocode Translator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai penerjemah dari logika bahasa manusia atau pseudocode menjadi kode pemrograman yang fungsional. Pengguna menulis alur logika mereka, memilih bahasa target, dan AI akan menghasilkan kode yang siap pakai.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Code Weaver AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tulis Logika atau Pseudocode Anda di Sini:".
    *   **Pilihan Bahasa Target:** Sebuah menu dropdown (select) dengan label "Terjemahkan ke Bahasa:" dan opsi: "Python", "JavaScript".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Translate to Code". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menenun Kode...".
4.  **Area Output (Blok Kode):**
    *   Judul (H3): "Kode yang Dihasilkan:"
    *   Sebuah **kontainer blok kode** khusus (seperti `<pre><code>...</code></pre>`) untuk menampilkan kode yang dihasilkan. Kontainer ini harus memiliki latar belakang gelap dan menggunakan font monospace.
    *   **Tombol Salin Kode (Copy Code):** Di sudut kanan atas kontainer blok kode, **wajib** ada tombol "Copy" yang memungkinkan pengguna menyalin seluruh kode ke clipboard dengan satu klik.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Blok Kode dengan Syntax Highlighting:** Aplikasi **wajib** menggunakan library JavaScript seperti `highlight.js` atau `prism.js` untuk merender respons dari AI. Library ini akan secara otomatis mendeteksi bahasa (Python/JavaScript) dari Markdown fence (```python) dan memberikan pewarnaan sintaks yang sesuai di dalam kontainer blok kode.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan pseudocode, memilih bahasa, dan mengklik tombol "Translate to Code".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang programmer ahli dan code generator. Tugas Anda adalah menerjemahkan pseudocode atau logika bahasa manusia menjadi kode yang bersih dan fungsional.

    Berdasarkan permintaan berikut:
    - Pseudocode: """[Teks dari input pengguna]"""
    - Bahasa Target: [Bahasa dari pilihan pengguna]

    Terjemahkan pseudocode tersebut ke dalam bahasa [Bahasa dari pilihan pengguna].

    PENTING: Respons Anda HARUS HANYA berisi blok kode Markdown mentah untuk bahasa yang diminta dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons (yang hanya berisi blok kode), aplikasi menggunakan library syntax highlighting untuk merendernya menjadi blok kode yang diformat dengan indah di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tulis Logika atau Pseudocode Anda di Sini:" dengan:**
    `Buat sebuah fungsi bernama 'sapa'.
    Fungsi ini menerima satu parameter: 'nama'.
    Di dalam fungsi, cetak kalimat "Halo, [nama]! Selamat datang."`
*   **Atur pilihan "Terjemahkan ke Bahasa:" ke:**
    `Python`
---