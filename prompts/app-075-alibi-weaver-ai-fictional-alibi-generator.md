## Nama Aplikasi
Alibi Weaver AI: Fictional Alibi Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para penulis dan pemain peran. Pengguna mendeskripsikan sebuah kejahatan fiktif dan karakter yang membutuhkan alibi, lalu AI akan menyusun alibi yang detail, logis, dan (hampir) tidak bisa dipatahkan, lengkap dengan saksi dan bukti pendukung fiktif.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Alibi Weaver AI".
2.  **Form Input Pengguna:**
    *   **Input Kejahatan:** Sebuah area teks (textarea) dengan label "Jelaskan Kejahatan Fiktif (Waktu, Tempat, Jenis):".
    *   **Input Karakter:** Sebuah kolom input teks dengan label "Karakter yang Membutuhkan Alibi:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Alibi!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Celah...".
4.  **Area Output:**
    *   Judul (H3): "Alibi yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh alibi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail kejahatan dan karakter, lalu mengklik tombol "Buat Alibi!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang perencana kriminal jenius dan ahli strategi yang sangat teliti. Anda mampu menciptakan alibi yang nyaris sempurna.

    Berdasarkan skenario fiktif berikut:
    - Kejahatan: """[Deskripsi kejahatan dari input pengguna]"""
    - Karakter yang Membutuhkan Alibi: [Nama karakter dari input pengguna]

    Tugas Anda adalah membuat alibi yang detail dan meyakinkan untuk karakter tersebut. Alibi harus mencakup:

    1.  **Linimasa (Timeline):** Rincian aktivitas karakter, menit demi menit, selama waktu kejahatan terjadi.
    2.  **Saksi Fiktif:** Sebutkan setidaknya satu orang atau tempat (misal: pelayan restoran, rekaman CCTV) yang bisa "memverifikasi" keberadaan karakter.
    3.  **Bukti Pendukung Fiktif:** Sebutkan bukti fisik atau digital yang mendukung alibi (misal: struk pembayaran, postingan media sosial, riwayat panggilan).
    4.  **Sikap Saat Diinterogasi:** Berikan saran singkat tentang bagaimana karakter harus bersikap jika ditanyai oleh detektif.

    Gunakan format Markdown untuk menyusun alibi dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan alibi yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Kejahatan Fiktif (Waktu, Tempat, Jenis):" dengan:**
    `Pembobolan brankas di Museum Seni Kota pada hari Selasa, antara jam 10 malam hingga 11 malam.`
*   **Isi kolom "Karakter yang Membutuhkan Alibi:" dengan:**
    `Victor "The Ghost" Sterling, seorang pencuri ulung yang dikenal cerdas.`
---