## Nama Aplikasi
Perancang Tradisi Fiktif AI: Cultural Weaver

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para penulis dan world-builder yang menciptakan tradisi budaya fiktif. Pengguna memasukkan nama masyarakat dan nilai-nilai inti mereka, lalu AI akan merancang sebuah festival, ritual, atau tradisi unik yang mencerminkan nilai-nilai tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Perancang Tradisi Fiktif AI".
2.  **Form Input Pengguna:**
    *   **Input Nama Masyarakat:** Sebuah kolom input teks dengan label "Nama Masyarakat Fiktif Anda:".
    *   **Input Nilai Inti:** Sebuah area teks (textarea) dengan label "Apa Nilai-Nilai Inti Masyarakat Ini? (pisahkan dengan koma)".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ciptakan Tradisi". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menenun Budaya...".
4.  **Area Output:**
    *   Judul (H3): "Tradisi yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh deskripsi tradisi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan nama masyarakat dan nilai-nilainya, lalu mengklik tombol "Ciptakan Tradisi".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang antropolog budaya dan sejarawan fiksi. Anda ahli dalam merancang tradisi dan ritual yang terasa otentik dan memiliki makna mendalam bagi sebuah masyarakat.

    Berdasarkan informasi masyarakat fiktif berikut:
    - Nama Masyarakat: [Nama dari input pengguna]
    - Nilai-Nilai Inti: [Nilai-nilai dari input pengguna]

    Tugas Anda adalah merancang SATU tradisi, festival, atau ritual unik untuk masyarakat ini. Deskripsi tradisi harus mencakup:

    1.  **Nama Tradisi:** Berikan nama yang khas untuk tradisi ini.
    2.  **Tujuan & Makna:** Jelaskan mengapa tradisi ini ada dan nilai inti apa yang direpresentasikannya.
    3.  **Pelaksanaan:** Deskripsikan secara singkat bagaimana tradisi ini dirayakan atau dilakukan (misalnya, waktu, aktivitas, simbol yang digunakan).

    Gunakan format Markdown untuk menyusun deskripsi dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan deskripsi tradisi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Masyarakat Fiktif Anda:" dengan:**
    `Kaum Penempa Gunung`
*   **Isi kolom "Apa Nilai-Nilai Inti Masyarakat Ini?..." dengan:**
    `Keberanian, Komunitas, Kehormatan pada Leluhur`
---