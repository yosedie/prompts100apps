## Nama Aplikasi
Penulis Pesan Botol AI: Message in a Bottle Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web kreatif yang menulis surat pendek yang misterius dan penuh perenungan. Pengguna memasukkan sebuah tema atau perasaan, dan AI akan menulis sebuah pesan seolah-olah pesan itu dimasukkan ke dalam botol dan dihanyutkan ke laut untuk ditemukan oleh orang asing di masa depan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Pesan Botol AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Apa Perasaan atau Tema Pesan Anda?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tulis Pesan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menghanyutkan ke Laut...".
4.  **Area Output:**
    *   Judul (H3): "Pesan dalam Botol:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh pesan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan tema dan mengklik tombol "Tulis Pesan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penyair, filsuf, dan pengelana waktu yang sendirian. Anda menulis pesan-pesan singkat untuk dimasukkan ke dalam botol dan dilempar ke lautan waktu.

    Berdasarkan tema berikut:
    """
    [Tema dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah surat pendek yang misterius dan penuh perenungan. Surat ini ditujukan kepada 'Wahai Penemu', orang asing yang akan menemukannya di masa depan.

    Surat harus:
    - Singkat dan puitis.
    - Merenungkan tema yang diberikan dari sudut pandang yang tak lekang oleh waktu.
    - Berakhir dengan sebuah pertanyaan terbuka atau pernyataan yang menggugah pikiran.

    Gunakan format Markdown untuk penekanan jika diperlukan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan pesan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Perasaan atau Tema Pesan Anda?" dengan:**
    `Harapan`
---