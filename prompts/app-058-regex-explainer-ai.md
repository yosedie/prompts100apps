## Nama Aplikasi
Regex Explainer AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web utilitas yang berfungsi sebagai penerjemah ekspresi reguler (regex). Pengguna memasukkan sebuah pola regex yang rumit, dan AI akan menguraikannya bagian per bagian dan menjelaskannya dalam bahasa manusia yang mudah dimengerti.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Regex Explainer AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Tempelkan Ekspresi Reguler (Regex) Anda:". Input ini harus menggunakan font monospace.
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Jelaskan Regex Ini!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menguraikan...".
4.  **Area Output:**
    *   Judul (H3): "Penjelasan Regex:"
    *   Sebuah area konten tunggal untuk menampilkan penjelasan terperinci.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**`, `*`, dan blok kode kecil) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan pola regex dan mengklik tombol "Jelaskan Regex Ini!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang programmer senior dan ahli ekspresi reguler (regex). Anda sangat pandai dalam membaca pola regex yang paling rumit sekalipun dan menjelaskannya kepada orang lain.

    Berdasarkan ekspresi reguler berikut:
    """
    [Regex dari input pengguna]
    """

    Tugas Anda adalah memberikan penjelasan yang terperinci untuk setiap bagian dari regex ini. Uraikan pola tersebut secara berurutan dan jelaskan apa yang dicocokkan oleh setiap token atau grup.

    Gunakan format Markdown untuk menyajikan penjelasan dengan rapi, misalnya dengan daftar poin atau tabel.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan penjelasan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Ekspresi Reguler (Regex) Anda:" dengan:**
    `^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$`
---