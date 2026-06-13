## Nama Aplikasi
WorldForge AI: Generator Dunia Fiksi

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para penulis dan world-builder. Pengguna memasukkan satu tema atau konsep inti, dan AI akan menghasilkan deskripsi yang kaya dan mendalam untuk sebuah dunia fiksi baru, lengkap dengan geografi, budaya, sistem sihir/teknologi, dan faksi politiknya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "WorldForge AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Masukkan Tema Utama atau Konsep Inti Dunia Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ciptakan Dunia!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Membangun Realitas...".
4.  **Area Output:**
    *   Judul (H3): "Deskripsi Dunia Fiksi Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh deskripsi.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan tema dan mengklik tombol "Ciptakan Dunia!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang world-builder veteran, sejarawan fiksi, dan penulis fantasi epik.

    Berdasarkan tema inti berikut:
    """
    [Tema dari input pengguna]
    """

    Tugas Anda adalah menciptakan deskripsi yang kaya dan mendalam untuk sebuah dunia fiksi baru. Deskripsi harus mencakup empat pilar utama:

    1.  **Geografi Unik:** Jelaskan lanskap, iklim, dan ciri khas geografis dunia ini.
    2.  **Budaya & Masyarakat:** Deskripsikan penduduknya, tradisi mereka, dan bagaimana mereka beradaptasi dengan lingkungannya.
    3.  **Sistem Sihir atau Teknologi Khas:** Jelaskan sumber kekuatan di dunia ini. Apakah itu sihir, teknologi uap, psionik, atau lainnya? Bagaimana cara kerjanya?
    4.  **Faksi & Politik:** Sebutkan 2-3 faksi atau kerajaan utama yang ada, dan jelaskan hubungan atau konflik di antara mereka.

    Gunakan format Markdown untuk menyusun deskripsi dengan rapi (judul, sub-judul, daftar poin).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan deskripsi dunia yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Tema Utama atau Konsep Inti Dunia Anda:" dengan:**
    `Sebuah dunia di mana kota-kota terapung di atas lautan awan beracun, dan perjalanan antar kota dilakukan dengan kapal udara.`
---