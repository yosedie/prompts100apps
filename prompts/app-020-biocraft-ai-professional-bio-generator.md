## Nama Aplikasi
BioCraft AI: Professional Bio Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu para profesional menulis bio yang menarik untuk profil LinkedIn, portofolio, atau website pribadi. Pengguna memasukkan peran, keahlian, dan pencapaian mereka dalam bentuk poin, dan AI akan menyusunnya menjadi sebuah bio naratif yang singkat dan berdampak.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "BioCraft AI".
2.  **Form Input Pengguna:**
    *   **Input Peran/Jabatan:** Sebuah kolom input teks dengan label "Peran/Jabatan Anda Saat Ini:".
    *   **Input Keahlian:** Sebuah area teks (textarea) dengan label "Keahlian Utama Anda (pisahkan dengan koma):".
    *   **Input Pencapaian:** Sebuah area teks (textarea) dengan label "Pencapaian Penting Anda (satu per baris):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Bio Profesional". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Merangkai Kata...".
4.  **Area Output:**
    *   Judul (H3): "Bio Profesional Anda:"
    *   Sebuah area konten tunggal untuk menampilkan bio yang dihasilkan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##` dan `**`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail profesional mereka dan mengklik tombol "Buat Bio Profesional".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang copywriter ahli dan konsultan personal branding yang berspesialisasi dalam menulis bio profesional.

    Berdasarkan poin-poin berikut:
    - Peran/Jabatan: [Peran dari input pengguna]
    - Keahlian Utama: [Keahlian dari input pengguna]
    - Pencapaian Penting: [Pencapaian dari input pengguna]

    Tugas Anda adalah mengubah poin-poin ini menjadi sebuah bio naratif yang singkat (sekitar 3-4 kalimat), profesional, dan menarik. Bio ini harus menonjolkan nilai dan dampak dari individu tersebut.

    Untuk memberikan pilihan kepada pengguna, buat **DUA versi bio**:
    1.  **Versi Sudut Pandang Orang Pertama (Saya adalah...)**
    2.  **Versi Sudut Pandang Orang Ketiga ([Nama Jabatan] adalah...)**

    Gunakan format Markdown untuk memisahkan kedua versi dengan jelas menggunakan sub-judul.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan kedua versi bio yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Peran/Jabatan Anda Saat Ini:" dengan:**
    `Digital Marketing Manager`
*   **Isi kolom "Keahlian Utama Anda (pisahkan dengan koma):" dengan:**
    `SEO, SEM, Content Strategy, Google Analytics, Email Marketing`
*   **Isi kolom "Pencapaian Penting Anda (satu per baris):" dengan:**
    `- Meningkatkan traffic organik website sebesar 150% dalam satu tahun.
    - Mengelola kampanye iklan digital dengan budget lebih dari $50,000.
    - Memimpin tim konten yang memenangkan penghargaan 'Best Content Marketing 2023'.`
---