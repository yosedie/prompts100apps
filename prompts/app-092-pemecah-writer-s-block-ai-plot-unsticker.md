## Nama Aplikasi
Pemecah Writer's Block AI: Plot Unsticker

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai teman brainstorming untuk para penulis. Pengguna mendeskripsikan sebuah adegan atau titik plot di mana mereka merasa buntu, dan AI akan memberikan tiga saran yang berbeda dan tak terduga tentang bagaimana cerita bisa berlanjut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pemecah Writer's Block AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Jelaskan di mana Anda merasa buntu dalam cerita Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Beri Saya Ide!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Brainstorming...".
4.  **Area Output:**
    *   Judul (H3): "3 Ide untuk Melanjutkan Cerita:"
    *   Sebuah area konten tunggal untuk menampilkan 3 ide. Setiap ide harus dipisahkan dengan jelas.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Semua" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##` dan `---`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi kebuntuan mereka dan mengklik tombol "Beri Saya Ide!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang editor cerita (story editor) dan penulis kreatif yang sangat imajinatif. Anda ahli dalam menemukan solusi tak terduga untuk masalah plot.

    Berikut adalah deskripsi kebuntuan (writer's block) dari seorang penulis:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah memberikan **3 saran yang sangat berbeda** tentang bagaimana cerita bisa berlanjut dari titik ini. Setiap saran harus:
    - Menawarkan arah yang unik (misalnya, satu saran bisa berupa aksi, satu berupa pengungkapan karakter, satu berupa plot twist).
    - Cukup detail untuk memicu imajinasi penulis.
    - Dirancang untuk memecahkan kebuntuan dan membuka kemungkinan baru.

    Gunakan format Markdown untuk memisahkan setiap saran dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 3 ide di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan di mana Anda merasa buntu dalam cerita Anda:" dengan:**
    `Protagonis saya, seorang detektif, akhirnya berhasil menyudutkan penjahat utama di atap gedung. Mereka berdua saling menodongkan senjata. Saya tidak tahu bagaimana cara mengakhiri adegan ini tanpa terasa klise.`
---