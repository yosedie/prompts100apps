## Nama Aplikasi
Perekrut AI: Penulis Deskripsi Jabatan

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang secara otomatis membuat deskripsi lowongan kerja yang lengkap dan menarik. Pengguna hanya perlu memasukkan nama posisi dan tiga tanggung jawab utama, dan AI akan menyusun sisanya, termasuk ringkasan posisi, kualifikasi yang dibutuhkan, dan apa yang ditawarkan perusahaan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Perekrut AI".
2.  **Form Input Pengguna:**
    *   **Input Nama Posisi:** Sebuah kolom input teks dengan label "Nama Posisi:".
    *   **Input Tanggung Jawab:** Tiga kolom input teks terpisah:
        *   "Tanggung Jawab Utama 1:"
        *   "Tanggung Jawab Utama 2:"
        *   "Tanggung Jawab Utama 3:"
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Deskripsi Jabatan". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menyusun...".
4.  **Area Output:**
    *   Judul (H3): "Deskripsi Lowongan Kerja:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh deskripsi yang dihasilkan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi nama posisi dan tiga tanggung jawab, lalu mengklik tombol "Buat Deskripsi Jabatan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang Manajer Perekrutan (Hiring Manager) dan copywriter ahli yang berspesialisasi dalam membuat deskripsi lowongan kerja yang menarik bagi talenta terbaik.

    Berdasarkan informasi singkat berikut:
    - Nama Posisi: [Nama Posisi dari input pengguna]
    - Tanggung Jawab Utama 1: [Teks dari input 1]
    - Tanggung Jawab Utama 2: [Teks dari input 2]
    - Tanggung Jawab Utama 3: [Teks dari input 3]

    Tugas Anda adalah mengubah informasi singkat ini menjadi deskripsi lowongan kerja yang lengkap, profesional, dan menarik. Deskripsi harus mencakup bagian-bagian berikut:
    - Ringkasan Posisi
    - Tanggung Jawab Utama (gunakan 3 poin yang diberikan)
    - Kualifikasi yang Dibutuhkan (simpulkan kualifikasi teknis dan non-teknis yang paling relevan dari nama posisi dan tanggung jawab)
    - Kualifikasi Tambahan (Nilai Plus)
    - Apa yang Kami Tawarkan (buat daftar penawaran standar yang menarik seperti gaji kompetitif, lingkungan kerja kolaboratif, dll.)

    Gunakan format Markdown untuk kejelasan, termasuk judul, sub-judul, dan daftar poin.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan deskripsi jabatan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Posisi:" dengan:**
    `Senior Frontend Developer`
*   **Isi kolom "Tanggung Jawab Utama 1:" dengan:**
    `Mengembangkan dan memelihara antarmuka pengguna (UI) aplikasi web kami.`
*   **Isi kolom "Tanggung Jawab Utama 2:" dengan:**
    `Berkolaborasi dengan tim backend dan desainer UI/UX.`
*   **Isi kolom "Tanggung Jawab Utama 3:" dengan:**
    `Mengoptimalkan aplikasi untuk kecepatan dan skalabilitas maksimum.`
---