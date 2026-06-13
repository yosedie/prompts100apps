## Nama Aplikasi
Analis Umpan Balik Pelanggan

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web analitik yang mampu merangkum ratusan ulasan pelanggan. Pengguna menempelkan sekumpulan ulasan, dan aplikasi akan menganalisisnya untuk mengidentifikasi tema-tema utama yang dibicarakan, sentimen keseluruhan (positif, negatif, atau campuran), dan memberikan daftar saran perbaikan yang bisa ditindaklanjuti.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Analis Umpan Balik Pelanggan".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang sangat besar dengan label "Tempelkan semua ulasan pelanggan di sini (pisahkan setiap ulasan dengan baris baru):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Analisis Umpan Balik". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:** Didesain seperti dasbor ringkasan dengan tiga bagian yang jelas:
    *   **Bagian 1: Tema Utama:** Judul (H3) "Tema Utama" diikuti area konten untuk daftar poin-poin utama.
    *   **Bagian 2: Analisis Sentimen:** Judul (H3) "Analisis Sentimen" diikuti area konten untuk paragraf ringkasan sentimen.
    *   **Bagian 3: Saran Perbaikan:** Judul (H3) "Saran Perbaikan (Actionable)" diikuti area konten untuk daftar saran bernomor.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `###`, `**`, `*`, dan `1.`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada ketiga bagian di Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan teks ulasan dan mengklik tombol "Analisis Umpan Balik".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang analis data dan peneliti pasar yang ahli dalam mengolah data kualitatif dari umpan balik pelanggan.

    Berikut adalah sekumpulan ulasan pelanggan untuk dianalisis:
    """
    [Teks ulasan dari input pengguna]
    """

    Tugas Anda adalah menganalisis semua ulasan tersebut dan menyajikan hasilnya dalam tiga bagian yang jelas:

    ### 1. Tema Utama
    Identifikasi 3-5 tema atau topik utama yang paling sering dibicarakan pelanggan (contoh: Kualitas Produk, Harga, Layanan Pelanggan, Pengiriman). Sajikan dalam bentuk daftar poin.

    ### 2. Analisis Sentimen
    Berikan ringkasan singkat mengenai sentimen keseluruhan dari ulasan tersebut. Apakah cenderung positif, negatif, atau campuran? Sebutkan aspek apa yang paling disukai dan paling tidak disukai.

    ### 3. Saran Perbaikan (Actionable)
    Berdasarkan tema negatif atau keluhan yang muncul, berikan daftar saran perbaikan yang konkret dan bisa ditindaklanjuti oleh tim produk atau bisnis. Sajikan dalam bentuk daftar bernomor.

    Gunakan format Markdown untuk seluruh respons Anda.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan hasil analisis di tiga bagian yang sesuai di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan semua ulasan pelanggan di sini..." dengan:**
    ```
    Kopi dari mesin ini enak sekali, aromanya mantap! Sangat puas.
    Barangnya sampai dengan cepat, tapi bodinya terasa agak ringkih, terlalu banyak plastik.
    Saya suka desainnya yang minimalis, cocok di dapur saya. Tapi suaranya agak berisik saat menggiling kopi.
    Sulit sekali membersihkan wadah ampas kopinya, desainnya kurang praktis.
    Harga sangat terjangkau untuk kualitas kopi yang dihasilkan. Recommended!
    Mesin saya rusak setelah dipakai 2 minggu, layanan pelanggannya lambat merespons.
    Fitur timer otomatisnya sangat membantu di pagi hari.
    ```
---