## Nama Aplikasi
Komentator Pertandingan Fiktif AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web hiburan yang menulis narasi komentar play-by-play yang seru untuk pertandingan olahraga yang sepenuhnya fiktif. Pengguna memasukkan nama olahraga aneh, dan AI akan menghasilkan naskah komentar yang dramatis dan penuh semangat seolah-olah sedang menyiarkan momen puncak pertandingan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Komentator Pertandingan Fiktif AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Nama Olahraga Fiktif yang Akan Dikomentari:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Mulai Komentari!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menyiapkan Mikrofon...".
4.  **Area Output:**
    *   Judul (H3): "Komentar Play-by-Play:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh narasi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama olahraga dan mengklik tombol "Mulai Komentari!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang komentator olahraga legendaris dengan energi tinggi. Anda mampu membuat pertandingan paling aneh sekalipun terdengar seru, dramatis, dan menegangkan.

    Berdasarkan nama olahraga fiktif berikut:
    """
    [Nama olahraga dari input pengguna]
    """

    Tugas Anda adalah menulis naskah komentar play-by-play yang seru untuk momen-momen puncak dari pertandingan final olahraga ini. Naskah harus:
    - Menciptakan nama-nama atlet fiktif.
    - Menggambarkan aksi dengan detail yang hidup.
    - Membangun ketegangan hingga mencapai klimaks.
    - Menggunakan frasa-frasa khas komentator olahraga ("Luar biasa!", "Tidak bisa dipercaya!", "Sejarah tercipta hari ini!").

    Gunakan format Markdown untuk penekanan pada momen-momen dramatis.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan narasi komentar yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Olahraga Fiktif yang Akan Dikomentari:" dengan:**
    `Final Kejuaraan Dunia Balap Siput Ekstrem`
---