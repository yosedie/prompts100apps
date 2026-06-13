## Nama Aplikasi
Cron Job AI Translator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web utilitas yang menerjemahkan deskripsi jadwal dalam bahasa manusia menjadi sintaks cron job yang benar. Pengguna menulis kapan mereka ingin sebuah tugas dijalankan, dan AI akan menghasilkan string cron yang sesuai.

## Komponen Antrimuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Cron Job AI Translator".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Jelaskan Jadwal yang Anda Inginkan:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate Cron Syntax". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menghitung...".
4.  **Area Output:**
    *   Judul (H3): "Sintaks Cron Job Anda:"
    *   Sebuah **area teks read-only** yang didesain seperti blok kode (latar belakang gelap, font monospace) untuk menampilkan string cron.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin" di sebelah area output.
    *   **Area Penjelasan:** Di bawah sintaks cron, sertakan area untuk penjelasan singkat tentang arti setiap bagian dari string cron yang dihasilkan.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Penjelasan.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi jadwal dan mengklik tombol "Generate Cron Syntax".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang System Administrator (SysAdmin) Linux senior yang sangat ahli dalam menjadwalkan tugas menggunakan cron.

    Berdasarkan deskripsi jadwal dalam bahasa manusia berikut:
    """
    [Deskripsi dari input pengguna]
    """

    Tugas Anda adalah menghasilkan DUA hal:
    1.  **Sintaks Cron:** String cron job yang benar (* * * * *) yang sesuai dengan deskripsi.
    2.  **Penjelasan:** Penjelasan singkat untuk setiap bagian dari string cron tersebut (Menit, Jam, Hari dalam Bulan, Bulan, Hari dalam Minggu).

    Gunakan format berikut dengan pemisah yang jelas:
    [String cron job Anda di sini]
    ---EXPLANATION---
    [Penjelasan Anda di sini]
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi mem-parsing teks tersebut menggunakan pemisah `---EXPLANATION---`.
5.  Aplikasi menampilkan string cron di area output utama dan penjelasan yang sudah di-render di bawahnya.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Jadwal yang Anda Inginkan:" dengan:**
    `Jalankan skrip setiap hari Senin jam 5 pagi.`
---