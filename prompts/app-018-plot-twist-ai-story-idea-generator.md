## Nama Aplikasi
Plot Twist AI: Story Idea Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web kreatif untuk para penulis. Pengguna memasukkan sinopsis atau ringkasan cerita mereka, dan AI akan memberikan 3 ide plot twist yang tak terduga dan berpotensi mengubah arah narasi secara drastis.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Plot Twist AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Sinopsis Cerita Anda di Sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Cari Plot Twist!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Berpikir Keras...".
4.  **Area Output:**
    *   Judul (H3): "3 Ide Plot Twist Tak Terduga:"
    *   Sebuah area konten tunggal untuk menampilkan 3 ide plot twist.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `###` untuk judul dan `**` untuk tebal) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan sinopsis dan mengklik tombol "Cari Plot Twist!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang penulis novel misteri dan skenario film thriller yang ahli dalam menciptakan plot twist yang mengejutkan dan cerdas.

    Berikut adalah sinopsis sebuah cerita:
    """
    [Sinopsis dari input pengguna]
    """

    Tugas Anda adalah membaca sinopsis ini dan memberikan **3 ide plot twist yang benar-benar tak terduga**. Untuk setiap ide, jelaskan secara singkat twist-nya dan bagaimana hal itu bisa mengubah arah cerita secara drastis.

    Gunakan format Markdown untuk memisahkan setiap ide dengan jelas, misalnya dengan sub-judul.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 3 ide plot twist yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Sinopsis Cerita Anda di Sini:" dengan:**
    `Seorang detektif veteran yang dihantui masa lalu harus memburu seorang pembunuh berantai yang meninggalkan teka-teki di setiap TKP. Sang detektif perlahan menyadari bahwa semua korban memiliki hubungan dengan kasus lama yang gagal ia selesaikan.`
---