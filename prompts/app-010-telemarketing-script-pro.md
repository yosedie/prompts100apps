## Nama Aplikasi
Telemarketing Script Pro

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai generator naskah (skrip) telemarketing. Pengguna memasukkan informasi tentang produk, keunggulannya, dan target audiens, lalu AI akan menyusun skrip panggilan penjualan yang lengkap dan efektif, dari kalimat pembuka hingga cara mengatasi penolakan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Telemarketing Script Pro".
2.  **Form Input Pengguna:**
    *   **Input Produk/Layanan:** Sebuah kolom input teks dengan label "Nama Produk/Layanan yang Ditawarkan:".
    *   **Input Keunggulan:** Sebuah area teks (textarea) dengan label "Poin-Poin Keunggulan Utama:".
    *   **Input Target Audiens:** Sebuah area teks (textarea) dengan label "Siapa Target Audiens Anda?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Naskah Penjualan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun Naskah...".
4.  **Area Output:**
    *   Judul (H3): "Naskah Panggilan Penjualan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh naskah.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail produk dan audiens, lalu mengklik tombol "Buat Naskah Penjualan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis naskah penjualan (sales scriptwriter) dan pelatih telemarketing yang sangat berpengalaman.

    Berdasarkan informasi berikut:
    - Produk/Layanan: [Nama dari input pengguna]
    - Keunggulan Utama: [Poin-poin dari input pengguna]
    - Target Audiens: [Deskripsi dari input pengguna]

    Tugas Anda adalah membuat naskah panggilan penjualan (telemarketing script) yang lengkap dan persuasif. Naskah harus terstruktur dengan jelas dan mencakup bagian-bagian berikut:

    1.  **Pembuka (Opening):** Kalimat pembuka yang menarik perhatian dan membangun rapport dalam beberapa detik.
    2.  **Penyampaian Nilai (Value Proposition):** Jelaskan secara singkat bagaimana produk/layanan ini bisa membantu target audiens, berdasarkan keunggulan yang diberikan.
    3.  **Mengatasi Penolakan Umum (Handling Objections):** Sediakan contoh cara menjawab penolakan umum seperti "Saya tidak tertarik," "Harganya terlalu mahal," atau "Saya sedang sibuk."
    4.  **Panggilan untuk Bertindak (Call to Action):** Kalimat penutup yang jelas untuk mengarahkan prospek ke langkah selanjutnya (misalnya, menjadwalkan demo, mengirim email, dll.).

    Gunakan format Markdown untuk judul, sub-judul, dan poin-poin penting agar naskah mudah dibaca dan diikuti.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan naskah yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Nama Produk/Layanan yang Ditawarkan:" dengan:**
    `SyncUp CRM`
*   **Isi kolom "Poin-Poin Keunggulan Utama:" dengan:**
    `- Mengotomatiskan follow-up email ke pelanggan.
    - Dasbor analitik penjualan real-time.
    - Mengelola semua data pelanggan di satu tempat, tidak perlu spreadsheet lagi.`
*   **Isi kolom "Siapa Target Audiens Anda?" dengan:**
    `Pemilik usaha kecil dan menengah (UKM) yang saat ini masih mengelola data pelanggan secara manual.`
---