## Nama Aplikasi
Generator Sumpah Pernikahan AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna menulis janji atau sumpah pernikahan (wedding vows) yang personal dan menyentuh. Pengguna memasukkan beberapa kenangan, sifat yang disukai, dan janji untuk pasangan mereka, lalu AI akan merangkainya menjadi sebuah naskah yang indah dan puitis.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Generator Sumpah Pernikahan AI".
2.  **Form Input Pengguna:**
    *   **Input Kenangan:** Sebuah area teks (textarea) dengan label "Ceritakan satu kenangan favorit bersama pasangan Anda:".
    *   **Input Sifat:** Sebuah area teks (textarea) dengan label "Sebutkan 3 sifat yang paling Anda cintai darinya:".
    *   **Input Janji:** Sebuah area teks (textarea) dengan label "Apa janji utama yang ingin Anda sampaikan untuk masa depan?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Tulis Sumpah Pernikahan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Merangkai Kata Cinta...".
4.  **Area Output:**
    *   Judul (H3): "Draf Sumpah Pernikahan Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh naskah.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail kenangan, sifat, dan janji, lalu mengklik tombol "Tulis Sumpah Pernikahan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis pidato dan penyair yang sangat romantis dan empatik. Anda ahli dalam merangkai cerita personal menjadi kata-kata yang menyentuh hati.

    Berdasarkan poin-poin personal berikut:
    - Kenangan Favorit: """[Teks dari input kenangan]"""
    - Sifat yang Dicintai: """[Teks dari input sifat]"""
    - Janji untuk Masa Depan: """[Teks dari input janji]"""

    Tugas Anda adalah menulis sebuah draf sumpah pernikahan yang indah dan personal. Naskah harus:
    - Dimulai dengan menyapa pasangan.
    - Mengintegrasikan kenangan favorit yang diberikan secara naratif.
    - Memuji sifat-sifat yang dicintai.
    - Diakhiri dengan janji untuk masa depan.
    - Menggunakan bahasa yang tulus, romantis, dan puitis.

    Gunakan placeholder `[Nama Pasangan]` agar mudah disesuaikan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan draf sumpah pernikahan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Ceritakan satu kenangan favorit bersama pasangan Anda:" dengan:**
    `Aku tidak akan pernah lupa saat kita pertama kali kehujanan di perjalanan pulang dan akhirnya kita malah tertawa-tawa sambil menari di bawah hujan.`
*   **Isi kolom "Sebutkan 3 sifat yang paling Anda cintai darinya:" dengan:**
    `Tawanya yang menular, kebaikannya pada semua orang, dan caranya membuatku merasa tenang saat aku panik.`
*   **Isi kolom "Apa janji utama yang ingin Anda sampaikan untuk masa depan?" dengan:**
    `Aku berjanji akan selalu menjadi partner dalam petualangan dan tempatmu pulang yang paling nyaman.`
---