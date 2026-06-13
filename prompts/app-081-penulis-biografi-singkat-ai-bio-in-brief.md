## Nama Aplikasi
Penulis Biografi Singkat AI: Bio in Brief

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang menulis biografi singkat (sekitar 150 kata) tentang tokoh sejarah atau fiksi. Pengguna hanya perlu memasukkan nama tokoh, dan AI akan menghasilkan ringkasan yang padat, menyoroti pencapaian dan dampak terpenting mereka.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Biografi Singkat AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Nama Tokoh (Sejarah atau Fiksi):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tulis Biografi". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Meneliti...".
4.  **Area Output:**
    *   Judul (H3): "Biografi Singkat:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh biografi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama tokoh dan mengklik tombol "Tulis Biografi".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang sejarawan dan penulis biografi yang ahli dalam merangkum kehidupan seseorang secara ringkas namun berdampak.

    Berdasarkan nama tokoh berikut:
    """
    [Nama tokoh dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah biografi singkat, sekitar 150 kata. Biografi harus:
    - Memperkenalkan siapa tokoh tersebut.
    - Menyoroti pencapaian atau kontribusi mereka yang paling signifikan.
    - Menjelaskan dampak atau warisan abadi mereka.
    - Ditulis dalam gaya ensiklopedis yang jelas dan informatif.

    PENTING: Hanya berikan teks biografinya saja, tanpa tambahan komentar.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan biografi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Nama Tokoh (Sejarah atau Fiksi):" dengan:**
    `Albert Einstein`
---