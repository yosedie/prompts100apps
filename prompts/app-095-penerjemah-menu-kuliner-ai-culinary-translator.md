## Nama Aplikasi
Penerjemah Menu Kuliner AI: Culinary Translator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai kamus kuliner interaktif. Pengguna memasukkan nama hidangan asing yang tidak mereka kenali, dan AI akan memberikan penjelasan singkat tentang apa itu, bahan-bahan utamanya, dan bagaimana cara memasaknya secara tradisional.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penerjemah Menu Kuliner AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Masukkan Nama Hidangan Asing:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Jelaskan Hidangan Ini!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Bertanya pada Koki...".
4.  **Area Output:**
    *   Judul (H3): "Deskripsi Hidangan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh penjelasan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama hidangan dan mengklik tombol "Jelaskan Hidangan Ini!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang koki internasional dan sejarawan kuliner. Anda memiliki pengetahuan luas tentang berbagai masakan dunia.

    Berdasarkan nama hidangan berikut:
    """
    [Nama hidangan dari input pengguna]
    """

    Tugas Anda adalah memberikan penjelasan yang jelas dan ringkas tentang hidangan ini untuk seseorang yang belum pernah mendengarnya. Penjelasan harus mencakup:

    1.  **Apa Itu?:** Satu kalimat pengantar tentang hidangan tersebut dan dari mana asalnya.
    2.  **Bahan Utama:** Daftar poin-poin bahan kunci yang memberikan rasa khas pada hidangan ini.
    3.  **Cara Memasak Singkat:** Jelaskan secara singkat bagaimana hidangan ini biasanya dibuat.

    Gunakan format Markdown untuk menyusun penjelasan dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan penjelasan hidangan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Nama Hidangan Asing:" dengan:**
    `Paella`
---