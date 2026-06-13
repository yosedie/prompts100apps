## Nama Aplikasi
Penulis Pesan Permintaan Maaf AI: Sincere Apology Writer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna merumuskan pesan permintaan maaf yang tulus dan bertanggung jawab. Pengguna menjelaskan situasi dan kesalahan yang mereka perbuat, dan AI akan menyusun draf permintaan maaf yang menunjukkan penyesalan, mengakui kesalahan, dan mengungkapkan niat untuk memperbaiki.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Pesan Permintaan Maaf AI".
2.  **Form Input Pengguna:**
    *   **Input Situasi:** Sebuah area teks (textarea) dengan label "Jelaskan Situasi & Kesalahan Anda:".
    *   **Input Penerima:** Sebuah kolom input teks dengan label "Kepada Siapa Permintaan Maaf Ini Ditujukan?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Susun Permintaan Maaf". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Merangkai Kata...".
4.  **Area Output:**
    *   Judul (H3): "Draf Pesan Permintaan Maaf Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh pesan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail situasi dan mengklik tombol "Susun Permintaan Maaf".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli komunikasi interpersonal dan mediator yang sangat empatik. Anda memahami cara merumuskan permintaan maaf yang tulus dan efektif.

    Berdasarkan situasi berikut:
    - Situasi & Kesalahan: """[Teks dari input situasi]"""
    - Ditujukan Kepada: [Teks dari input penerima]

    Tugas Anda adalah menulis sebuah draf pesan permintaan maaf yang bertanggung jawab. Pesan harus mengikuti struktur:
    1.  **Akui Kesalahan:** Mulai dengan mengakui kesalahan secara spesifik tanpa membuat alasan.
    2.  **Tunjukkan Penyesalan & Empati:** Jelaskan bahwa Anda memahami dampak negatif dari tindakan Anda terhadap perasaan mereka.
    3.  **Ambil Tanggung Jawab:** Nyatakan bahwa itu adalah kesalahan Anda.
    4.  **Tawarkan Perbaikan (jika memungkinkan):** Sebutkan niat Anda untuk memperbaiki situasi atau untuk tidak mengulanginya lagi.

    Gunakan placeholder `[Nama Penerima]` dan `[Nama Anda]` agar mudah disesuaikan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan draf permintaan maaf di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Situasi & Kesalahan Anda:" dengan:**
    `Saya lupa ulang tahun sahabat saya kemarin. Saya benar-benar sibuk dengan pekerjaan dan baru ingat hari ini. Dia pasti merasa sedih dan tidak dipedulikan.`
*   **Isi kolom "Kepada Siapa Permintaan Maaf Ini Ditujukan?" dengan:**
    `Sahabat saya, Rina`
---