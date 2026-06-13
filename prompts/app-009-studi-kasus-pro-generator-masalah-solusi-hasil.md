## Nama Aplikasi
Studi Kasus Pro: Generator Masalah-Solusi-Hasil

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang mengubah data mentah atau poin-poin proyek menjadi sebuah studi kasus (case study) yang naratif dan persuasif. Pengguna memasukkan detail proyek, dan AI akan menyusunnya ke dalam struktur "Masalah-Solusi-Hasil" yang terbukti efektif.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Studi Kasus Pro".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Masukkan Poin-Poin atau Data Mentah Proyek Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Studi Kasus". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menyusun Cerita...".
4.  **Area Output:**
    *   Judul (H3): "Studi Kasus yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh studi kasus.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##` untuk judul, `**` untuk tebal, dan `*` untuk daftar) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan data proyek dan mengklik tombol "Buat Studi Kasus".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis konten pemasaran (marketing content writer) yang ahli dalam menyusun studi kasus yang persuasif dan berorientasi pada hasil.

    Berikut adalah poin-poin atau data mentah dari sebuah proyek:
    """
    [Data dari input pengguna]
    """

    Tugas Anda adalah mengubah data ini menjadi sebuah studi kasus yang naratif dan meyakinkan, dengan mengikuti struktur **Masalah-Solusi-Hasil** yang jelas.

    - **Masalah (The Problem):** Identifikasi dan jelaskan tantangan atau masalah utama yang dihadapi klien sebelum menggunakan solusi Anda.
    - **Solusi (The Solution):** Jelaskan bagaimana produk atau layanan Anda diimplementasikan untuk mengatasi masalah tersebut.
    - **Hasil (The Results):** Paparkan hasil positif yang dicapai. Jika ada data kuantitatif (angka, persentase), tonjolkan data tersebut sebagai bukti keberhasilan.

    Gunakan format Markdown untuk judul, sub-judul, dan poin-poin penting untuk membuat studi kasus ini mudah dibaca dan profesional.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan studi kasus yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Poin-Poin atau Data Mentah Proyek Anda:" dengan:**
    ```
    - Klien: PT. Logistik Cepat
    - Masalah: Proses pelacakan inventaris masih manual menggunakan spreadsheet, sering terjadi human error dan data tidak real-time. Sulit mengetahui stok barang yang akurat.
    - Solusi: Mengimplementasikan sistem manajemen gudang (Warehouse Management System) berbasis web kami.
    - Hasil: Pengurangan human error sebesar 95%, peningkatan efisiensi waktu pencarian barang 80%, visibilitas stok real-time 100% di semua cabang.
    ```
---