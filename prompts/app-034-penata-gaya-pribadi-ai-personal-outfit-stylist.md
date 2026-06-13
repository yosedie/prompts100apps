## Nama Aplikasi
Penata Gaya Pribadi AI: Personal Outfit Stylist

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai penata gaya pribadi virtual. Pengguna memasukkan jenis acara, gaya busana, dan gaya yang diinginkan, lalu AI akan memberikan satu rekomendasi outfit yang lengkap dan koheren, dari atasan hingga sepatu dan aksesori.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penata Gaya Pribadi AI".
2.  **Form Input Pengguna:**
    *   **Input Acara:** Sebuah kolom input teks dengan label "Untuk Acara Apa?".
    *   **Pilihan Gaya Busana:** Sebuah menu dropdown (select) dengan label "Gaya Busana Untuk:" dan opsi: "Pria", "Wanita".
    *   **Pilihan Gaya:** Sebuah menu dropdown (select) dengan label "Gaya yang Diinginkan:" dan opsi: "Formal & Profesional", "Kasual & Santai", "Elegan & Chic", "Kreatif & Unik".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Rekomendasikan Outfit!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Inspirasi...".
4.  **Area Output:**
    *   Judul (H3): "Rekomendasi Outfit Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh rekomendasi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail acara dan gaya, lalu mengklik tombol "Rekomendasikan Outfit!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penata gaya pribadi (personal stylist) dan fashion consultant yang berpengalaman dengan selera mode yang tinggi.

    Berdasarkan kriteria berikut:
    - Acara: [Acara dari input pengguna]
    - Gaya Busana Untuk: [Gaya busana dari pilihan pengguna]
    - Gaya yang Diinginkan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah merancang SATU rekomendasi outfit yang lengkap dan koheren. Rekomendasi harus mencakup:
    - **Atasan (Top):**
    - **Bawahan (Bottom):**
    - **Lapisan Luar (Outerwear, jika perlu):**
    - **Sepatu (Footwear):**
    - **Aksesori (Accessories):**
    - **Tips Tambahan:** (Berikan satu tips singkat tentang cara memakainya).

    Pastikan semua item saling melengkapi dan sesuai dengan acara serta gaya yang diinginkan. Gunakan format Markdown untuk menyusun rekomendasi dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan rekomendasi outfit yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Untuk Acara Apa?" dengan:**
    `Wawancara kerja di perusahaan teknologi`
*   **Atur pilihan "Gaya Busana Untuk:" ke:**
    `Wanita`
*   **Atur pilihan "Gaya yang Diinginkan:" ke:**
    `Formal & Profesional`
---