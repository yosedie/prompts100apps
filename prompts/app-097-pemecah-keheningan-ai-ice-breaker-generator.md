## Nama Aplikasi
Pemecah Keheningan AI: Ice Breaker Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna memulai percakapan. Pengguna memasukkan konteks sebuah acara sosial, dan AI akan menghasilkan daftar pertanyaan pembuka percakapan (ice breaker) yang unik, menarik, dan sesuai dengan suasana acara tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pemecah Keheningan AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Apa Konteks Acara Sosial Anda?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Beri Saya Ice Breaker!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Topik...".
4.  **Area Output:**
    *   Judul (H3): "5 Pertanyaan Pembuka Percakapan:"
    *   Sebuah area konten tunggal untuk menampilkan 5 pertanyaan dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan konteks acara dan mengklik tombol "Beri Saya Ice Breaker!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli komunikasi sosial dan fasilitator acara yang sangat pandai membuat orang merasa nyaman dan terhubung.

    Berdasarkan konteks acara berikut:
    """
    [Konteks dari input pengguna]
    """

    Tugas Anda adalah membuat **5 pertanyaan pembuka percakapan (ice breaker)** yang bagus. Pertanyaan-pertanyaan ini harus:
    - Sesuai dengan konteks acara yang diberikan.
    - Bersifat terbuka (bukan pertanyaan ya/tidak).
    - Menarik dan tidak terlalu personal atau aneh.
    - Dirancang untuk memicu cerita atau opini, bukan jawaban satu kata.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 5 pertanyaan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Konteks Acara Sosial Anda?" dengan:**
    `Acara networking untuk para profesional di industri teknologi.`
---