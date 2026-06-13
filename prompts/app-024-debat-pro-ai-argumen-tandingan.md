## Nama Aplikasi
Debat Pro AI: Argumen Tandingan

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web interaktif yang berfungsi sebagai lawan debat virtual. Pengguna memasukkan sebuah topik, memilih posisi (Pro atau Kontra), dan menulis argumen mereka. AI akan secara otomatis mengambil posisi yang berlawanan dan memberikan argumen tandingan yang logis dan terstruktur untuk melatih kemampuan berdebat pengguna.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Debat Pro AI".
2.  **Form Input Pengguna:**
    *   **Input Topik Debat:** Sebuah kolom input teks dengan label "Topik Debat:".
    *   **Pilihan Posisi:** Sebuah menu dropdown (select) dengan label "Posisi Anda:" dan opsi: "Pro" dan "Kontra".
    *   **Input Argumen:** Sebuah area teks (textarea) yang besar dengan label "Argumen Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Beri Argumen Tandingan!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Memikirkan Sanggahan...".
4.  **Area Output:**
    *   Judul (H3): "Argumen dari Lawan Debat:"
    *   Sebuah area konten tunggal untuk menampilkan argumen tandingan dari AI.
    *   **Instruksi Lanjutan:** Di bawah argumen AI, tampilkan teks instruksi: "*Untuk melanjutkan debat, tulis sanggahan Anda di kolom 'Argumen Anda' di atas dan klik tombol lagi.*"
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan daftar poin) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi topik, posisi, dan argumen awal, lalu mengklik tombol.
2.  Aplikasi menentukan posisi yang harus diambil AI (jika pengguna 'Pro', AI 'Kontra', dan sebaliknya).
3.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli debat yang logis, kritis, dan terstruktur. Anda sangat pandai dalam menemukan kelemahan dalam argumen lawan dan memberikan sanggahan yang kuat.

    Konteks Debat:
    - Topik: [Topik dari input pengguna]
    - Posisi Lawan (Pengguna): [Posisi dari pilihan pengguna]
    - Argumen Lawan (Pengguna): """[Argumen dari input pengguna]"""

    Tugas Anda adalah:
    1.  Ambil posisi yang **BERLAWANAN** dari lawan Anda.
    2.  Berikan argumen tandingan yang kuat dan terstruktur.
    3.  Serang kelemahan, asumsi, atau celah logika dalam argumen lawan.
    4.  Gunakan data, logika, atau contoh untuk mendukung poin Anda.

    PENTING: Hanya berikan argumen tandingan Anda, tanpa kalimat pembuka seperti "Baik, saya akan mengambil posisi kontra...". Langsung saja ke argumennya.
    ```
4.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
5.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
6.  Aplikasi menampilkan argumen tandingan AI di Area Output. Alur ini berulang setiap kali pengguna mengirimkan argumen baru.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Topik Debat:" dengan:**
    `Pekerjaan remote (WFH) lebih baik daripada kerja di kantor.`
*   **Atur pilihan "Posisi Anda:" ke:**
    `Pro`
*   **Isi kolom "Argumen Anda:" dengan:**
    `Pekerjaan remote memberikan fleksibilitas waktu dan menghemat biaya transportasi, sehingga meningkatkan keseimbangan hidup dan kerja (work-life balance) bagi karyawan.`
---