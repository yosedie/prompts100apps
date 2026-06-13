## Nama Aplikasi
Generator Konspirasi Fiktif: The Truth Is In Here AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang menciptakan teori konspirasi yang terdengar meyakinkan (namun sepenuhnya fiktif dan untuk hiburan). Pengguna memasukkan sebuah objek atau peristiwa sehari-hari, dan AI akan menghasilkan sebuah teori konspirasi yang rumit dan lucu tentangnya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Generator Konspirasi Fiktif".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Objek atau Peristiwa Sehari-hari Apa yang Ingin Diungkap?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ungkap Kebenarannya!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menghubungkan Titik-Titik...".
4.  **Area Output:**
    *   Judul (H3): "Teori Konspirasi yang 'Sebenarnya':"
    *   Sebuah area konten tunggal untuk menampilkan seluruh teori.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan objek/peristiwa dan mengklik tombol "Ungkap Kebenarannya!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli teori konspirasi veteran dan peneliti 'kebenaran tersembunyi'. Anda mampu melihat pola dan hubungan rahasia di balik hal-hal yang paling biasa sekalipun.

    Berdasarkan objek/peristiwa sehari-hari berikut:
    """
    [Input dari pengguna]
    """

    Tugas Anda adalah menciptakan SATU teori konspirasi yang terdengar meyakinkan, rumit, namun sepenuhnya fiktif dan menghibur. Teori harus memiliki struktur berikut:

    - **Apa yang 'Mereka' Ingin Anda Percaya:** Jelaskan penjelasan yang umum atau membosankan.
    - **Kebenaran yang Sebenarnya:** Ungkap "kebenaran" yang tersembunyi di baliknya.
    - **'Bukti' yang Tak Terbantahkan:** Berikan beberapa "bukti" yang terdengar masuk akal tapi sebenarnya tidak berhubungan.
    - **Apa Tujuan Mereka Sebenarnya?:** Jelaskan motif tersembunyi di balik konspirasi ini.

    Gunakan format Markdown untuk menyusun teori dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan teori konspirasi yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Objek atau Peristiwa Sehari-hari Apa yang Ingin Diungkap?" dengan:**
    `Kaus kaki yang hilang sebelah`
---