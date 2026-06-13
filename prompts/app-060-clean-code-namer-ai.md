## Nama Aplikasi
Clean Code Namer AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web utilitas untuk para programmer. Pengguna mendeskripsikan tujuan sebuah variabel atau fungsi dalam bahasa biasa, dan AI akan memberikan beberapa saran nama yang deskriptif dalam berbagai konvensi penulisan kode (camelCase, PascalCase, snake_case, kebab-case).

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Clean Code Namer AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Jelaskan Tujuan Variabel atau Fungsi Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Sarankan Nama". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Berpikir...".
4.  **Area Output:**
    *   Judul (H3): "Saran Nama Variabel/Fungsi:"
    *   Sebuah area konten yang menampilkan saran nama dalam format tabel atau daftar yang jelas, dikelompokkan berdasarkan konvensi.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (terutama tabel atau daftar) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi dan mengklik tombol "Sarankan Nama".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang programmer senior yang sangat peduli dengan clean code dan konvensi penamaan yang baik.

    Berdasarkan deskripsi berikut:
    """
    [Deskripsi dari input pengguna]
    """

    Tugas Anda adalah memberikan beberapa saran nama variabel atau fungsi yang deskriptif. Sajikan saran tersebut dalam beberapa konvensi penulisan kode yang umum.

    Gunakan format tabel Markdown berikut untuk jawaban Anda:

    | Konvensi       | Saran Nama                 |
    |----------------|----------------------------|
    | camelCase      | [saran Anda]               |
    | PascalCase     | [saran Anda]               |
    | snake_case     | [saran Anda]               |
    | kebab-case     | [saran Anda]               |
    | CONSTANT_CASE  | [saran Anda]               |
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan tabel saran nama yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Tujuan Variabel atau Fungsi Anda:" dengan:**
    `Sebuah fungsi untuk mengambil data pengguna dari database berdasarkan ID.`
---