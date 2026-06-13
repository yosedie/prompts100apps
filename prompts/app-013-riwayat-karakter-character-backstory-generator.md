## Nama Aplikasi
Riwayat Karakter: Character Backstory Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk penulis novel, skenario, atau game yang dapat menciptakan latar belakang karakter (backstory) yang kaya dan mendalam. Pengguna memasukkan beberapa sifat dasar, dan AI akan mengembangkannya menjadi profil karakter yang lengkap, termasuk motivasi, ketakutan, dan rahasia terpendam.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Riwayat Karakter".
2.  **Form Input Pengguna:**
    *   **Input Nama Karakter:** Sebuah kolom input teks dengan label "Nama Karakter:".
    *   **Input Arketipe/Peran:** Sebuah kolom input teks dengan label "Arketipe/Peran Utama:".
    *   **Input Sifat Positif:** Sebuah kolom input teks dengan label "Sifat Positif Utama:".
    *   **Input Kelemahan:** Sebuah kolom input teks dengan label "Kelemahan/Konflik Utama:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ciptakan Riwayat Karakter". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menulis...".
4.  **Area Output:**
    *   Judul (H3): "Profil Karakter:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh profil.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail karakter dan mengklik tombol "Ciptakan Riwayat Karakter".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis fiksi dan master pengembangan karakter (character development).

    Berdasarkan informasi dasar berikut:
    - Nama: [Nama dari input pengguna]
    - Arketipe/Peran: [Arketipe dari input pengguna]
    - Sifat Positif: [Sifat dari input pengguna]
    - Kelemahan/Konflik: [Kelemahan dari input pengguna]

    Tugas Anda adalah menciptakan profil karakter yang mendalam dan kaya. Kembangkan informasi dasar tersebut menjadi sebuah riwayat yang koheren. Profil harus mencakup bagian-bagian berikut:

    - **Ringkasan:** Paragraf singkat yang memperkenalkan karakter.
    - **Motivasi Utama:** Apa yang mendorong karakter ini untuk bertindak? Apa tujuan hidupnya?
    - **Ketakutan Terbesar:** Apa yang paling ia takuti, dan mengapa? Ini harus berhubungan dengan kelemahannya.
    - **Rahasia Terpendam:** Sebuah rahasia penting yang ia sembunyikan dari dunia, yang membentuk kepribadiannya.
    - **Latar Belakang Singkat:** Sebuah narasi singkat tentang masa lalunya yang menjelaskan bagaimana ia menjadi seperti sekarang.

    Gunakan format Markdown untuk judul, sub-judul, dan poin-poin penting agar profil mudah dibaca.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan profil karakter yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Karakter:" dengan:**
    `Kaelan`
*   **Isi kolom "Arketipe/Peran Utama:" dengan:**
    `Seorang pemburu bayaran di kota cyberpunk yang sinis`
*   **Isi kolom "Sifat Positif Utama:" dengan:**
    `Memiliki kode etik pribadi yang kuat`
*   **Isi kolom "Kelemahan/Konflik Utama:" dengan:**
    `Terobsesi dengan kegagalan di masa lalunya`
---