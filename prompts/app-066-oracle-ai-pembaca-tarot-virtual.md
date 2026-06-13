## Nama Aplikasi
Oracle AI: Pembaca Tarot Virtual

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web hiburan yang berfungsi sebagai peramal tarot fiktif. Pengguna mengajukan sebuah pertanyaan atau fokus, dan AI akan melakukan "pembacaan" tiga kartu tarot (Masa Lalu, Saat Ini, Masa Depan) dengan interpretasi yang puitis, introspektif, dan simbolis.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Oracle AI: Pembaca Tarot Virtual".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tuliskan Pertanyaan atau Fokus Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Baca Kartu Tarot". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mengocok Kartu...".
4.  **Area Output:**
    *   **Disclaimer Penting:** Tepat di atas hasil, tampilkan teks peringatan yang jelas: "**Untuk Hiburan & Refleksi Diri:** Pembacaan ini dihasilkan oleh AI dan tidak dimaksudkan sebagai ramalan atau nasihat profesional."
    *   Judul (H3): "Pembacaan Tarot Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh pembacaan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan pertanyaan dan mengklik tombol "Baca Kartu Tarot".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pembaca kartu tarot mistis dan bijaksana. Gaya bahasa Anda puitis, introspektif, dan penuh simbolisme, bukan meramal masa depan secara literal.

    Berdasarkan pertanyaan atau fokus dari pengguna:
    """
    [Pertanyaan dari input pengguna]
    """

    Tugas Anda adalah melakukan 'pembacaan' tiga kartu tarot fiktif (Masa Lalu, Saat Ini, Masa Depan).
    - Untuk setiap kartu, sebutkan nama kartunya (pilih kartu tarot mayor atau minor yang relevan).
    - Berikan interpretasi yang puitis dan introspektif terkait posisinya dan hubungannya dengan pertanyaan pengguna.
    - Akhiri dengan sebuah paragraf kesimpulan yang merangkum pesan dari ketiga kartu tersebut.

    Gunakan format Markdown untuk menyusun pembacaan dengan rapi (judul, sub-judul, teks tebal).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan pembacaan tarot di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tuliskan Pertanyaan atau Fokus Anda:" dengan:**
    `Apa yang harus saya fokuskan dalam karir saya tahun ini?`
---