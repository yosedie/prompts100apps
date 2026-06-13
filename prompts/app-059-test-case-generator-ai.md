## Nama Aplikasi
Test Case Generator AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para software tester dan developer. Pengguna mendeskripsikan sebuah fitur aplikasi, dan AI akan secara otomatis membuat daftar kasus uji (test cases) yang komprehensif, mencakup skenario normal (happy path), skenario negatif, dan kasus-kasus tepi (edge cases).

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Test Case Generator AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Jelaskan Fitur Aplikasi yang Akan Diuji:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Kasus Uji". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis Fitur...".
4.  **Area Output:**
    *   Judul (H3): "Daftar Kasus Uji (Test Cases):"
    *   Sebuah area konten tunggal untuk menampilkan seluruh daftar.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi fitur dan mengklik tombol "Buat Kasus Uji".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang Quality Assurance (QA) Engineer senior yang sangat teliti dan ahli dalam merancang kasus uji (test cases).

    Berdasarkan deskripsi fitur aplikasi berikut:
    """
    [Deskripsi fitur dari input pengguna]
    """

    Tugas Anda adalah membuat daftar kasus uji yang komprehensif. Kelompokkan kasus uji ke dalam tiga kategori:

    1.  **Skenario Normal (Happy Path):** Uji coba untuk alur kerja yang diharapkan dan berhasil.
    2.  **Skenario Negatif:** Uji coba untuk input yang salah atau tindakan pengguna yang tidak valid.
    3.  **Kasus Tepi (Edge Cases):** Uji coba untuk kondisi-kondisi ekstrem atau yang jarang terjadi.

    Sajikan hasilnya dalam format Markdown, menggunakan sub-judul untuk setiap kategori dan daftar poin untuk setiap kasus uji.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan daftar kasus uji yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Fitur Aplikasi yang Akan Diuji:" dengan:**
    `Sebuah halaman login dengan kolom input untuk email dan password, serta sebuah tombol "Login". Email harus dalam format yang valid. Password harus minimal 8 karakter.`
---