## Nama Aplikasi
Pemandu Wisata Virtual AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pemandu wisata pribadi. Pengguna memasukkan nama sebuah kota atau museum terkenal, dan AI akan menulis sebuah narasi tur yang imersif dan informatif, seolah-olah pengguna sedang berjalan-jalan di lokasi tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pemandu Wisata Virtual AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Lokasi Tur (Kota atau Museum):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Mulai Tur Virtual!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menjelajahi Lokasi...".
4.  **Area Output:**
    *   Judul (H3): "Narasi Tur Virtual Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh narasi tur.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan lokasi dan mengklik tombol "Mulai Tur Virtual!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pemandu wisata (tour guide) yang sangat berpengetahuan, karismatik, dan pandai bercerita.

    Berdasarkan lokasi berikut:
    """
    [Lokasi dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah naskah tur virtual yang imersif. Tulis narasi dari sudut pandang orang pertama jamak ("Kita sekarang berada di...", "Di sebelah kanan kita, kita bisa melihat...").

    Narasi harus mencakup:
    - **Deskripsi Visual:** Lukiskan gambaran yang jelas tentang pemandangan di sekitar.
    - **Fakta Sejarah:** Sisipkan fakta-fakta sejarah yang menarik dan relevan.
    - **Anekdot & Cerita Menarik:** Bagikan cerita atau detail kecil yang tidak banyak diketahui orang.
    - **Arahan Virtual:** Berikan arahan seolah-olah kita sedang berjalan ("Mari kita berjalan sedikit ke depan...").

    Gunakan format Markdown untuk penekanan pada nama tempat atau detail penting.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan narasi tur yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Lokasi Tur (Kota atau Museum):" dengan:**
    `Tokyo`
---