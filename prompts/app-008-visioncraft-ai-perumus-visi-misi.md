## Nama Aplikasi
VisionCraft AI: Perumus Visi & Misi

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web strategis yang membantu para pemimpin bisnis merumuskan pernyataan Visi dan Misi yang kuat. Pengguna memasukkan nilai-nilai inti dan tujuan bisnis perusahaan mereka, dan AI akan menyusun draf pernyataan Visi yang inspiratif dan Misi yang ringkas serta dapat ditindaklanjuti.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "VisionCraft AI".
2.  **Form Input Pengguna:**
    *   **Input Nilai Inti:** Sebuah area teks (textarea) dengan label "Apa Nilai-Nilai Inti Perusahaan Anda? (pisahkan dengan koma)".
    *   **Input Tujuan Bisnis:** Sebuah area teks (textarea) dengan label "Jelaskan Tujuan Utama Bisnis Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Rumuskan Visi & Misi". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Merumuskan...".
4.  **Area Output:** Dibagi menjadi dua bagian yang jelas:
    *   **Bagian Visi:** Judul (H3) "Pernyataan Visi (Vision Statement)" diikuti area konten untuk menampilkan draf visi. Harus ada tombol "Salin" di sebelahnya.
    *   **Bagian Misi:** Judul (H3) "Pernyataan Misi (Mission Statement)" diikuti area konten untuk menampilkan draf misi. Harus ada tombol "Salin" di sebelahnya.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah sintaks Markdown (jika ada) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada kedua bagian di Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi nilai-nilai inti dan tujuan bisnis, lalu mengklik tombol "Rumuskan Visi & Misi".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang konsultan strategi bisnis dan branding yang ahli dalam merumuskan identitas perusahaan.

    Berdasarkan informasi berikut:
    - Nilai-Nilai Inti Perusahaan: [Nilai-nilai dari input pengguna]
    - Tujuan Utama Bisnis: [Tujuan dari input pengguna]

    Tugas Anda adalah membuat DUA pernyataan terpisah:

    1.  **Pernyataan Visi:** Sebuah kalimat yang inspiratif, berorientasi ke masa depan, dan menggambarkan dampak besar yang ingin dicapai perusahaan.
    2.  **Pernyataan Misi:** Sebuah kalimat yang ringkas, jelas, dan berorientasi pada tindakan, yang menjelaskan apa yang dilakukan perusahaan, untuk siapa, dan bagaimana caranya untuk mencapai visi tersebut.

    Pastikan kedua pernyataan tersebut selaras dengan nilai dan tujuan yang diberikan. Sajikan hasilnya dengan jelas, dipisahkan oleh judul. Gunakan format Markdown untuk judul.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi mem-parsingnya untuk memisahkan Visi dan Misi.
5.  Aplikasi merender konten Markdown dari setiap bagian menjadi HTML, lalu menampilkannya di area output yang sesuai.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Nilai-Nilai Inti Perusahaan Anda?..." dengan:**
    `Inovasi, Keberlanjutan, Pemberdayaan Komunitas Lokal`
*   **Isi kolom "Jelaskan Tujuan Utama Bisnis Anda:" dengan:**
    `Menjadi platform e-commerce terdepan untuk produk kerajinan tangan ramah lingkungan di Asia Tenggara dan membantu pengrajin kecil menjangkau pasar global.`
---