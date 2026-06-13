## Nama Aplikasi
Mediator Konflik AI: Neutral Ground

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai mediator konflik virtual yang netral. Pengguna mendeskripsikan sebuah masalah atau perselisihan dari dua sudut pandang yang berbeda, dan AI akan memberikan analisis objektif, mengidentifikasi inti masalah, dan menyarankan langkah-langkah komunikasi untuk mencapai resolusi.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Mediator Konflik AI".
2.  **Form Input Pengguna:**
    *   **Input Sudut Pandang A:** Sebuah area teks (textarea) dengan label "Deskripsikan Masalah dari Sudut Pandang Pihak A:".
    *   **Input Sudut Pandang B:** Sebuah area teks (textarea) dengan label "Deskripsikan Masalah dari Sudut Pandang Pihak B:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Cari Jalan Tengah". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Analisis & Saran Mediasi:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh analisis.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi deskripsi dari kedua sudut pandang dan mengklik tombol "Cari Jalan Tengah".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang mediator konflik profesional yang netral, empatik, dan sangat objektif.

    Berikut adalah deskripsi sebuah perselisihan dari dua sudut pandang yang berbeda:
    - Sudut Pandang Pihak A: """[Teks dari input A]"""
    - Sudut Pandang Pihak B: """[Teks dari input B]"""

    Tugas Anda adalah menganalisis konflik ini dan memberikan panduan untuk resolusi. Analisis Anda harus mencakup:

    1.  **Analisis Objektif:** Rangkum situasi secara netral tanpa memihak. Identifikasi apa inti masalah sebenarnya di luar emosi yang diungkapkan.
    2.  **Validasi Kedua Pihak:** Tulis satu kalimat yang memvalidasi perasaan atau perspektif Pihak A, dan satu kalimat untuk Pihak B.
    3.  **Saran Langkah Komunikasi:** Berikan saran langkah-demi-langkah yang konkret tentang bagaimana kedua pihak bisa memulai percakapan yang produktif. Sarankan kalimat pembuka yang bisa mereka gunakan.

    Gunakan format Markdown untuk menyusun analisis dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan analisis mediasi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Deskripsikan Masalah dari Sudut Pandang Pihak A:" dengan:**
    `Saya merasa rekan kerja saya, Budi, selalu menyerahkan pekerjaannya di menit-menit terakhir. Ini membuat saya harus terburu-buru dan sering lembur untuk menyelesaikan bagian saya yang bergantung pada pekerjaannya. Saya merasa tidak dihargai.`
*   **Isi kolom "Deskripsikan Masalah dari Sudut Pandang Pihak B:" dengan:**
    `Saya merasa Anita terlalu banyak menuntut dan tidak mengerti bahwa saya menangani beberapa proyek sekaligus. Saya selalu menyelesaikan pekerjaan sebelum deadline, tapi dia terus-menerus menanyakan progres dan membuat saya merasa tertekan.`
---