## Nama Aplikasi
Penulis Surat Protes AI: Complaint Letter Assistant

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna menyusun surat keluhan atau protes yang formal dan efektif. Pengguna mendeskripsikan masalah yang mereka hadapi dan solusi yang diinginkan, lalu AI akan menulis draf surat yang jelas, tegas, namun tetap sopan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Surat Protes AI".
2.  **Form Input Pengguna:**
    *   **Input Nama Perusahaan:** Sebuah kolom input teks dengan label "Nama Perusahaan/Lembaga yang Dituju:".
    *   **Input Masalah:** Sebuah area teks (textarea) dengan label "Jelaskan Masalah Anda Secara Rinci:".
    *   **Input Solusi:** Sebuah area teks (textarea) dengan label "Apa Solusi atau Hasil yang Anda Inginkan?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Susun Surat Protes". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun...".
4.  **Area Output:**
    *   Judul (H3): "Draf Surat Protes Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh surat.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail keluhan dan mengklik tombol "Susun Surat Protes".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis surat bisnis profesional dan advokat konsumen. Anda ahli dalam menyusun komunikasi yang jelas, formal, dan persuasif.

    Berdasarkan informasi keluhan berikut:
    - Perusahaan yang Dituju: [Nama dari input pengguna]
    - Deskripsi Masalah: """[Masalah dari input pengguna]"""
    - Solusi yang Diinginkan: """[Solusi dari input pengguna]"""

    Tugas Anda adalah menulis draf surat keluhan atau protes yang formal. Surat harus:
    - Memiliki struktur yang jelas: pembukaan (menyatakan tujuan surat), isi (merinci masalah secara kronologis dan faktual), dan penutup (menyatakan solusi yang diinginkan dan batas waktu untuk tanggapan).
    - Menggunakan nada yang tegas dan serius, namun tetap sopan dan profesional.
    - Menghindari bahasa yang emosional atau menuduh.

    Gunakan placeholder seperti `[Nama Anda]` dan `[Tanggal]` agar mudah disesuaikan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan draf surat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Perusahaan/Lembaga yang Dituju:" dengan:**
    `SuperNet ISP`
*   **Isi kolom "Jelaskan Masalah Anda Secara Rinci:" dengan:**
    `Koneksi internet saya dengan nomor pelanggan 12345 sudah putus total selama 3 hari terakhir, sejak tanggal 15 September 2025. Saya sudah menelepon customer service sebanyak 5 kali dan setiap kali hanya dijanjikan akan segera diperbaiki tanpa ada kepastian waktu.`
*   **Isi kolom "Apa Solusi atau Hasil yang Anda Inginkan?" dengan:**
    `Saya menuntut teknisi untuk datang dan memperbaiki masalah dalam 24 jam ke depan. Selain itu, saya meminta kompensasi berupa potongan tagihan untuk hari-hari di mana saya tidak menerima layanan.`
---