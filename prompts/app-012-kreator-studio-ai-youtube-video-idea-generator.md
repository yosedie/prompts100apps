## Nama Aplikasi
Kreator Studio AI: YouTube Video Idea Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para kreator YouTube yang dapat menghasilkan 5 konsep video lengkap dari satu topik. Untuk setiap konsep, AI akan memberikan ide judul yang menarik (click-worthy), deskripsi visual untuk thumbnail yang mencolok, dan draf skrip untuk 30 detik pertama video yang dirancang untuk memaksimalkan retensi penonton.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Kreator Studio AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Topik Video Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Ide Video!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Mencari Inspirasi...".
4.  **Area Output:**
    *   Judul (H3): "5 Ide Video untuk Topik Anda:"
    *   Sebuah area konten tunggal untuk menampilkan 5 konsep video.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua Ide" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan topik dan mengklik tombol "Buat Ide Video!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli strategi konten YouTube dan copywriter viral yang sangat berpengalaman dalam menciptakan video yang mendapatkan engagement tinggi.

    Berdasarkan topik berikut:
    """
    [Topik dari input pengguna]
    """

    Tugas Anda adalah menghasilkan **5 konsep video YouTube yang lengkap**. Setiap konsep harus dirancang untuk memaksimalkan klik, retensi penonton, dan interaksi.

    Untuk setiap dari 5 ide, berikan tiga elemen berikut dalam format Markdown yang jelas:

    ---
    ### Ide [Nomor Ide]

    **Judul Video:** (Buat judul yang menarik, mengandung kata kunci, dan membuat penasaran).

    **Ide Thumbnail:** (Jelaskan secara visual apa yang harus ada di thumbnail: gambar utama, ekspresi wajah, teks singkat yang mencolok, warna kontras).

    **Skrip Pembuka (30 detik pertama):** (Tulis draf narasi untuk 30 detik pertama yang langsung mengait penonton, menjanjikan nilai, dan membuat mereka ingin menonton sampai akhir).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 5 konsep video yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Topik Video Anda:" dengan:**
    `Cara belajar bahasa baru dengan cepat`
---