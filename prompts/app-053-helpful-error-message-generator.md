## Nama Aplikasi
Helpful Error Message Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para developer yang berfungsi sebagai penulis pesan error. Pengguna mendeskripsikan sebuah situasi error teknis, dan AI akan menulis pesan error yang jelas, informatif, dan ramah pengguna, lengkap dengan penjelasan dan saran perbaikan untuk developer.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Helpful Error Message Generator".
2.  **Form Input Pengguna:**
    *   **Input Situasi Error:** Sebuah area teks (textarea) dengan label "Jelaskan Situasi Error Secara Teknis:".
    *   **Pilihan Gaya Pesan:** Sebuah menu dropdown (select) dengan label "Pilih Gaya Pesan:" dan opsi: "Helpful & Professional", "Helpful & Humorous".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate Pesan Error". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Alasan...".
4.  **Area Output:**
    *   Judul (H3): "Pesan Error yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh pesan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan blok kode) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi situasi error, memilih gaya, dan mengklik tombol "Generate Pesan Error".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang developer senior sekaligus UX writer yang ahli dalam membuat pesan error yang tidak membuat frustrasi.

    Berdasarkan informasi berikut:
    - Situasi Error: [Deskripsi dari input pengguna]
    - Gaya Pesan yang Diinginkan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah menulis pesan error yang lengkap. Pesan harus mencakup:

    1.  **Pesan Error:** Teks yang akan ditampilkan kepada pengguna akhir. Harus jelas, ringkas, dan sesuai dengan gaya yang diminta.
    2.  **Penjelasan untuk Developer:** Penjelasan singkat tentang kemungkinan penyebab error ini.
    3.  **Saran Perbaikan:** Langkah-langkah konkret yang bisa dicoba oleh developer untuk mengatasi masalah ini.

    Gunakan format Markdown untuk menyusun jawaban dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan pesan error yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Situasi Error Secara Teknis:" dengan:**
    `Panggilan API gagal karena API key yang diberikan tidak valid atau sudah kedaluwarsa.`
*   **Atur pilihan "Pilih Gaya Pesan:" ke:**
    `Helpful & Humorous`
---