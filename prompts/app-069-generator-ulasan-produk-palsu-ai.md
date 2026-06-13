## Nama Aplikasi
Generator Ulasan Produk Palsu AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang menghasilkan ulasan produk palsu yang detail dan terdengar otentik untuk tujuan pengujian atau contoh. Pengguna memasukkan nama produk dan memilih sentimen, lalu AI akan menulis sebuah ulasan lengkap seolah-olah dari pelanggan sungguhan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Generator Ulasan Produk Palsu AI".
2.  **Form Input Pengguna:**
    *   **Input Nama Produk:** Sebuah kolom input teks dengan label "Nama Produk Fiktif:".
    *   **Pilihan Sentimen:** Sebuah menu dropdown (select) dengan label "Pilih Sentimen Ulasan:" dan opsi: "Positif (5 Bintang)", "Negatif (1 Bintang)", "Seimbang (3 Bintang)".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tulis Ulasan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menulis...".
4.  **Area Output:**
    *   Judul (H3): "Ulasan Produk yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh ulasan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama produk, memilih sentimen, dan mengklik tombol "Tulis Ulasan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis yang sangat pandai meniru gaya tulisan ulasan produk online. Anda bisa menulis ulasan yang terdengar sangat otentik dan detail.

    Berdasarkan informasi berikut:
    - Nama Produk: [Nama produk dari input pengguna]
    - Sentimen yang Diinginkan: [Sentimen dari pilihan pengguna]

    Tugas Anda adalah menulis SATU ulasan produk palsu yang detail. Ulasan harus memiliki:
    - **Judul Ulasan:** Sebuah judul yang menarik dan sesuai dengan sentimen.
    - **Isi Ulasan:** Beberapa paragraf yang menjelaskan pengalaman "pengguna". Sebutkan detail spesifik (baik atau buruk) tentang fitur, desain, atau penggunaan produk.
    - **Rating Bintang:** Tampilkan rating bintang yang sesuai di akhir (misal: ★★★★★ untuk positif).

    Pastikan gaya bahasa dan detailnya cocok dengan sentimen yang diminta.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan ulasan produk di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Produk Fiktif:" dengan:**
    `Headphone Kedap Suara "AuraSound Pro"`
*   **Atur pilihan "Pilih Sentimen Ulasan:" ke:**
    `Positif (5 Bintang)`
---