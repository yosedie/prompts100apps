## Nama Aplikasi
Penulis Eulogi AI: In Loving Memory

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna menyusun pidato kenangan (eulogi) di saat-saat sulit. Pengguna memasukkan kenangan, sifat-sifat baik, dan hubungan mereka dengan almarhum/almarhumah, lalu AI akan membantu merangkainya menjadi sebuah eulogi yang tulus, mengharukan, dan penuh hormat.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Eulogi AI".
2.  **Form Input Pengguna:**
    *   **Input Hubungan:** Sebuah kolom input teks dengan label "Apa hubungan Anda dengan almarhum/almarhumah?".
    *   **Input Sifat:** Sebuah area teks (textarea) dengan label "Sebutkan 3 sifat terbaik yang paling Anda ingat darinya:".
    *   **Input Kenangan:** Sebuah area teks (textarea) dengan label "Ceritakan satu kenangan singkat yang paling berkesan bersama beliau:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Susun Draf Eulogi". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mengenang...".
4.  **Area Output:**
    *   Judul (H3): "Draf Eulogi Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh naskah.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti paragraf) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail kenangan dan mengklik tombol "Susun Draf Eulogi".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis yang sangat empatik dan bijaksana. Anda mampu merangkai kata-kata untuk menghormati kenangan seseorang dengan cara yang tulus dan mengharukan.

    Berdasarkan informasi berikut:
    - Hubungan Penulis: [Hubungan dari input pengguna]
    - Sifat Terbaik Almarhum/ah: """[Sifat dari input pengguna]"""
    - Kenangan Berkesan: """[Kenangan dari input pengguna]"""

    Tugas Anda adalah menulis sebuah draf eulogi yang singkat dan penuh hormat. Naskah harus:
    - Memiliki pembukaan yang memperkenalkan hubungan Anda dengan almarhum/ah.
    - Mengintegrasikan cerita tentang sifat-sifat baik dan kenangan yang diberikan.
    - Memiliki penutup yang merefleksikan warisan atau dampak positif yang ditinggalkan.
    - Menggunakan nada yang tulus, hangat, dan menghibur.

    Gunakan placeholder `[Nama Almarhum/ah]` agar mudah disesuaikan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan draf eulogi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa hubungan Anda dengan almarhum/almarhumah?" dengan:**
    `Saya adalah cucunya.`
*   **Isi kolom "Sebutkan 3 sifat terbaik yang paling Anda ingat darinya:" dengan:**
    `Selalu sabar, punya selera humor yang luar biasa, dan sangat pandai membuat kue.`
*   **Isi kolom "Ceritakan satu kenangan singkat yang paling berkesan bersama beliau:" dengan:**
    `Saya ingat saat beliau mengajari saya cara membuat kue cokelat pertamanya, meskipun dapurnya jadi berantakan, beliau hanya tertawa dan berkata bahwa kekacauan adalah bagian dari petualangan.`
---