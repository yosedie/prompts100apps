## Nama Aplikasi
Generator Afirmasi Harian AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pembuat afirmasi positif yang personal. Pengguna menuliskan tujuan, fokus, atau tantangan yang mereka hadapi hari itu, dan AI akan membuat sebuah kalimat afirmasi yang spesifik, memberdayakan, dan siap untuk diucapkan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Generator Afirmasi Harian AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) dengan label "Apa Fokus atau Tantangan Anda Hari Ini?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Afirmasi Saya". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Kekuatan...".
4.  **Area Output:**
    *   Judul (H3): "Afirmasi Anda untuk Hari Ini:"
    *   Sebuah area konten tunggal untuk menampilkan afirmasi. Desainnya bisa dibuat menonjol seperti kartu kutipan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan fokus/tantangan dan mengklik tombol "Buat Afirmasi Saya".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pelatih mindfulness dan ahli dalam psikologi positif. Anda mampu merumuskan kalimat yang memberdayakan.

    Berdasarkan fokus atau tantangan pengguna berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah mengubah input tersebut menjadi SATU kalimat afirmasi positif yang kuat. Afirmasi harus:
    - Ditulis dari sudut pandang orang pertama ("Saya...").
    - Bersifat aktif dan berorientasi pada tindakan.
    - Mengubah tantangan menjadi pernyataan kekuatan.
    - Spesifik dan relevan dengan input pengguna.

    PENTING: Hanya berikan kalimat afirmasinya saja, tanpa tambahan komentar atau penjelasan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan afirmasi yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Fokus atau Tantangan Anda Hari Ini?" dengan:**
    `Saya ada presentasi penting di depan klien dan merasa sangat gugup.`
---