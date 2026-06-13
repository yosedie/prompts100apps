## Nama Aplikasi
Peningkat Prompt Gambar AI: Prompt Enhancer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna menulis prompt yang lebih baik untuk generator gambar AI (seperti Midjourney atau Stable Diffusion). Pengguna memasukkan ide prompt yang sederhana, dan AI akan mengembangkannya menjadi prompt yang sangat detail, menambahkan elemen-elemen seperti gaya seni, pencahayaan, komposisi, dan detail teknis lainnya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Peningkat Prompt Gambar AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Ide Prompt Sederhana Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tingkatkan Prompt!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menambahkan Detail...".
4.  **Area Output:**
    *   Judul (H3): "Prompt yang Ditingkatkan:"
    *   Sebuah area konten tunggal untuk menampilkan prompt yang detail.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan prompt sederhana dan mengklik tombol "Tingkatkan Prompt!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang 'prompt engineer' dan seniman digital yang sangat ahli. Anda tahu persis kata kunci apa yang harus digunakan untuk mendapatkan hasil terbaik dari model generator gambar AI.

    Berdasarkan ide prompt sederhana berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menulis ulang prompt ini menjadi versi yang sangat detail dan kaya. Tambahkan elemen-elemen berikut untuk memperkaya prompt:
    - **Subjek & Aksi:** Deskripsikan subjek dan apa yang dilakukannya dengan lebih detail.
    - **Gaya Seni (Art Style):** Sebutkan gaya seni yang spesifik (misal: 'digital painting', 'cyberpunk', 'fantasy concept art').
    - **Pencahayaan (Lighting):** Deskripsikan pencahayaan (misal: 'cinematic lighting', 'soft volumetric light', 'neon glow').
    - **Komposisi & Detail:** Tambahkan detail tentang lingkungan, warna, dan komposisi gambar.
    - **Parameter Teknis:** Akhiri dengan beberapa parameter teknis yang umum digunakan (misal: `--ar 16:9 --v 6.0`).

    PENTING: Gabungkan semua elemen ini menjadi satu paragraf teks yang siap disalin, bukan dalam bentuk daftar.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan prompt yang ditingkatkan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Ide Prompt Sederhana Anda:" dengan:**
    `astronot di hutan`
---