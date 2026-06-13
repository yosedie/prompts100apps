## Nama Aplikasi
Project Codename Generator AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para developer dan manajer proyek yang memberikan ide-ide nama kode (codename) yang kreatif. Pengguna memasukkan deskripsi singkat tentang tujuan proyek, dan AI akan menghasilkan 10 ide nama kode yang unik dan tematik.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Project Codename Generator AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) dengan label "Jelaskan Tujuan Utama Proyek Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate Codenames!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Brainstorming...".
4.  **Area Output:**
    *   Judul (H3): "10 Ide Nama Kode Proyek:"
    *   Sebuah area konten tunggal untuk menampilkan 10 nama dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi proyek dan mengklik tombol "Generate Codenames!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang manajer produk di sebuah laboratorium inovasi rahasia (skunkworks). Anda ahli dalam memberikan nama kode yang keren, misterius, dan tematik untuk proyek-proyek baru.

    Berdasarkan deskripsi tujuan proyek berikut:
    """
    [Deskripsi dari input pengguna]
    """

    Tugas Anda adalah membuat **10 ide nama kode (codename)** yang unik. Nama-nama ini harus:
    - Terdiri dari satu atau dua kata.
    - Terdengar keren dan profesional.
    - Secara tematis berhubungan dengan tujuan proyek (misalnya, proyek tentang kecepatan bisa dinamai 'Project Velocity' atau 'Project Cheetah').

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 10 ide nama kode di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Tujuan Utama Proyek Anda:" dengan:**
    `Sebuah proyek rahasia untuk membangun ulang website perusahaan dari awal dengan teknologi terbaru, dengan fokus pada kecepatan dan pengalaman pengguna yang modern.`
---