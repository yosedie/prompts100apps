## Nama Aplikasi
Proses Efisien AI: Workflow Optimizer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web analitik yang berfungsi sebagai konsultan efisiensi proses. Pengguna mendeskripsikan sebuah alur kerja (workflow) yang ada, dan AI akan menganalisisnya untuk mengidentifikasi hambatan dan memberikan saran-saran konkret untuk meningkatkan efisiensi.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Proses Efisien AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Jelaskan Alur Kerja Anda Saat Ini Secara Detail:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Analisis & Beri Saran". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Saran Peningkatan Proses:"
    *   Sebuah area konten tunggal untuk menampilkan daftar saran.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `1.`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi alur kerja dan mengklik tombol "Analisis & Beri Saran".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang konsultan efisiensi proses bisnis (Business Process Efficiency Consultant) yang sangat berpengalaman.

    Berikut adalah deskripsi sebuah alur kerja (workflow) saat ini:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menganalisis alur kerja ini secara kritis. Identifikasi titik-titik hambatan (bottlenecks), inefisiensi, dan area yang rentan terhadap kesalahan (human error).

    Setelah itu, berikan daftar saran perbaikan yang konkret dan dapat ditindaklanjuti (actionable). Untuk setiap saran, jelaskan 'Mengapa' ini adalah masalah dan 'Bagaimana' solusinya dapat diterapkan.

    Sajikan hasilnya dalam format daftar bernomor. Gunakan format Markdown untuk kejelasan (judul, sub-judul, teks tebal).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan daftar saran yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Alur Kerja Anda Saat Ini Secara Detail:" dengan:**
    `Proses klaim reimbursement karyawan kami saat ini: 1. Karyawan mengisi formulir reimbursement kertas. 2. Karyawan menempelkan struk/bukti pembayaran fisik ke formulir. 3. Formulir diserahkan ke manajer untuk ditandatangani. 4. Manajer menyerahkan formulir ke departemen HRD. 5. HRD memeriksa dan mengarsipkan formulir fisik, lalu memberikan instruksi pembayaran ke tim keuangan. 6. Tim keuangan melakukan transfer manual.`
---