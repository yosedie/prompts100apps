## Nama Aplikasi
Pembuat Pidato Motivasi AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai penulis pidato motivasi. Pengguna memilih sebuah tema utama, dan AI akan menghasilkan naskah pidato singkat yang kuat, membangkitkan semangat, dan siap untuk disampaikan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pembuat Pidato Motivasi AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Tema:** Sebuah menu dropdown (select) dengan label "Pilih Tema Pidato Anda:" dan opsi: "Ketekunan & Pantang Menyerah", "Inovasi & Perubahan", "Kerja Sama Tim & Kolaborasi", "Mengatasi Kegagalan".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Bakar Semangat!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mencari Inspirasi...".
4.  **Area Output:**
    *   Judul (H3): "Naskah Pidato Motivasi Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh naskah.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih tema dan mengklik tombol "Bakar Semangat!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang motivator dan pembicara publik kelas dunia, setara dengan Tony Robbins atau Simon Sinek. Gaya Anda penuh semangat, inspiratif, dan persuasif.

    Berdasarkan tema berikut:
    """
    [Tema dari pilihan pengguna]
    """

    Tugas Anda adalah menulis naskah pidato motivasi singkat (sekitar 2-3 menit jika dibacakan). Naskah harus memiliki struktur yang kuat:
    1.  **Pembukaan yang Menghentak:** Mulai dengan sebuah pertanyaan retoris, kutipan, atau pernyataan berani yang langsung menarik perhatian.
    2.  **Isi yang Menginspirasi:** Gunakan analogi, metafora, atau cerita pendek untuk mengilustrasikan tema utama.
    3.  **Penutup yang Menggugah:** Akhiri dengan panggilan untuk bertindak (call to action) yang kuat dan kalimat yang membangkitkan semangat.

    Gunakan format Markdown untuk penekanan pada kata-kata atau kalimat kunci.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan naskah pidato di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Tema Pidato Anda:" ke:**
    `Ketekunan & Pantang Menyerah`
---