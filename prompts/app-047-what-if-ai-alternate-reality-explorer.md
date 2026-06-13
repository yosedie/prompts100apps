## Nama Aplikasi
What If AI: Alternate Reality Explorer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang memungkinkan pengguna menjelajahi skenario sejarah atau fiksi alternatif. Pengguna mengajukan pertanyaan "Bagaimana jika...", dan AI akan menulis sebuah esai naratif yang mengeksplorasi konsekuensi dan realitas alternatif dari skenario tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "What If AI: Alternate Reality Explorer".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Ajukan Pertanyaan 'Bagaimana Jika...' Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Jelajahi Skenario!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menjelajahi Lini Masa...".
4.  **Area Output:**
    *   Judul (H3): "Eksplorasi Skenario Alternatif:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh esai.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan skenario "Bagaimana jika" dan mengklik tombol "Jelajahi Skenario!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang sejarawan sejarah alternatif dan penulis fiksi spekulatif. Anda ahli dalam menganalisis titik-titik percabangan dalam sejarah dan mengeksplorasi konsekuensi jangka panjangnya.

    Berdasarkan pertanyaan "Bagaimana jika" berikut:
    """
    [Pertanyaan dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah esai naratif yang mendalam yang menjelajahi skenario ini. Esai Anda harus mencakup:
    - **Konsekuensi Langsung:** Apa yang akan langsung berubah setelah peristiwa percabangan ini?
    - **Efek Riak (Ripple Effects):** Bagaimana perubahan awal ini memengaruhi perkembangan teknologi, sosial, budaya, dan politik dalam dekade atau abad berikutnya?
    - **Dunia Saat Ini:** Gambarkan seperti apa dunia "saat ini" dalam lini masa alternatif ini.

    Gunakan gaya penulisan yang menarik dan informatif. Gunakan format Markdown untuk menyusun esai dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan esai yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Ajukan Pertanyaan 'Bagaimana Jika...' Anda:" dengan:**
    `Bagaimana jika internet tidak pernah ditemukan?`
---