## Nama Aplikasi
SloganGen AI: Campaign Slogan Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai generator slogan kampanye. Pengguna mendeskripsikan tujuan utama dan target audiens dari kampanye mereka, lalu AI akan menghasilkan beberapa opsi slogan yang menarik, ringkas, dan mudah diingat.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "SloganGen AI".
2.  **Form Input Pengguna:**
    *   **Input Tujuan Kampanye:** Sebuah area teks (textarea) dengan label "Apa Tujuan Utama Kampanye Anda?".
    *   **Input Target Audiens:** Sebuah kolom input teks dengan label "Siapa Target Audiens Utama Anda?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Slogan!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Brainstorming...".
4.  **Area Output:**
    *   Judul (H3): "5 Opsi Slogan Kampanye:"
    *   Sebuah area konten tunggal untuk menampilkan 5 slogan dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail kampanye dan mengklik tombol "Buat Slogan!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang copywriter senior dan ahli branding yang berspesialisasi dalam menciptakan slogan kampanye yang kuat dan berkesan.

    Berdasarkan informasi kampanye berikut:
    - Tujuan Utama: """[Tujuan dari input pengguna]"""
    - Target Audiens: """[Audiens dari input pengguna]"""

    Tugas Anda adalah membuat **5 opsi slogan** yang berbeda. Setiap slogan harus:
    - Ringkas (idealnya 3-7 kata).
    - Mudah diingat dan diucapkan.
    - Menarik secara emosional atau rasional bagi target audiens.
    - Mencerminkan tujuan utama kampanye.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 5 opsi slogan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Tujuan Utama Kampanye Anda?" dengan:**
    `Mendorong masyarakat untuk mengurangi penggunaan plastik sekali pakai dan beralih ke alternatif yang lebih ramah lingkungan.`
*   **Isi kolom "Siapa Target Audiens Utama Anda?" dengan:**
    `Anak muda dan keluarga yang peduli terhadap lingkungan.`
---