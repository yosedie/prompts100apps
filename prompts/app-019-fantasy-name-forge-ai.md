## Nama Aplikasi
Fantasy Name Forge AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web kreatif yang berfungsi sebagai generator nama fantasi. Pengguna memilih kategori (Karakter, Tempat, Artefak) dan memberikan tema opsional, lalu AI akan menciptakan sejumlah nama yang unik, lengkap dengan etimologi fiktif singkat untuk setiap nama.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Fantasy Name Forge AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Kategori:** Sebuah menu dropdown (select) dengan label "Pilih Kategori Nama:" dan opsi: "Karakter", "Tempat", "Artefak".
    *   **Input Tema:** Sebuah kolom input teks dengan label "Tema atau Ras (Opsional):".
    *   **Input Jumlah:** Sebuah kolom input angka (type="number") dengan label "Jumlah Nama yang Diinginkan:" dan nilai default 5.
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tempa Nama!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menempa...".
4.  **Area Output:**
    *   Judul (H3): "Nama Fantasi yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan daftar nama.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih kategori, mengisi tema (opsional), dan jumlah, lalu mengklik tombol "Tempa Nama!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang world-builder, loremaster, dan ahli bahasa fiktif untuk dunia fantasi.

    Berdasarkan kriteria berikut:
    - Kategori Nama: [Kategori dari pilihan pengguna]
    - Tema/Ras: [Tema dari input pengguna, jika ada]
    - Jumlah Nama: [Jumlah dari input pengguna]

    Tugas Anda adalah menciptakan nama-nama fantasi yang unik dan terdengar otentik. Untuk setiap nama, berikan juga etimologi fiktif (asal-usul atau makna nama) yang singkat dan menarik.

    Gunakan format Markdown berikut untuk setiap entri:
    **[Nama yang Dihasilkan]** - *[Etimologi fiktif singkat]*
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan daftar nama yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Kategori Nama:" ke:**
    `Karakter`
*   **Isi kolom "Tema atau Ras (Opsional):" dengan:**
    `Elf penjaga hutan kuno`
*   **Atur "Jumlah Nama yang Diinginkan:" ke:**
    `5`
---