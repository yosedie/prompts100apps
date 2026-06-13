## Nama Aplikasi
Surat Lamaran Pro AI: Cover Letter Writer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang secara otomatis membuat surat lamaran kerja (cover letter) yang dipersonalisasi. Pengguna menempelkan deskripsi pekerjaan dan CV mereka, lalu AI akan menulis draf surat lamaran yang menyoroti pengalaman paling relevan dari CV untuk posisi yang dituju.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Surat Lamaran Pro AI".
2.  **Form Input Pengguna:**
    *   **Input Deskripsi Pekerjaan:** Sebuah area teks (textarea) dengan label "Tempelkan Deskripsi Pekerjaan di Sini:".
    *   **Input CV:** Sebuah area teks (textarea) yang besar dengan label "Tempelkan CV atau Ringkasan Pengalaman Anda di Sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Surat Lamaran". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menulis...".
4.  **Area Output:**
    *   Judul (H3): "Draf Surat Lamaran Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh surat.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan deskripsi pekerjaan dan CV, lalu mengklik tombol "Buat Surat Lamaran".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang konsultan karir dan penulis profesional yang ahli dalam membuat surat lamaran kerja yang persuasif.

    Berdasarkan dua dokumen berikut:
    1.  Deskripsi Pekerjaan: """[Teks dari input deskripsi pekerjaan]"""
    2.  CV Pelamar: """[Teks dari input CV]"""

    Tugas Anda adalah menulis draf surat lamaran kerja yang kuat dan dipersonalisasi. Surat lamaran harus:
    - Ditujukan untuk posisi yang spesifik dalam deskripsi pekerjaan.
    - Menyoroti 2-3 pengalaman atau keahlian paling relevan dari CV yang cocok dengan persyaratan di deskripsi pekerjaan.
    - Menggunakan bahasa yang profesional dan antusias.
    - Memiliki struktur standar: paragraf pembuka, paragraf isi yang menyoroti kecocokan, dan paragraf penutup dengan call-to-action.

    Gunakan placeholder seperti `[Nama Anda]` atau `[Nama Manajer Perekrutan]` jika informasi tersebut tidak tersedia.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan draf surat lamaran di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Deskripsi Pekerjaan di Sini:" dengan:**
    `Dicari: Social Media Manager. Tanggung jawab termasuk mengelola semua akun media sosial perusahaan, membuat kalender konten, dan menganalisis metrik engagement. Wajib memiliki pengalaman minimal 2 tahun dalam mengelola kampanye media sosial dan familiar dengan alat analisis seperti Hootsuite.`
*   **Isi kolom "Tempelkan CV atau Ringkasan Pengalaman Anda di Sini:" dengan:**
    `Budi Santoso - Spesialis Pemasaran Digital

    Pengalaman:
    - Social Media Specialist di PT. Maju Jaya (2021-Sekarang)
      - Mengelola akun Instagram & TikTok, meningkatkan followers sebesar 50%.
      - Membuat dan menjadwalkan konten harian menggunakan Hootsuite.
      - Melaporkan performa kampanye bulanan.
    - Marketing Intern di Agensi Kreatif (2020)
      - Membantu riset konten dan copywriting.

    Keahlian: Copywriting, Hootsuite, Analisis Data, SEO Dasar.`
---