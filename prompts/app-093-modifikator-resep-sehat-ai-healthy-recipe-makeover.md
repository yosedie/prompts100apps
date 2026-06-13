## Nama Aplikasi
Modifikator Resep Sehat AI: Healthy Recipe Makeover

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai ahli gizi virtual. Pengguna menempelkan sebuah resep masakan, dan AI akan menganalisisnya untuk memberikan saran substitusi bahan dan metode memasak agar resep tersebut menjadi lebih sehat, tanpa mengorbankan rasa secara signifikan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Modifikator Resep Sehat AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Resep Lengkap Anda di Sini (Bahan & Langkah):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Jadi Lebih Sehat!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Saran Modifikasi Resep Sehat:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh saran.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan resep dan mengklik tombol "Buat Jadi Lebih Sehat!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli gizi (nutritionist) dan koki yang ahli dalam memasak sehat. Anda tahu cara memodifikasi resep agar lebih bergizi tanpa membuatnya hambar.

    Berikut adalah resep yang perlu dimodifikasi:
    """
    [Teks resep dari input pengguna]
    """

    Tugas Anda adalah memberikan saran modifikasi untuk membuat resep ini lebih sehat. Kelompokkan saran Anda ke dalam dua bagian:

    1.  **Substitusi Bahan:** Sarankan bahan-bahan pengganti yang lebih sehat (misalnya, ganti tepung terigu dengan tepung gandum, gula dengan pemanis alami, minyak goreng dengan minyak zaitun). Jelaskan mengapa penggantian ini lebih baik.
    2.  **Modifikasi Metode Memasak:** Sarankan perubahan dalam cara memasak untuk mengurangi lemak atau kalori (misalnya, ganti 'goreng' dengan 'panggang' atau 'kukus').

    Gunakan format Markdown untuk menyusun saran dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan saran modifikasi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Resep Lengkap Anda di Sini..." dengan:**
    `Resep Ayam Goreng Tepung

    Bahan:
    - 1 ekor ayam, potong 8
    - 200g tepung terigu serbaguna
    - 1 sdt garam
    - 1 sdt lada
    - Minyak goreng secukupnya

    Langkah:
    1. Campur tepung, garam, dan lada.
    2. Balurkan potongan ayam ke dalam campuran tepung hingga rata.
    3. Panaskan minyak dalam jumlah banyak.
    4. Goreng ayam hingga terendam minyak sampai berwarna cokelat keemasan dan matang.`
---