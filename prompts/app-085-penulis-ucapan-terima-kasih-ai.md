## Nama Aplikasi
Penulis Ucapan Terima Kasih AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna menulis ucapan terima kasih yang tulus dan spesifik. Pengguna memasukkan hadiah atau bantuan yang mereka terima dan dari siapa, lalu AI akan menyusun draf ucapan yang personal dan tidak terdengar generik.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Ucapan Terima Kasih AI".
2.  **Form Input Pengguna:**
    *   **Input Hadiah/Bantuan:** Sebuah area teks (textarea) dengan label "Apa yang Anda terima (hadiah/bantuan)?".
    *   **Input Pemberi:** Sebuah kolom input teks dengan label "Dari siapa?".
    *   **Pilihan Gaya:** Sebuah menu dropdown (select) dengan label "Gaya Ucapan:" dan opsi: "Santai & Hangat", "Formal & Profesional".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tulis Ucapan Terima Kasih". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Merangkai Kata...".
4.  **Area Output:**
    *   Judul (H3): "Draf Ucapan Terima Kasih Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh ucapan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail, memilih gaya, dan mengklik tombol "Tulis Ucapan Terima Kasih".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis yang ahli dalam mengekspresikan rasa terima kasih dengan tulus dan spesifik.

    Berdasarkan informasi berikut:
    - Hadiah/Bantuan yang Diterima: """[Teks dari input hadiah/bantuan]"""
    - Pemberi: [Nama dari input pemberi]
    - Gaya yang Diinginkan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah menulis sebuah draf ucapan terima kasih yang singkat. Ucapan harus:
    - Menyebutkan secara spesifik hadiah atau bantuan yang diterima.
    - Menjelaskan secara singkat mengapa hadiah/bantuan tersebut dihargai atau apa dampaknya.
    - Menggunakan nada yang sesuai dengan gaya yang dipilih.

    Gunakan placeholder `[Nama Pemberi]` dan `[Nama Anda]` agar mudah disesuaikan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan draf ucapan terima kasih di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa yang Anda terima (hadiah/bantuan)?" dengan:**
    `Sebuah buku tentang astronomi untuk ulang tahunku. Aku sudah lama menginginkannya!`
*   **Isi kolom "Dari siapa?" dengan:**
    `Tante Rina`
*   **Atur pilihan "Gaya Ucapan:" ke:**
    `Santai & Hangat`
---