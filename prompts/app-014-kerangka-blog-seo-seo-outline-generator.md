## Nama Aplikasi
Kerangka Blog SEO: SEO Outline Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai perencana konten SEO. Pengguna memasukkan satu kata kunci utama, dan AI akan menghasilkan kerangka artikel blog yang terstruktur (H1, H2, H3) dan dioptimalkan untuk mesin pencari, lengkap dengan saran sub-topik yang relevan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Kerangka Blog SEO".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Kata Kunci Utama Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Kerangka Blog". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis SEO...".
4.  **Area Output:**
    *   Judul (H3): "Kerangka Artikel SEO-Friendly:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh kerangka.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (terutama `H1`, `H2`, `H3`, dan daftar) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan kata kunci dan mengklik tombol "Buat Kerangka Blog".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang Spesialis SEO Konten (Content SEO Specialist) dan ahli strategi digital yang sangat berpengalaman.

    Berdasarkan kata kunci utama berikut:
    """
    [Kata kunci dari input pengguna]
    """

    Tugas Anda adalah membuat kerangka artikel blog yang komprehensif dan SEO-friendly. Kerangka ini harus membantu penulis untuk membuat konten yang mendalam dan berperingkat tinggi di mesin pencari.

    Struktur kerangka harus menggunakan format Markdown hierarkis yang jelas:

    - **H1 (Judul Utama):** Buat satu judul yang menarik, mengandung kata kunci, dan memancing klik.
    - **H2 (Sub-Judul Utama):** Buat beberapa H2 yang mencakup aspek-aspek utama dari topik, menjawab pertanyaan umum (apa, mengapa, bagaimana).
    - **H3 (Poin-Poin Detail):** Di bawah setiap H2, berikan beberapa H3 yang lebih spesifik sebagai poin-poin pembahasan.
    - **Saran Sub-Topik Tambahan:** Di akhir, berikan daftar poin berisi saran kata kunci turunan atau pertanyaan terkait (LSI keywords, People Also Ask) yang bisa dimasukkan ke dalam artikel.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan kerangka yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Kata Kunci Utama Anda:" dengan:**
    `Manfaat kopi untuk kesehatan`
---