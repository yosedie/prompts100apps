## Nama Aplikasi
Code Commenter AI: Docstring Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang secara otomatis mendokumentasikan kode. Pengguna menempelkan sebuah fungsi kode, dan AI akan menganalisisnya untuk menulis komentar atau docstring yang jelas, menjelaskan tujuan fungsi, parameter input, dan nilai outputnya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Code Commenter AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Fungsi Kode Anda di Sini:". Area teks ini harus menggunakan font monospace.
    *   **Pilihan Gaya Komentar:** Sebuah menu dropdown (select) dengan label "Pilih Gaya Komentar:" dan opsi: "Docstring (Python)", "JSDoc (JavaScript)".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate Komentar". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis Kode...".
4.  **Area Output (Blok Kode):**
    *   Judul (H3): "Kode dengan Komentar:"
    *   Sebuah **kontainer blok kode** khusus (seperti `<pre><code>...</code></pre>`) untuk menampilkan kode yang sudah ditambahkan komentar. Kontainer ini harus memiliki latar belakang gelap dan menggunakan font monospace.
    *   **Tombol Salin Kode (Copy Code):** Di sudut kanan atas kontainer blok kode, **wajib** ada tombol "Copy" yang memungkinkan pengguna menyalin seluruh kode ke clipboard dengan satu klik.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Blok Kode dengan Syntax Highlighting:** Aplikasi **wajib** menggunakan library JavaScript seperti `highlight.js` atau `prism.js` untuk merender respons dari AI. Library ini akan secara otomatis mendeteksi bahasa dan memberikan pewarnaan sintaks yang sesuai di dalam kontainer blok kode.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan kode, memilih gaya, dan mengklik tombol "Generate Komentar".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang programmer senior yang sangat disiplin dalam menulis kode yang bersih dan terdokumentasi dengan baik.

    Berdasarkan fungsi kode berikut:
    ```
    [Kode dari input pengguna]
    ```

    Tugas Anda adalah menganalisis fungsi ini dan menulis komentar dokumentasi (docstring/JSDoc) yang sesuai dengan gaya "[Gaya dari pilihan pengguna]".

    Komentar harus mencakup:
    1.  Deskripsi singkat tentang apa yang dilakukan fungsi tersebut.
    2.  Penjelasan untuk setiap parameter (Args/Params).
    3.  Penjelasan tentang apa yang dikembalikan oleh fungsi (Returns).

    PENTING: Respons Anda HARUS HANYA berisi blok kode mentah yang sudah digabungkan dengan komentar barunya, dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons (yang hanya berisi blok kode), aplikasi menggunakan library syntax highlighting untuk merendernya menjadi blok kode yang diformat dengan indah di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Fungsi Kode Anda di Sini:" dengan:**
    ```python
    def calculate_area(length, width):
        if length < 0 or width < 0:
            return None
        area = length * width
        return area
    ```
*   **Atur pilihan "Pilih Gaya Komentar:" ke:**
    `Docstring (Python)`
---