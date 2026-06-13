## Nama Aplikasi
Perencana Latihan Rumahan AI: Home Workout Planner

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pelatih kebugaran pribadi. Pengguna memilih area tubuh yang ingin dilatih, peralatan yang tersedia, dan tingkat kebugaran, lalu AI akan menyusun rutinitas latihan rumahan yang sederhana dan efektif, lengkap dengan deskripsi setiap gerakan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Perencana Latihan Rumahan AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Target Area:** Sebuah menu dropdown (select) dengan label "Pilih Target Area Tubuh:" dan opsi: "Seluruh Tubuh (Full Body)", "Perut & Inti (Abs & Core)", "Lengan & Dada (Upper Body)", "Kaki & Bokong (Lower Body)".
    *   **Input Peralatan:** Sebuah kolom input teks dengan label "Peralatan yang Tersedia (atau 'tanpa alat'):".
    *   **Pilihan Tingkat Kebugaran:** Sebuah menu dropdown (select) dengan label "Tingkat Kebugaran Anda:" dan opsi: "Pemula", "Menengah", "Mahir".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Rutinitas Latihan!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun Latihan...".
4.  **Area Output:**
    *   Judul (H3): "Rutinitas Latihan Anda Hari Ini:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh rutinitas.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih target, peralatan, dan tingkat kebugaran, lalu mengklik tombol "Buat Rutinitas Latihan!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pelatih kebugaran pribadi (personal trainer) bersertifikat. Anda ahli dalam merancang program latihan yang efektif dan aman untuk dilakukan di rumah.

    Berdasarkan kriteria pengguna berikut:
    - Target Area: [Target dari pilihan pengguna]
    - Peralatan: [Peralatan dari input pengguna]
    - Tingkat Kebugaran: [Tingkat dari pilihan pengguna]

    Tugas Anda adalah membuat satu rutinitas latihan yang lengkap. Rutinitas harus mencakup:
    1.  **Pemanasan (Warm-up):** 2-3 gerakan pemanasan ringan.
    2.  **Latihan Inti (Main Workout):** 4-6 gerakan latihan yang sesuai dengan target area, peralatan, dan tingkat kebugaran. Untuk setiap gerakan, sebutkan jumlah set dan repetisi yang direkomendasikan.
    3.  **Pendinginan (Cool-down):** 2-3 gerakan peregangan.

    Untuk setiap gerakan, berikan deskripsi singkat tentang cara melakukannya dengan benar. Gunakan format Markdown untuk menyusun rutinitas dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan rutinitas latihan di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Target Area Tubuh:" ke:**
    `Perut & Inti (Abs & Core)`
*   **Isi kolom "Peralatan yang Tersedia..." dengan:**
    `Tanpa alat`
*   **Atur pilihan "Tingkat Kebugaran Anda:" ke:**
    `Pemula`
---