## Nama Aplikasi
Asisten Negosiasi Gaji AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pelatih negosiasi gaji. Pengguna memasukkan data tentang posisi, industri, dan pencapaian mereka, lalu AI akan menghasilkan poin-poin argumen yang kuat dan frasa-frasa kunci yang bisa langsung digunakan dalam percakapan negosiasi.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Asisten Negosiasi Gaji AI".
2.  **Form Input Pengguna:**
    *   **Input Posisi:** Sebuah kolom input teks dengan label "Posisi/Jabatan Anda:".
    *   **Input Industri:** Sebuah kolom input teks dengan label "Industri Perusahaan:".
    *   **Input Pencapaian:** Sebuah area teks (textarea) dengan label "Sebutkan 2-3 Pencapaian Kuantitatif Terbaik Anda:". Berikan placeholder seperti "Contoh: Meningkatkan penjualan sebesar 20%, Mengurangi biaya operasional 15%".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Siapkan Argumen Saya". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mempersiapkan...".
4.  **Area Output:**
    *   Judul (H3): "Poin & Frasa Kunci untuk Negosiasi:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh panduan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail posisi dan pencapaian, lalu mengklik tombol "Siapkan Argumen Saya".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang negosiator ulung dan konsultan karir yang ahli dalam strategi negosiasi gaji.

    Berdasarkan profil pengguna berikut:
    - Posisi: [Posisi dari input pengguna]
    - Industri: [Industri dari input pengguna]
    - Pencapaian: """[Pencapaian dari input pengguna]"""

    Tugas Anda adalah membuat panduan negosiasi yang ringkas dan kuat. Panduan harus mencakup:

    1.  **Riset Pasar (Pembuka):** Sebuah kalimat pembuka yang menunjukkan bahwa pengguna telah melakukan riset, berdasarkan posisi dan industrinya.
    2.  **Poin Argumen Berbasis Nilai:** Ubah setiap pencapaian yang diberikan menjadi poin argumen yang kuat, menghubungkan kontribusi masa lalu dengan nilai masa depan bagi perusahaan.
    3.  **Frasa Kunci yang Bisa Digunakan:** Berikan beberapa contoh frasa diplomatis untuk digunakan saat mengajukan permintaan, menanggapi tawaran, atau saat hening.

    Gunakan format Markdown untuk menyusun panduan dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan panduan negosiasi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Posisi/Jabatan Anda:" dengan:**
    `Senior Software Engineer`
*   **Isi kolom "Industri Perusahaan:" dengan:**
    `Teknologi Finansial (Fintech)`
*   **Isi kolom "Sebutkan 2-3 Pencapaian Kuantitatif Terbaik Anda:" dengan:**
    `- Memimpin proyek yang meningkatkan kecepatan loading aplikasi sebesar 30%.
    - Mengurangi bug kritis di produksi sebesar 50% melalui implementasi unit testing yang lebih baik.`
---