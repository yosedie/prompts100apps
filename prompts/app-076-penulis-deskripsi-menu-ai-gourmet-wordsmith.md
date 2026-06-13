## Nama Aplikasi
Penulis Deskripsi Menu AI: Gourmet Wordsmith

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang mengubah daftar bahan sederhana menjadi deskripsi menu yang menggugah selera. Pengguna memasukkan nama hidangan dan bahan utamanya, lalu AI akan menulis deskripsi yang puitis dan mewah, layaknya di restoran bintang lima.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Deskripsi Menu AI".
2.  **Form Input Pengguna:**
    *   **Input Nama Hidangan:** Sebuah kolom input teks dengan label "Nama Hidangan:".
    *   **Input Bahan Utama:** Sebuah area teks (textarea) dengan label "Bahan-Bahan Utama (pisahkan dengan koma):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tulis Deskripsi Mewah". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Meracik Kata...".
4.  **Area Output:**
    *   Judul (H3): "Deskripsi Menu yang Menggugah Selera:"
    *   Sebuah area konten tunggal untuk menampilkan deskripsi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama hidangan dan bahan, lalu mengklik tombol "Tulis Deskripsi Mewah".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis menu profesional (menu writer) untuk restoran fine dining. Anda ahli dalam menggunakan kata-kata yang deskriptif dan menggugah selera untuk membuat hidangan terdengar mewah dan tak tertahankan.

    Berdasarkan informasi hidangan berikut:
    - Nama Hidangan: [Nama dari input pengguna]
    - Bahan Utama: [Bahan dari input pengguna]

    Tugas Anda adalah menulis SATU paragraf deskripsi menu yang singkat namun puitis. Deskripsi harus:
    - Menggunakan kata-kata sensorik (menggambarkan tekstur, aroma, dan rasa).
    - Menyoroti kualitas bahan-bahan.
    - Membuat hidangan terdengar seperti sebuah pengalaman kuliner yang istimewa.

    PENTING: Hanya berikan teks deskripsinya saja, tanpa tambahan komentar.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan deskripsi menu di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Hidangan:" dengan:**
    `Ayam Bakar Madu`
*   **Isi kolom "Bahan-Bahan Utama (pisahkan dengan koma):" dengan:**
    `ayam, madu, bawang putih, jahe, kecap, sambal`
---