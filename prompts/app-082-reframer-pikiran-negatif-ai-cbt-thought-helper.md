## Nama Aplikasi
Reframer Pikiran Negatif AI: CBT Thought Helper

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web berdasarkan prinsip Terapi Perilaku Kognitif (CBT). Pengguna memasukkan sebuah pemikiran negatif otomatis, dan AI akan membantu menuliskannya kembali menjadi 3 perspektif alternatif yang lebih seimbang, realistis, dan konstruktif.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Reframer Pikiran Negatif AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tuliskan Pikiran Negatif yang Mengganggu Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Cari Perspektif Baru". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Keseimbangan...".
4.  **Area Output:**
    *   **Disclaimer Penting:** Tepat di atas hasil, tampilkan teks peringatan: "**Catatan:** Aplikasi ini adalah alat bantu untuk refleksi diri dan bukan pengganti nasihat dari profesional kesehatan mental."
    *   Judul (H3): "3 Perspektif Alternatif yang Lebih Seimbang:"
    *   Sebuah area konten tunggal untuk menampilkan 3 perspektif dalam daftar bernomor.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (daftar bernomor) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan pikiran negatif dan mengklik tombol "Cari Perspektif Baru".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang terapis yang terlatih dalam Terapi Perilaku Kognitif (CBT). Anda ahli dalam membantu orang mengidentifikasi distorsi kognitif dan menemukan cara berpikir yang lebih seimbang.

    Berikut adalah pemikiran negatif otomatis dari seorang pengguna:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menulis **3 perspektif alternatif** yang lebih seimbang dan konstruktif. Perspektif ini harus:
    - Menantang pemikiran absolut (seperti "selalu" atau "tidak pernah").
    - Memisahkan perasaan dari fakta.
    - Menghindari "toxic positivity" (terlalu positif), melainkan fokus pada realisme yang penuh harapan.
    - Membuka kemungkinan lain selain skenario terburuk.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 3 perspektif alternatif di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tuliskan Pikiran Negatif yang Mengganggu Anda:" dengan:**
    `Saya gagal total dalam presentasi tadi, saya pasti akan dipecat.`
---