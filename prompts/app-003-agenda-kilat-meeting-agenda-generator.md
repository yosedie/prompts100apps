## Nama Aplikasi
Agenda Kilat: Meeting Agenda Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang sangat efisien untuk membuat agenda rapat terstruktur. Pengguna hanya perlu memasukkan satu kalimat tujuan rapat, waktu mulai, dan durasi, lalu aplikasi akan secara otomatis menghasilkan agenda lengkap dengan alokasi waktu, topik bahasan, dan tujuan untuk setiap sesi.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Agenda Kilat".
2.  **Form Input Pengguna:** Dibuat dalam satu baris atau grid yang rapi.
    *   **Input Tujuan Rapat:** Sebuah kolom input teks dengan label "Tujuan Utama Rapat (1 Kalimat):".
    *   **Input Waktu Mulai:** Sebuah kolom input waktu (type="time") dengan label "Waktu Mulai:".
    *   **Input Durasi:** Sebuah kolom input angka (type="number") dengan label "Total Durasi (menit):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Agenda". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menyusun Agenda...".
4.  **Area Output:**
    *   Sebuah area konten tunggal untuk menampilkan seluruh agenda yang dihasilkan.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `# Judul`, `**tebal**`, `* item daftar`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi tujuan, waktu mulai, dan durasi rapat, lalu mengklik tombol "Buat Agenda".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang fasilitator rapat profesional dan asisten eksekutif yang sangat terorganisir.

    Berdasarkan informasi berikut:
    - Tujuan Utama Rapat: [Tujuan dari input pengguna]
    - Waktu Mulai: [Waktu dari input pengguna]
    - Total Durasi: [Durasi dari input pengguna] menit

    Tugas Anda adalah membuat agenda rapat yang detail, logis, dan efisien. Agenda harus mencakup:
    1.  Alokasi waktu yang tepat untuk setiap sesi (contoh: 09:00 - 09:10).
    2.  Topik bahasan yang jelas.
    3.  Tujuan atau hasil yang diharapkan dari setiap sesi.

    Strukturkan agenda secara logis, dimulai dengan perkenalan, diikuti oleh pembahasan inti, dan diakhiri dengan rangkuman serta langkah selanjutnya (action items). Gunakan format Markdown untuk kejelasan (judul, sub-judul, daftar, dan teks tebal).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan agenda yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tujuan Utama Rapat (1 Kalimat):" dengan:**
    `Membahas dan memutuskan strategi peluncuran produk baru untuk kuartal depan.`
*   **Isi kolom "Waktu Mulai:" dengan:**
    `09:00`
*   **Isi kolom "Total Durasi (menit):" dengan:**
    `60`
---