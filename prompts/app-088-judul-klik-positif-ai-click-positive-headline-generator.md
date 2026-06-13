## Nama Aplikasi
Judul Klik-Positif AI: Click-Positive Headline Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu penulis dan kreator konten membuat judul yang menarik perhatian tanpa menjadi clickbait yang menipu. Pengguna memasukkan topik atau judul asli, dan AI akan menghasilkan 5 alternatif judul "klik-positif" yang memancing rasa penasaran namun tetap akurat.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Judul Klik-Positif AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Topik atau Judul Asli Artikel/Video Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Judul Menarik!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Brainstorming...".
4.  **Area Output:**
    *   Judul (H3): "5 Alternatif Judul Klik-Positif:"
    *   Sebuah area konten tunggal untuk menampilkan 5 judul dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan topik/judul dan mengklik tombol "Buat Judul Menarik!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli strategi konten digital dan copywriter viral. Anda memahami psikologi di balik judul yang membuat orang mengklik, tetapi Anda juga menjunjung tinggi etika dan akurasi.

    Berdasarkan topik atau judul asli berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah membuat **5 alternatif judul "klik-positif"**. Judul-judul ini harus:
    - Menarik perhatian dan memancing rasa penasaran.
    - Menggunakan angka, pertanyaan, atau kata-kata pemicu emosi positif.
    - Tetap akurat dan tidak menjanjikan sesuatu yang tidak ada di dalam konten.
    - Menghindari gaya clickbait yang menipu (contoh: "Anda tidak akan percaya apa yang terjadi selanjutnya!").

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 5 alternatif judul di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Topik atau Judul Asli Artikel/Video Anda:" dengan:**
    `Manfaat Minum Air Putih`
---