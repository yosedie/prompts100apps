## Nama Aplikasi
Resolusi SMART AI: Personal Goal Setter

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pelatih penetapan tujuan. Pengguna memasukkan sebuah tujuan atau resolusi yang masih umum, dan AI akan membantu merumuskannya kembali menjadi tujuan yang **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound).

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Resolusi SMART AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) dengan label "Apa Tujuan atau Resolusi Anda yang Masih Umum?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Jadi SMART!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun Rencana...".
4.  **Area Output:**
    *   Judul (H3): "Resolusi Anda dalam Format SMART:"
    *   Sebuah area konten tunggal untuk menampilkan rincian tujuan SMART.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan tujuan umum dan mengklik tombol "Buat Jadi SMART!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pelatih pengembangan diri (life coach) dan ahli produktivitas yang berspesialisasi dalam metode penetapan tujuan SMART.

    Berikut adalah tujuan umum dari seorang pengguna:
    """
    [Tujuan dari input pengguna]
    """

    Tugas Anda adalah mengubah tujuan umum ini menjadi sebuah tujuan yang terstruktur menggunakan kerangka SMART. Rincikan setiap komponen dengan jelas:

    - **Specific (Spesifik):** Apa yang sebenarnya ingin dicapai? Siapa yang terlibat? Di mana?
    - **Measurable (Terukur):** Bagaimana cara mengukur kemajuannya? Angka apa yang bisa dilacak?
    - **Achievable (Dapat Dicapai):** Apakah tujuan ini realistis? Langkah pertama apa yang bisa diambil?
    - **Relevant (Relevan):** Mengapa tujuan ini penting bagi Anda saat ini?
    - **Time-bound (Berbatas Waktu):** Kapan target ini harus tercapai? Apa tenggat waktunya?

    Setelah merinci kelima komponen tersebut, tulis satu **Pernyataan Tujuan Akhir** yang menggabungkan semua elemen SMART menjadi satu kalimat yang kuat. Gunakan format Markdown untuk menyusun jawaban dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan rincian tujuan SMART di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Tujuan atau Resolusi Anda yang Masih Umum?" dengan:**
    `Saya ingin lebih sehat tahun ini.`
---