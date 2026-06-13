## Nama Aplikasi
Koki Kreatif AI: Resep dari Kulkas

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai koki pribadi. Pengguna memasukkan daftar bahan-bahan yang mereka miliki, dan AI akan menciptakan sebuah ide resep masakan yang kreatif dan lezat, lengkap dengan nama masakan, daftar bahan, dan langkah-langkah pembuatannya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Koki Kreatif AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Bahan apa saja yang kamu punya? (pisahkan dengan koma atau baris baru)".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Cari Ide Resep!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Memasak...".
4.  **Area Output:**
    *   Judul (H3): "Ide Resep Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh resep.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan daftar bahan dan mengklik tombol "Cari Ide Resep!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang koki yang sangat kreatif dan inovatif, ahli dalam menciptakan masakan lezat dari bahan-bahan yang terbatas.

    Berikut adalah daftar bahan yang tersedia:
    """
    [Daftar bahan dari input pengguna]
    """

    Tugas Anda adalah membuat satu resep masakan yang menarik menggunakan bahan-bahan tersebut.
    - Anda boleh berasumsi pengguna memiliki bahan-bahan dasar seperti garam, merica, gula, minyak goreng, dan air.
    - Berikan nama yang kreatif untuk resep Anda.
    - Sajikan resep dalam format yang jelas: Nama Resep, Bahan-bahan, dan Langkah-langkah.

    Gunakan format Markdown untuk menyusun resep dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan resep yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Bahan apa saja yang kamu punya?..." dengan:**
    `Nasi sisa semalam, 2 butir telur, bawang putih, kecap manis, daun bawang`
---