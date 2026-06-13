## Nama Aplikasi
Generator Nama Band AI: Band Name Forge

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu para musisi menemukan nama band yang keren dan unik. Pengguna memilih genre musik mereka, dan AI akan menghasilkan 10 ide nama band yang kreatif dan sesuai dengan genre tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Generator Nama Band AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Genre:** Sebuah menu dropdown (select) dengan label "Pilih Genre Musik Anda:" dan opsi: "Indie Rock", "Heavy Metal", "Pop Punk", "Electronic Dance Music (EDM)", "Folk Akustik", "Hip Hop Alternatif".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Generate Nama Band!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Tuning Up...".
4.  **Area Output:**
    *   Judul (H3): "10 Ide Nama Band Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan 10 nama dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih genre dan mengklik tombol "Generate Nama Band!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang produser musik dan pencari bakat (A&R scout) yang sangat keren dan memiliki selera musik yang tinggi. Anda tahu nama seperti apa yang akan terlihat bagus di poster konser.

    Berdasarkan genre musik berikut:
    """
    [Genre dari pilihan pengguna]
    """

    Tugas Anda adalah membuat **10 ide nama band** yang unik, keren, dan cocok dengan nuansa genre tersebut.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 10 ide nama band di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Genre Musik Anda:" ke:**
    `Indie Rock`
---