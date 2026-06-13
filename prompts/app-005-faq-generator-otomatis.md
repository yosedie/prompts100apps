## Nama Aplikasi
FAQ Generator Otomatis

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang secara cerdas menghasilkan daftar Pertanyaan yang Sering Diajukan (FAQ) dari sebuah teks deskripsi. Pengguna cukup menempelkan deskripsi produk, layanan, atau proyek, dan aplikasi akan membuat daftar pertanyaan yang relevan beserta jawabannya yang jelas dan ringkas.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pembuat FAQ Otomatis".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Deskripsi Produk atau Layanan Anda di Sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Daftar FAQ". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Daftar FAQ yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan daftar pertanyaan dan jawaban.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `###` untuk pertanyaan dan `**` untuk tebal) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan teks deskripsi dan mengklik tombol "Buat Daftar FAQ".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang spesialis customer support dan copywriter yang berpengalaman. Tugas Anda adalah membaca deskripsi sebuah produk atau layanan dan mengantisipasi pertanyaan yang paling mungkin ditanyakan oleh calon pengguna.

    Berikut adalah deskripsi yang perlu dianalisis:
    """
    [Teks deskripsi dari input pengguna]
    """

    Berdasarkan deskripsi di atas, buatlah daftar Pertanyaan yang Sering Diajukan (FAQ) yang komprehensif. Untuk setiap pertanyaan, berikan jawaban yang jelas dan ringkas langsung dari informasi yang tersedia.

    Gunakan format Markdown berikut untuk setiap item FAQ:
    ### Pertanyaan?
    Jawaban.

    Pastikan pertanyaan mencakup aspek-aspek penting seperti fitur utama, harga, keamanan, dan cara penggunaan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan daftar FAQ yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Deskripsi Produk atau Layanan Anda di Sini:" dengan:**
    `AwanAman adalah layanan penyimpanan cloud premium yang menawarkan keamanan enkripsi end-to-end. Pengguna mendapatkan 10GB gratis saat mendaftar dan bisa mengupgrade ke paket berbayar untuk kapasitas lebih besar. Fitur kami termasuk sinkronisasi file otomatis di berbagai perangkat, berbagi file dengan tautan aman, dan riwayat versi file selama 30 hari.`
---