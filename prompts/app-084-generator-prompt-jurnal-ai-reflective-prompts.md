## Nama Aplikasi
Generator Prompt Jurnal AI: Reflective Prompts

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web sederhana yang berfungsi sebagai pemicu untuk journaling. Pengguna memasukkan satu kata yang menggambarkan perasaan mereka hari ini, dan AI akan menghasilkan 5 pertanyaan jurnal yang mendalam dan introspektif untuk membantu pengguna merefleksikan dan memahami perasaan tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Generator Prompt Jurnal AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Satu Kata yang Menggambarkan Perasaanmu Hari Ini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Beri Saya Prompt Jurnal". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Pertanyaan...".
4.  **Area Output:**
    *   Judul (H3): "5 Prompt Jurnal Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan 5 pertanyaan dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan satu kata perasaan dan mengklik tombol "Beri Saya Prompt Jurnal".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang terapis dan pemandu jurnal (journaling facilitator) yang bijaksana. Anda ahli dalam membuat pertanyaan yang menggugah pikiran untuk refleksi diri.

    Berdasarkan satu kata perasaan dari pengguna berikut:
    """
    [Kata dari input pengguna]
    """

    Tugas Anda adalah membuat **5 pertanyaan jurnal yang mendalam**. Pertanyaan-pertanyaan ini harus membantu pengguna untuk:
    - Mengeksplorasi akar dari perasaan tersebut.
    - Memahami bagaimana perasaan itu bermanifestasi dalam tubuh dan pikiran mereka.
    - Menemukan apa yang bisa mereka pelajari dari perasaan itu.
    - Mempertimbangkan tindakan apa yang bisa diambil (jika perlu).

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 5 prompt jurnal di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Satu Kata yang Menggambarkan Perasaanmu Hari Ini:" dengan:**
    `Lelah`
---