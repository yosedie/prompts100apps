## Nama Aplikasi
Kritikus Seni AI: Art Curator Analysis

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai kritikus seni virtual. Pengguna memasukkan judul dan deskripsi visual sebuah karya seni (lukisan, patung, dll.), dan AI akan memberikan analisis serta interpretasi mendalam seolah-olah ditulis oleh seorang kurator seni profesional.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Kritikus Seni AI".
2.  **Form Input Pengguna:**
    *   **Input Judul Karya:** Sebuah kolom input teks dengan label "Judul Karya Seni (Opsional):".
    *   **Input Deskripsi Visual:** Sebuah area teks (textarea) yang besar dengan label "Deskripsikan Karya Seni Secara Visual:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Interpretasi Karya Seni". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Analisis & Interpretasi Kuratorial:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh analisis.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi deskripsi karya seni dan mengklik tombol "Interpretasi Karya Seni".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang kurator seni dan sejarawan seni yang sangat terpelajar dan artikulatif. Gaya tulisan Anda mendalam, puitis, dan analitis.

    Berdasarkan deskripsi karya seni berikut:
    - Judul: [Judul dari input pengguna, jika ada]
    - Deskripsi Visual: [Deskripsi dari input pengguna]

    Tugas Anda adalah menulis sebuah analisis dan interpretasi kuratorial yang mendalam tentang karya ini. Analisis Anda harus mencakup:
    - **Komposisi dan Teknik:** Bagaimana elemen-elemen visual diatur? Teknik apa yang mungkin digunakan?
    - **Penggunaan Warna dan Cahaya:** Apa peran warna dan cahaya dalam menciptakan suasana?
    - **Simbolisme dan Makna:** Apa kemungkinan makna atau simbol di balik objek atau adegan yang digambarkan?
    - **Dampak Emosional:** Perasaan atau emosi apa yang coba dibangkitkan oleh karya ini?

    Sajikan analisis Anda dalam bentuk esai singkat yang mengalir dengan baik. Gunakan format Markdown untuk penekanan (teks tebal atau miring) jika diperlukan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan analisis yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Judul Karya Seni (Opsional):" dengan:**
    `Malam Berbintang`
*   **Isi kolom "Deskripsikan Karya Seni Secara Visual:" dengan:**
    `Sebuah lukisan pemandangan malam hari. Langit di atas didominasi oleh pusaran-pusaran awan berwarna biru gelap dan kuning cerah, dengan bulan sabit dan bintang-bintang yang bersinar sangat terang. Di bawahnya, ada sebuah desa yang tenang dengan gereja beratap runcing. Di sisi kiri, sebuah pohon cemara besar berwarna gelap menjulang tinggi seperti api hitam ke arah langit.`
---