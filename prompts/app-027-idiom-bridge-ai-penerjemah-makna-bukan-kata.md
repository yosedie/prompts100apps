## Nama Aplikasi
Idiom Bridge AI: Penerjemah Makna, Bukan Kata

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web linguistik yang mampu menerjemahkan idiom. Aplikasi ini tidak menerjemahkan secara harfiah, melainkan menjelaskan makna sebenarnya dari idiom tersebut dan memberikan padanan idiom yang memiliki makna serupa di bahasa target.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Idiom Bridge AI".
2.  **Form Input Pengguna:**
    *   **Input Idiom:** Sebuah kolom input teks dengan label "Masukkan Idiom:".
    *   **Pilihan Bahasa:** Dua menu dropdown (select) berdampingan:
        *   "Dari Bahasa:" dengan opsi "Indonesia", "Inggris".
        *   "Ke Bahasa:" dengan opsi "Inggris", "Indonesia".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Terjemahkan Makna". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menjembatani Makna...".
4.  **Area Output:** Didesain dengan tiga bagian yang jelas:
    *   **Bagian 1: Terjemahan Harfiah:** Judul (H3) "Terjemahan Harfiah (Literal)" diikuti area konten.
    *   **Bagian 2: Makna Sebenarnya:** Judul (H3) "Makna Sebenarnya (Meaning)" diikuti area konten.
    *   **Bagian 3: Padanan Idiom:** Judul (H3) "Padanan Idiom (Equivalent Idiom)" diikuti area konten.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan idiom, memilih bahasa, dan mengklik tombol.
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli bahasa (linguist) dan pakar budaya yang memahami nuansa idiom di berbagai bahasa.

    Berdasarkan permintaan berikut:
    - Idiom: "[Idiom dari input pengguna]"
    - Terjemahkan dari: [Bahasa sumber dari pilihan pengguna]
    - Terjemahkan ke: [Bahasa target dari pilihan pengguna]

    Tugas Anda adalah memberikan TIGA informasi dalam format yang jelas:

    1.  **Terjemahan Harfiah:** Terjemahkan idiom ini kata per kata.
    2.  **Makna Sebenarnya:** Jelaskan arti atau makna sesungguhnya dari idiom ini.
    3.  **Padanan Idiom:** Berikan idiom dalam bahasa target yang memiliki makna paling mirip. Jika tidak ada padanan langsung, berikan frasa umum yang setara.

    Gunakan format Markdown berikut untuk jawaban Anda:
    **Terjemahan Harfiah:** [Jawaban Anda]
    **Makna Sebenarnya:** [Jawaban Anda]
    **Padanan Idiom:** [Jawaban Anda]
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi mem-parsing teks tersebut untuk memisahkan ketiga bagian.
5.  Aplikasi merender konten Markdown dan menampilkannya di tiga bagian yang sesuai di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Idiom:" dengan:**
    `Kambing hitam`
*   **Atur pilihan "Dari Bahasa:" ke:**
    `Indonesia`
*   **Atur pilihan "Ke Bahasa:" ke:**
    `Inggris`
---