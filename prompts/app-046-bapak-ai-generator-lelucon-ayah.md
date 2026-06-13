## Nama Aplikasi
Bapak AI: Generator Lelucon Ayah

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web sederhana yang berfungsi sebagai generator lelucon ayah (dad jokes) tanpa henti. Pengguna memasukkan sebuah kata kunci, dan AI akan membuat lelucon receh atau permainan kata (pun) berdasarkan kata kunci tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Bapak AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Beri saya satu kata kunci:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Lelucon!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari inspirasi receh...".
4.  **Area Output:**
    *   Judul (H3): "Lelucon Ayah Untukmu:"
    *   Sebuah area konten tunggal yang didesain seperti kartu atau bubble chat untuk menampilkan lelucon.
    *   **Tombol Lagi!:** Di bawah lelucon, sertakan tombol "Lagi Dong!" yang akan membuat lelucon baru dengan kata kunci yang sama tanpa perlu mengklik tombol utama lagi.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (jika ada) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan kata kunci dan mengklik tombol "Buat Lelucon!" atau "Lagi Dong!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang "Bapak-Bapak" dengan selera humor yang sangat receh. Anda adalah raja dari dad jokes dan permainan kata (puns).

    Berdasarkan kata kunci berikut:
    """
    [Kata kunci dari input pengguna]
    """

    Tugas Anda adalah membuat SATU lelucon ayah yang orisinal dan receh. Lelucon harus dalam format tanya-jawab.

    PENTING: Hanya berikan teks leluconnya saja, tanpa tambahan komentar atau emoji.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan lelucon yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Beri saya satu kata kunci:" dengan:**
    `Ikan`
---