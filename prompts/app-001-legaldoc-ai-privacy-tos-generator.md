## Nama Aplikasi
LegalDoc AI: Privacy & ToS Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web sederhana namun profesional yang berfungsi sebagai generator dokumen legal dasar. Pengguna memasukkan nama dan deskripsi layanan mereka, dan aplikasi akan menghasilkan draf "Kebijakan Privasi" (Privacy Policy) dan "Syarat & Ketentuan" (Terms of Service).

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "LegalDoc AI: Generator Kebijakan Privasi & S&K".
2.  **Form Input Pengguna:**
    *   **Input Nama Layanan:** Sebuah kolom input teks dengan label "Nama Website/Aplikasi Anda:".
    *   **Input Deskripsi Layanan:** Sebuah area teks (textarea) yang lebih besar dengan label "Jelaskan Layanan Anda:". Berikan placeholder seperti "Contoh: Sebuah aplikasi mobile untuk berbagi resep masakan, di mana pengguna bisa mendaftar, mengunggah foto, dan memberikan komentar."
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Dokumen Sekarang". Saat proses berjalan, tombol ini harus dinonaktifkan dan menampilkan status "Memproses...".
4.  **Area Output Dokumen:**
    *   **Disclaimer Penting:** Tepat di atas hasil, tampilkan teks peringatan yang jelas: "**PENTING:** Dokumen ini dihasilkan oleh AI dan hanya bersifat draf. Ini bukan nasihat hukum. Selalu konsultasikan dengan profesional hukum untuk kebutuhan spesifik Anda."
    *   **Tampilan Tab:** Gunakan antarmuka tab untuk memisahkan kedua dokumen.
        *   **Tab 1:** "Kebijakan Privasi"
        *   **Tab 2:** "Syarat & Ketentuan"
    *   **Konten Dokumen:** Setiap tab akan berisi area teks (read-only) yang menampilkan dokumen yang dihasilkan. Teks harus diformat dengan baik (paragraf, judul, dll).
    *   **Tombol Salin (Copy):** Setiap area output harus memiliki tombol "Salin Teks" di sudut kanan atas untuk memudahkan pengguna menyalin seluruh dokumen.
5.  **Footer:** Sebuah footer sederhana di bagian bawah halaman dengan teks "Created by yosedie".

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi nama dan deskripsi layanan mereka, lalu mengklik tombol "Buat Dokumen Sekarang".
2.  Aplikasi menampilkan status loading.
3.  Di latar belakang, aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI. Prompt ini harus mengikuti format:
    ```
    Anda adalah seorang asisten AI yang berspesialisasi dalam membuat draf dokumen legal dasar untuk layanan digital.

    Berdasarkan informasi berikut:
    - Nama Layanan: [Nama dari input pengguna]
    - Deskripsi Layanan: [Deskripsi dari input pengguna]

    Tugas Anda adalah menghasilkan DUA dokumen terpisah:
    1.  Draf Kebijakan Privasi (Privacy Policy).
    2.  Draf Syarat & Ketentuan (Terms of Service).

    Pastikan kedua dokumen tersebut komprehensif untuk layanan yang dijelaskan, mencakup poin-poin standar seperti pengumpulan data, penggunaan data, hak pengguna, batasan tanggung jawab, dll. Gunakan format yang jelas dengan judul dan sub-judul.

    Pisahkan kedua dokumen dengan jelas menggunakan penanda unik, misalnya: "---END PRIVACY POLICY---".
    ```
4.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
5.  Setelah menerima respons, aplikasi mem-parsing teks tersebut, memisahkannya menjadi dua dokumen berdasarkan penanda unik.
6.  Aplikasi menampilkan Kebijakan Privasi di Tab 1 dan Syarat & Ketentuan di Tab 2.
7.  Status loading dihilangkan dan hasil ditampilkan.