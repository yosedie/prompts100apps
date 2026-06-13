## Nama Aplikasi
Laporan Cuaca Puitis AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang mengubah data cuaca teknis menjadi sebuah deskripsi naratif yang puitis dan imajinatif. Pengguna memasukkan kondisi cuaca, dan AI akan menulis sebuah paragraf singkat yang melukiskan suasana hari itu dengan indah.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Laporan Cuaca Puitis AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Kondisi Cuaca Hari Ini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Deskripsi Puitis". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Merasakan Angin...".
4.  **Area Output:**
    *   Judul (H3): "Laporan Cuaca Hari Ini:"
    *   Sebuah area konten tunggal untuk menampilkan deskripsi puitis.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan kondisi cuaca dan mengklik tombol "Buat Deskripsi Puitis".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penyair dan penulis alam (nature writer). Anda mampu melihat keindahan dan cerita di balik fenomena cuaca yang paling biasa sekalipun.

    Berdasarkan data cuaca berikut:
    """
    [Kondisi cuaca dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah deskripsi cuaca yang puitis dan imajinatif dalam satu paragraf singkat (3-5 kalimat).
    - Gunakan metafora dan bahasa kiasan.
    - Fokus pada perasaan dan suasana yang diciptakan oleh cuaca tersebut.
    - Hindari menyebutkan angka atau data teknis secara langsung.

    Gunakan format Markdown untuk penekanan pada kata-kata tertentu jika perlu.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan deskripsi puitis di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Kondisi Cuaca Hari Ini:" dengan:**
    `Suhu 25 derajat Celcius, berawan, sedikit berangin.`
---