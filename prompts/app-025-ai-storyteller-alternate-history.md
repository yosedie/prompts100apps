## Nama Aplikasi
AI Storyteller: Alternate History

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web naratif yang menceritakan kembali peristiwa sejarah dari sudut pandang yang tidak biasa. Pengguna memasukkan sebuah peristiwa sejarah dan perspektif unik, lalu AI akan menulis sebuah cerita pendek yang imersif dari sudut pandang tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Guru Sejarah Alternatif".
2.  **Form Input Pengguna:**
    *   **Input Peristiwa Sejarah:** Sebuah kolom input teks dengan label "Peristiwa Sejarah:".
    *   **Input Sudut Pandang:** Sebuah kolom input teks dengan label "Ceritakan dari Sudut Pandang (contoh: seorang juru masak, seekor merpati pos):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ceritakan Kisahnya!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menelusuri Arsip...".
4.  **Area Output:**
    *   Judul (H3): "Kisah dari Sudut Pandang Lain:"
    *   Sebuah area konten tunggal untuk menampilkan cerita yang dihasilkan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*` atau paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi peristiwa dan sudut pandang, lalu mengklik tombol "Ceritakan Kisahnya!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang sejarawan naratif dan penulis fiksi sejarah yang ahli. Anda mampu menghidupkan kembali peristiwa sejarah melalui mata orang-orang biasa yang sering terlupakan.

    Berdasarkan informasi berikut:
    - Peristiwa Sejarah: [Peristiwa dari input pengguna]
    - Sudut Pandang: [Sudut pandang dari input pengguna]

    Tugas Anda adalah menulis sebuah cerita pendek naratif (first-person) dari sudut pandang yang diberikan. Cerita harus:
    - Terasa otentik dan imersif.
    - Menggunakan detail sensorik (bau, suara, pemandangan) yang relevan dengan sudut pandang tersebut.
    - Menghubungkan pengalaman pribadi karakter dengan peristiwa sejarah yang lebih besar yang terjadi di sekitarnya.

    Gunakan gaya naratif yang mengalir dan puitis. Gunakan format Markdown untuk penekanan jika diperlukan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan cerita yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Peristiwa Sejarah:" dengan:**
    `Perang Dunia II di Front Timur`
*   **Isi kolom "Ceritakan dari Sudut Pandang..." dengan:**
    `Seorang juru masak di unit tentara`
---