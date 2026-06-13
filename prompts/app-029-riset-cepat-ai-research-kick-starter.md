## Nama Aplikasi
Riset Cepat AI: Research Kick-starter

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai titik awal untuk sebuah riset. Pengguna memasukkan sebuah pertanyaan riset, dan AI akan memberikan ringkasan awal, mengidentifikasi poin-poin kunci, dan menyarankan kata kunci untuk pencarian literatur lebih lanjut, mempercepat proses riset secara signifikan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Riset Cepat AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Masukkan Pertanyaan Riset Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Mulai Riset". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Mencari Informasi...".
4.  **Area Output:** Didesain seperti dasbor ringkasan dengan tiga bagian yang jelas:
    *   **Bagian 1: Ringkasan Awal:** Judul (H3) "Ringkasan Awal" diikuti area konten untuk ringkasan singkat.
    *   **Bagian 2: Poin-Poin Kunci:** Judul (H3) "Poin-Poin Kunci" diikuti area konten untuk daftar poin.
    *   **Bagian 3: Kata Kunci untuk Riset Lanjutan:** Judul (H3) "Kata Kunci untuk Riset Lanjutan" diikuti area konten untuk daftar kata kunci.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `###`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada ketiga bagian di Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan pertanyaan riset dan mengklik tombol "Mulai Riset".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang asisten riset AI yang terlatih untuk mensintesis informasi dan mengidentifikasi konsep-konsep inti dengan cepat.

    Berdasarkan pertanyaan riset berikut:
    """
    [Pertanyaan dari input pengguna]
    """

    Tugas Anda adalah memberikan tiga hal untuk membantu memulai proses riset:

    1.  **Ringkasan Awal:** Tulis ringkasan singkat (2-4 kalimat) yang menjawab pertanyaan secara umum dan memberikan konteks.
    2.  **Poin-Poin Kunci:** Identifikasi 3-5 poin atau sub-topik paling penting yang terkait dengan pertanyaan. Sajikan dalam bentuk daftar poin.
    3.  **Kata Kunci untuk Riset Lanjutan:** Berikan daftar kata kunci dan frasa yang bisa digunakan pengguna di database akademik (seperti Google Scholar, JSTOR) untuk menemukan literatur yang relevan.

    Gunakan format Markdown untuk seluruh respons Anda, dengan sub-judul yang jelas untuk setiap bagian.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan hasil analisis di tiga bagian yang sesuai di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Pertanyaan Riset Anda:" dengan:**
    `Apa dampak penggunaan media sosial terhadap kesehatan mental remaja?`
---