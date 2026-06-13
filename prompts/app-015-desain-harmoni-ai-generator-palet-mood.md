## Nama Aplikasi
Desain Harmoni AI: Generator Palet & Mood

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para desainer dan kreator. Pengguna memasukkan sebuah tema atau kata kunci visual, dan AI akan menghasilkan palet warna yang harmonis (lengkap dengan kode HEX) serta deskripsi singkat tentang suasana (mood) yang diciptakan oleh palet tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Desain Harmoni AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Tema atau Kata Kunci Visual:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Palet Desain". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Harmoni...".
4.  **Area Output:** Dibagi menjadi dua bagian yang jelas:
    *   **Bagian Palet Warna:**
        *   Judul (H3): "Palet Warna yang Dihasilkan:"
        *   Area ini harus menampilkan 5 kotak berwarna (swatches) secara horizontal. Latar belakang setiap kotak harus diisi dengan warna sesuai kode HEX yang dihasilkan. Di dalam setiap kotak, tampilkan kode HEX warna tersebut dengan teks yang kontras agar mudah dibaca.
    *   **Bagian Deskripsi Mood:**
        *   Judul (H3): "Deskripsi Mood Visual:"
        *   Area konten untuk menampilkan deskripsi singkat dari AI.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah sintaks Markdown (jika ada) menjadi elemen HTML yang diformat. Terapkan rendering ini pada bagian Deskripsi Mood.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan tema dan mengklik tombol "Buat Palet Desain".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang desainer grafis senior dan ahli teori warna (color theorist).

    Berdasarkan tema berikut:
    """
    [Tema dari input pengguna]
    """

    Tugas Anda adalah menghasilkan DUA hal:

    1.  **Palet Warna:** Buat palet berisi 5 warna yang harmonis. Sajikan dalam format daftar, di mana setiap item adalah kode HEX warna (contoh: `#FFFFFF`).
    2.  **Deskripsi Mood Visual:** Tulis deskripsi singkat (2-3 kalimat) yang menjelaskan suasana atau mood yang diciptakan oleh palet warna ini.

    Pisahkan kedua bagian dengan jelas menggunakan penanda unik: `---MOOD---`.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi mem-parsing teks tersebut. Teks sebelum `---MOOD---` adalah daftar kode HEX. Teks setelahnya adalah deskripsi mood.
5.  Aplikasi menggunakan daftar kode HEX untuk membuat 5 kotak berwarna secara dinamis.
6.  Aplikasi merender deskripsi mood (dengan Markdown) dan menampilkannya di area yang sesuai.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Tema atau Kata Kunci Visual:" dengan:**
    `Tropis senja`
---