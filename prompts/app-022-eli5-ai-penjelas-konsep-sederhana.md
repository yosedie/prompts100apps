## Nama Aplikasi
ELI5 AI: Penjelas Konsep Sederhana

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang dapat menyederhanakan topik yang sangat kompleks. Pengguna memasukkan sebuah subjek yang sulit, dan AI akan menjelaskannya dengan metode "Explain Like I'm 5" (ELI5), menggunakan analogi sederhana, bahasa yang mudah, dan tanpa jargon teknis.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "ELI5 AI: Jelaskan Seperti Aku 5 Tahun".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Topik Kompleks yang Ingin Dijelaskan:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Jadi Gampang!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menyederhanakan...".
4.  **Area Output:**
    *   Judul (H3): "Penjelasan Sederhana:"
    *   Sebuah area konten tunggal untuk menampilkan penjelasan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` atau `*miring*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan topik dan mengklik tombol "Buat Jadi Gampang!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang guru yang sangat sabar dan ahli dalam menyederhanakan konsep-konsep yang rumit untuk anak-anak.

    Berikut adalah topik yang perlu Anda jelaskan:
    """
    [Topik dari input pengguna]
    """

    Tugas Anda adalah menjelaskan topik ini seolah-olah Anda sedang berbicara kepada anak berusia 5 tahun (Explain Like I'm 5).

    Gunakan aturan berikut:
    - Gunakan kalimat yang sangat pendek dan bahasa yang sederhana.
    - Gunakan analogi atau perumpamaan yang mudah dimengerti oleh anak-anak (misalnya, mainan, makanan, hewan, taman bermain).
    - HINDARI jargon teknis sama sekali.
    - Fokus pada ide utamanya, bukan pada detail teknis yang akurat.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan penjelasan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Topik Kompleks yang Ingin Dijelaskan:" dengan:**
    `Blockchain`
---