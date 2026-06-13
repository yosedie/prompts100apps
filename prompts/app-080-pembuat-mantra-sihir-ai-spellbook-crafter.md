## Nama Aplikasi
Pembuat Mantra Sihir AI: Spellbook Crafter

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web kreatif yang menciptakan "mantra" atau "rapalan sihir" fiktif. Pengguna mendeskripsikan efek sihir yang diinginkan, dan AI akan menghasilkan nama mantra, rapalan yang berima, dan efek samping kecil yang menarik.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pembuat Mantra Sihir AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) dengan label "Apa Efek Sihir yang Diinginkan?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Rapalkan Mantra!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Mengumpulkan Mana...".
4.  **Area Output:**
    *   Judul (H3): "Mantra yang Tercipta:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh detail mantra.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan efek sihir dan mengklik tombol "Rapalkan Mantra!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang Archmage, penjaga perpustakaan sihir kuno. Anda adalah pencipta mantra yang tak tertandingi.

    Berdasarkan efek sihir yang diinginkan berikut:
    """
    [Efek dari input pengguna]
    """

    Tugas Anda adalah menciptakan satu mantra sihir yang lengkap. Mantra harus mencakup:

    1.  **Nama Mantra:** Nama yang terdengar magis dan sesuai dengan efeknya.
    2.  **Rapalan (Incantation):** Beberapa baris kalimat yang berima dan puitis untuk mengucapkan mantra.
    3.  **Efek Samping Kecil:** Sebuah efek samping yang menarik atau sedikit lucu (contoh: "rambut pengguna akan berkilau selama satu jam").

    Gunakan format Markdown untuk menyusun detail mantra dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan detail mantra di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa Efek Sihir yang Diinginkan?" dengan:**
    `Membuat secangkir teh hangat muncul di tangan.`
---