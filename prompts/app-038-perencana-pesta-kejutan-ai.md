## Nama Aplikasi
Perencana Pesta Kejutan AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai perencana acara rahasia. Pengguna memasukkan detail tentang orang yang akan diberi kejutan, budget, dan tanggal, lalu AI akan menyusun rencana pesta kejutan yang lengkap dari A sampai Z, termasuk ide tema, rundown acara, dan timeline persiapan mundur.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Perencana Pesta Kejutan AI".
2.  **Form Input Pengguna:**
    *   **Input Nama:** Sebuah kolom input teks dengan label "Siapa yang akan diberi kejutan?".
    *   **Input Minat:** Sebuah area teks (textarea) dengan label "Apa hobi & minatnya? (contoh: game, film, musik, olahraga)".
    *   **Input Tanggal Pesta:** Sebuah kolom input tanggal (type="date") dengan label "Tanggal Pesta Kejutan:".
    *   **Pilihan Budget:** Sebuah menu dropdown (select) dengan label "Perkiraan Budget:" dan opsi: "Hemat (di bawah 500rb)", "Sedang (500rb - 1.5jt)", "Besar (di atas 1.5jt)".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Rencanakan Pesta!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun Rencana Rahasia...".
4.  **Area Output:**
    *   Judul (H3): "Rencana Lengkap Pesta Kejutan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh rencana.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail pesta dan mengklik tombol "Rencanakan Pesta!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang perencana acara (event planner) profesional yang ahli dalam merancang pesta kejutan yang detail dan tak terlupakan.

    Berdasarkan informasi berikut:
    - Untuk Siapa: [Nama dari input pengguna]
    - Hobi & Minat: [Minat dari input pengguna]
    - Tanggal Pesta: [Tanggal dari input pengguna]
    - Budget: [Budget dari pilihan pengguna]

    Tugas Anda adalah membuat rencana pesta kejutan yang lengkap dan dapat ditindaklanjuti. Rencana harus mencakup:

    1.  **Ide Tema Pesta:** Berikan 2-3 ide tema kreatif yang sesuai dengan hobi dan minat orang tersebut.
    2.  **Timeline Persiapan:** Buat timeline persiapan MUNDUR dari tanggal pesta (misal: 2 Minggu Sebelumnya, 1 Minggu Sebelumnya, 1 Hari Sebelumnya, Hari-H). Rincikan tugas-tugas penting di setiap tahap.
    3.  **Rundown Acara (Hari-H):** Buat jadwal acara yang detail untuk hari pesta, dari persiapan akhir hingga momen kejutan.
    4.  **Tips Menjaga Kerahasiaan:** Berikan beberapa tips kunci agar kejutan tidak bocor.

    Gunakan format Markdown untuk menyusun seluruh rencana dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan rencana pesta yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Siapa yang akan diberi kejutan?" dengan:**
    `Andi`
*   **Isi kolom "Apa hobi & minatnya?..." dengan:**
    `Suka nonton film fiksi ilmiah (sci-fi), main board game, dan mendengarkan musik rock klasik.`
*   **Atur "Tanggal Pesta Kejutan:" ke:**
    `(Pilih tanggal apa saja, sekitar 3 minggu dari sekarang)`
*   **Atur pilihan "Perkiraan Budget:" ke:**
    `Sedang (500rb - 1.5jt)`
---