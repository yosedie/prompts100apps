## Nama Aplikasi
Radio Ad Pro: Penulis Naskah Iklan

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai penulis naskah iklan radio. Pengguna memasukkan deskripsi produk dan memilih durasi, lalu AI akan menyusun skrip iklan yang lengkap, termasuk arahan untuk efek suara (SFX), musik, dan dialog untuk durasi 30 atau 60 detik.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Radio Ad Pro".
2.  **Form Input Pengguna:**
    *   **Input Deskripsi Produk:** Sebuah area teks (textarea) dengan label "Deskripsi Produk/Layanan Anda:".
    *   **Pilihan Durasi:** Sebuah menu dropdown (select) dengan label "Pilih Durasi Iklan:" dan opsi: "30 Detik" dan "60 Detik".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Naskah Iklan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "On Air...".
4.  **Area Output:**
    *   Judul (H3): "Naskah Iklan Radio:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh naskah.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi deskripsi produk, memilih durasi, dan mengklik tombol "Buat Naskah Iklan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang copywriter iklan dan produser audio yang ahli dalam membuat naskah iklan radio yang menarik dan efektif.

    Berdasarkan informasi berikut:
    - Deskripsi Produk: [Deskripsi dari input pengguna]
    - Durasi Iklan: [Durasi dari pilihan pengguna]

    Tugas Anda adalah membuat naskah iklan radio yang lengkap dan siap produksi. Naskah harus diformat secara profesional dan mencakup:

    1.  **Arahan Musik:** Petunjuk tentang jenis musik yang harus diputar (contoh: [MUSIK: Upbeat dan ceria masuk lalu fade out]).
    2.  **Arahan Efek Suara (SFX):** Petunjuk untuk suara-suara yang relevan (contoh: [SFX: Suara mesin kopi espresso, cangkir beradu]).
    3.  **Dialog (NARATOR/SUARA):** Dialog yang diucapkan oleh narator atau karakter.

    Pastikan total durasi naskah sesuai dengan yang diminta. Naskah harus memiliki pembuka yang menarik, isi yang menjelaskan keunggulan produk, dan penutup dengan call-to-action yang jelas. Gunakan format Markdown untuk memisahkan arahan (SFX/Musik) dari dialog agar mudah dibaca.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan naskah yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Deskripsi Produk/Layanan Anda:" dengan:**
    `Kopi Kilat: Kedai kopi 'grab-and-go' yang menyajikan kopi premium dengan cepat untuk para profesional sibuk di pagi hari.`
*   **Atur pilihan "Pilih Durasi Iklan:" ke:**
    `30 Detik`
---