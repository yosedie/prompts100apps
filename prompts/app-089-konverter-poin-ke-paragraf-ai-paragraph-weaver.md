## Nama Aplikasi
Konverter Poin ke Paragraf AI: Paragraph Weaver

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang mengubah daftar poin-poin (bullet points) mentah menjadi sebuah paragraf naratif yang kohesif dan mengalir lancar. Pengguna cukup menempelkan daftar poin, dan AI akan menyusunnya menjadi teks yang enak dibaca.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Konverter Poin ke Paragraf AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Daftar Poin-Poin Anda di Sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ubah Jadi Paragraf". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun...".
4.  **Area Output:**
    *   Judul (H3): "Paragraf yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh paragraf.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan daftar poin dan mengklik tombol "Ubah Jadi Paragraf".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang editor dan penulis yang ahli dalam menciptakan teks yang mengalir lancar dan kohesif.

    Berdasarkan daftar poin-poin berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah mengubah daftar poin ini menjadi SATU paragraf naratif yang terstruktur dengan baik.
    - Gunakan kalimat transisi untuk menghubungkan setiap poin secara logis.
    - Jangan hanya mengubah setiap poin menjadi kalimat, tetapi rangkailah menjadi sebuah cerita atau penjelasan yang utuh.
    - Pastikan hasilnya adalah paragraf yang enak dibaca.

    PENTING: Hanya berikan hasil paragrafnya saja, tanpa tambahan komentar.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan paragraf yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Daftar Poin-Poin Anda di Sini:" dengan:**
    `- Proyek ini bertujuan meningkatkan efisiensi.
    - Fitur utamanya adalah otomatisasi laporan bulanan.
    - Target pengguna adalah manajer departemen.
    - Diharapkan bisa mengurangi waktu kerja manual hingga 40%.`
---