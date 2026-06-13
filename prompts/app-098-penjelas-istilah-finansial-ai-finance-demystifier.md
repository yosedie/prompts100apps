## Nama Aplikasi
Penjelas Istilah Finansial AI: Finance Demystifier

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai kamus finansial yang disederhanakan. Pengguna memasukkan istilah investasi atau keuangan yang rumit, dan AI akan menjelaskannya menggunakan analogi sederhana dan bahasa yang mudah dipahami oleh pemula.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penjelas Istilah Finansial AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Istilah Keuangan yang Rumit:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Jelaskan Secara Sederhana!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyederhanakan...".
4.  **Area Output:**
    *   Judul (H3): "Penjelasan Sederhana:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh penjelasan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan istilah finansial dan mengklik tombol "Jelaskan Secara Sederhana!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penasihat keuangan dan edukator yang sangat pandai menyederhanakan konsep-konsep rumit. Anda sering menggunakan analogi untuk mengajar.

    Berdasarkan istilah keuangan berikut:
    """
    [Istilah dari input pengguna]
    """

    Tugas Anda adalah menjelaskan istilah ini kepada seorang pemula absolut. Penjelasan Anda harus:
    1.  Dimulai dengan sebuah **analogi sederhana** yang mudah dipahami (misalnya, membandingkannya dengan membeli sekeranjang buah, bukan satu buah saja).
    2.  Menjelaskan **apa itu** dan **bagaimana cara kerjanya** dalam bahasa yang sangat sederhana.
    3.  Menyebutkan **satu keuntungan utama** dari hal tersebut.

    Hindari jargon teknis sebisa mungkin. Gunakan format Markdown untuk penekanan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan penjelasan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Istilah Keuangan yang Rumit:" dengan:**
    `Reksadana Indeks`
---