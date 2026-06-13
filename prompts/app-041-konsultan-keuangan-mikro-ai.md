## Nama Aplikasi
Konsultan Keuangan Mikro AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai konsultan keuangan pribadi. Pengguna mendeskripsikan gaya hidup, kebiasaan belanja, dan tujuan finansial mereka, lalu AI akan memberikan serangkaian tips praktis dan dapat ditindaklanjuti untuk menabung dan mengelola keuangan harian.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Konsultan Keuangan Mikro AI".
2.  **Form Input Pengguna:**
    *   **Input Gaya Hidup:** Sebuah area teks (textarea) dengan label "Jelaskan gaya hidup & kebiasaan belanja Anda:".
    *   **Input Tujuan Finansial:** Sebuah area teks (textarea) dengan label "Apa tujuan finansial utama Anda saat ini?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Beri Saya Tips Keuangan". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Tips Keuangan Praktis Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh tips.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail gaya hidup dan tujuan, lalu mengklik tombol "Beri Saya Tips Keuangan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang perencana keuangan pribadi (personal financial planner) yang ramah dan praktis. Anda ahli dalam memberikan saran yang mudah diterapkan, bukan teori yang rumit.

    Berdasarkan profil pengguna berikut:
    - Gaya Hidup & Kebiasaan: [Deskripsi dari input pengguna 1]
    - Tujuan Finansial: [Tujuan dari input pengguna 2]

    Tugas Anda adalah memberikan serangkaian tips keuangan yang personal dan dapat ditindaklanjuti. Kelompokkan tips Anda ke dalam dua kategori:

    1.  **Kebiasaan Harian & Mingguan (Quick Wins):** Berikan tips-tips kecil yang bisa langsung diterapkan untuk mengurangi pengeluaran dan meningkatkan tabungan berdasarkan gaya hidup yang dijelaskan.
    2.  **Strategi Mencapai Tujuan:** Berikan langkah-langkah konkret untuk mencapai tujuan finansial yang spesifik tersebut.

    Gunakan format Markdown untuk menyusun tips dengan rapi (judul, sub-judul, daftar poin).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan tips keuangan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan gaya hidup & kebiasaan belanja Anda:" dengan:**
    `Saya seorang mahasiswa dengan pendapatan tidak tetap dari kerja paruh waktu. Saya sering jajan kopi dan makan di luar karena sibuk dengan jadwal kuliah.`
*   **Isi kolom "Apa tujuan finansial utama Anda saat ini?" dengan:**
    `Ingin menabung untuk membeli laptop baru seharga 10 juta dalam waktu 6 bulan.`
---