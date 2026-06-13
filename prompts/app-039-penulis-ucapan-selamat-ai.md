## Nama Aplikasi
Penulis Ucapan Selamat AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang membantu pengguna menulis ucapan selamat yang tulus dan personal. Pengguna memilih jenis acara, hubungan mereka dengan penerima, dan gaya yang diinginkan, lalu AI akan membuat beberapa draf ucapan yang bisa langsung digunakan atau dimodifikasi.

## Komponen Antar muka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Penulis Ucapan Selamat AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Acara:** Sebuah menu dropdown (select) dengan label "Untuk Acara Apa?" dan opsi: "Ulang Tahun", "Pernikahan", "Kelulusan", "Kelahiran Anak".
    *   **Input Hubungan:** Sebuah kolom input teks dengan label "Hubungan Anda dengan Penerima? (contoh: sahabat, rekan kerja, adik)".
    *   **Pilihan Gaya:** Sebuah menu dropdown (select) dengan label "Gaya Ucapan:" dan opsi: "Tulus & Menyentuh", "Lucu & Santai", "Formal & Penuh Hormat".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Ucapan Selamat". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Merangkai Kata...".
4.  **Area Output:**
    *   Judul (H3): "3 Draf Ucapan Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan 3 draf ucapan. Setiap draf harus dipisahkan dengan jelas.
    *   **Tombol Salin (Copy):** Setiap draf harus memiliki tombol "Salin" individual di sebelahnya.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `---` atau `**`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail acara dan mengklik tombol "Buat Ucapan Selamat".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis kartu ucapan yang sangat empatik dan pandai merangkai kata-kata yang tulus.

    Berdasarkan kriteria berikut:
    - Acara: [Acara dari pilihan pengguna]
    - Hubungan dengan Penerima: [Hubungan dari input pengguna]
    - Gaya Ucapan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah menulis **3 draf ucapan selamat yang berbeda**. Setiap draf harus:
    - Sesuai dengan acara, hubungan, dan gaya yang dipilih.
    - Terasa personal dan tidak generik.
    - Menyertakan tempat kosong seperti `[Nama Penerima]` agar mudah disesuaikan oleh pengguna.

    Gunakan format Markdown untuk memisahkan setiap draf dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 3 draf ucapan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Untuk Acara Apa?" ke:**
    `Pernikahan`
*   **Isi kolom "Hubungan Anda dengan Penerima?..." dengan:**
    `Sahabat sejak kecil`
*   **Atur pilihan "Gaya Ucapan:" ke:**
    `Tulus & Menyentuh`
---