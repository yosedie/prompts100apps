## Nama Aplikasi
Pembuat Resep Aneh AI: Grimoire Gastronomi

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web hiburan yang menghasilkan resep makanan yang aneh dan lucu. Pengguna memilih persona (Alien atau Penyihir) dan nama makanan normal, lalu AI akan menulis ulang resep tersebut seolah-olah berasal dari dunia lain, lengkap dengan bahan-bahan dan langkah-langkah yang tidak masuk akal.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pembuat Resep Aneh AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Persona:** Sebuah menu dropdown (select) dengan label "Pilih Penulis Resep:" dan opsi: "Alien dari Galaksi Zorp", "Penyihir dari Hutan Gelap".
    *   **Input Makanan:** Sebuah kolom input teks dengan label "Nama Makanan Normal yang Ingin Dibuat Aneh:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Resep Aneh!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Mengaduk Kuali...".
4.  **Area Output:**
    *   Judul (H3): "Resep dari Dimensi Lain:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh resep.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih persona, memasukkan nama makanan, dan mengklik tombol "Buat Resep Aneh!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah [Persona dari pilihan pengguna] yang sedang menulis buku resep untuk kaum Anda.

    Berdasarkan makanan manusia berikut:
    """
    [Nama makanan dari input pengguna]
    """

    Tugas Anda adalah membuat versi resep yang aneh dan lucu dari makanan tersebut, dari sudut pandang Anda. Resep harus mencakup:

    1.  **Nama Resep Aneh:** Beri nama baru yang sesuai dengan persona Anda (contoh: "Tumis Meteor" atau "Sup Akar Mandrake").
    2.  **Bahan-Bahan Aneh:** Ganti bahan-bahan normal dengan bahan fiktif yang lucu dari dunia Anda (contoh: 'air mata naga', 'baut bekas kapal luar angkasa', 'bubuk cahaya bulan').
    3.  **Langkah-Langkah Aneh:** Tulis langkah-langkah memasak yang tidak masuk akal atau menggunakan alat-alat aneh (contoh: "Aduk menggunakan obeng sonik," atau "Bacakan mantra pemanggil rasa").

    Gunakan format Markdown untuk menyusun resep dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan resep aneh yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Penulis Resep:" ke:**
    `Penyihir dari Hutan Gelap`
*   **Isi kolom "Nama Makanan Normal yang Ingin Dibuat Aneh:" dengan:**
    `Nasi Goreng`
---