## Nama Aplikasi
Podcast Show Notes Generator AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu podcaster membuat deskripsi episode (show notes) yang menarik. Pengguna memasukkan poin-poin kunci atau ringkasan singkat dari episode mereka, dan AI akan menulis deskripsi yang lengkap serta memberikan beberapa usulan judul yang memikat.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Podcast Show Notes Generator AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Masukkan Poin-Poin Kunci atau Ringkasan Episode Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Deskripsi Episode". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mixing Audio...".
4.  **Area Output:**
    *   Judul (H3): "Deskripsi & Judul Episode Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh hasil.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan poin-poin episode dan mengklik tombol "Buat Deskripsi Episode".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang produser podcast dan copywriter yang ahli dalam membuat deskripsi episode yang membuat orang ingin langsung mendengarkan.

    Berdasarkan poin-poin kunci berikut dari sebuah episode podcast:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menghasilkan DUA hal:

    1.  **Usulan Judul Episode:** Berikan 3 opsi judul yang menarik, memancing rasa penasaran, dan mengandung kata kunci utama.
    2.  **Deskripsi Episode (Show Notes):** Tulis deskripsi yang menarik. Mulailah dengan sebuah 'hook' atau pertanyaan, jelaskan secara singkat apa saja yang akan dibahas (berdasarkan poin-poin yang diberikan), dan akhiri dengan ajakan untuk mendengarkan.

    Gunakan format Markdown untuk menyusun hasilnya dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan usulan judul dan deskripsi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Poin-Poin Kunci atau Ringkasan Episode Anda:" dengan:**
    `- Wawancara dengan Dr. Anya, seorang psikolog.
    - Membahas tentang fenomena 'burnout' di kalangan pekerja muda.
    - Tanda-tanda awal burnout yang sering diabaikan.
    - Tiga strategi praktis untuk mencegah dan mengatasi burnout.`
---