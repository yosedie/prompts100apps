## Nama Aplikasi
Poles Bahasa Pro: Professional Tone Adjuster

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai asisten komunikasi. Pengguna memasukkan draf teks (email, pesan chat, dll.) yang canggung atau terlalu blak-blakan, lalu memilih konteks dan gaya bahasa yang diinginkan. Aplikasi akan menulis ulang teks tersebut menjadi versi yang lebih profesional, persuasif, atau diplomatis.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Poles Bahasa Pro".
2.  **Form Input Pengguna:**
    *   **Input Teks Asli:** Sebuah area teks (textarea) yang besar dengan label "Teks Asli Anda:".
    *   **Input Konteks:** Sebuah kolom input teks dengan label "Apa Tujuan Utama Pesan Ini?".
    *   **Pilihan Gaya Bahasa:** Sebuah menu dropdown (select) dengan label "Pilih Gaya Bahasa yang Diinginkan:" dan opsi berikut:
        *   Profesional & Formal
        *   Persuasif & Ramah
        *   Diplomatis & Tegas
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Poles Teks Sekarang!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Memoles Bahasa...".
4.  **Area Output:**
    *   Judul (H3): "Versi yang Disempurnakan:"
    *   Sebuah area konten (read-only) untuk menampilkan teks yang sudah dipoles.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output untuk memudahkan pengguna.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah sintaks Markdown (jika ada) menjadi elemen HTML yang diformat. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi teks asli, tujuan, dan memilih gaya bahasa, lalu mengklik tombol "Poles Teks Sekarang!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli komunikasi profesional dan editor ahli.

    Berdasarkan informasi berikut:
    - Teks Asli: """[Teks dari input pengguna]"""
    - Konteks/Tujuan: [Tujuan dari input pengguna]
    - Gaya Bahasa yang Diinginkan: [Gaya bahasa dari pilihan pengguna]

    Tugas Anda adalah menulis ulang "Teks Asli" menjadi versi yang jauh lebih baik sesuai dengan konteks dan gaya bahasa yang diinginkan. Perbaiki tata bahasa, hilangkan kalimat yang canggung, dan gunakan kosa kata yang lebih profesional. Pastikan pesan utama tersampaikan dengan jelas dan efektif.

    PENTING: Hanya berikan hasil akhir teks yang sudah dipoles, tanpa tambahan komentar atau penjelasan dari Anda.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown (jika ada) dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan teks yang sudah disempurnakan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Teks Asli Anda:" dengan:**
    `Ini kerjaanmu salah, revisi lagi. Deadline besok jangan telat.`
*   **Isi kolom "Apa Tujuan Utama Pesan Ini?" dengan:**
    `Memberikan feedback revisi kepada rekan kerja dengan cara yang konstruktif.`
*   **Atur pilihan "Pilih Gaya Bahasa yang Diinginkan:" ke:**
    `Profesional & Formal`
---