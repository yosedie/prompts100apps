## Nama Aplikasi
Asisten Tanaman Hias AI: Plant Care Guide

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai 'dokter tanaman' virtual. Pengguna memasukkan nama tanaman hias mereka, dan AI akan memberikan panduan perawatan yang lengkap dan mudah diikuti, mencakup frekuensi penyiraman, kebutuhan cahaya, dan cara mengatasi hama umum.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Asisten Tanaman Hias AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Nama Tanaman Hias Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Cari Panduan Perawatan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Panduan...".
4.  **Area Output:**
    *   Judul (H3): "Panduan Perawatan Lengkap:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh panduan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama tanaman dan mengklik tombol "Cari Panduan Perawatan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli hortikultura dan 'dokter tanaman' yang berpengalaman. Anda mampu memberikan saran perawatan yang jelas dan mudah diikuti bahkan untuk pemula.

    Berdasarkan nama tanaman berikut:
    """
    [Nama tanaman dari input pengguna]
    """

    Tugas Anda adalah memberikan panduan perawatan yang lengkap. Panduan harus mencakup bagian-bagian berikut:

    - **Penyiraman (Watering):** Jelaskan seberapa sering harus disiram dan bagaimana cara terbaik untuk mengecek kelembapan tanah.
    - **Kebutuhan Cahaya (Light Needs):** Jelaskan jenis pencahayaan yang ideal (cahaya terang tidak langsung, cahaya rendah, dll.).
    - **Kelembapan & Suhu (Humidity & Temperature):** Berikan saran tentang tingkat kelembapan dan suhu ruangan yang disukai.
    - **Hama Umum & Cara Mengatasi (Common Pests & Solutions):** Sebutkan 2-3 hama yang sering menyerang tanaman ini dan berikan solusi sederhana untuk mengatasinya.

    Gunakan format Markdown untuk menyusun panduan dengan rapi (judul, sub-judul, daftar poin).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan panduan perawatan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Nama Tanaman Hias Anda:" dengan:**
    `Monstera Deliciosa`
---