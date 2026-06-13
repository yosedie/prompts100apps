## Nama Aplikasi
Asisten "Obrolan Sulit" AI: Difficult Conversation Coach

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pelatih komunikasi. Pengguna mendeskripsikan sebuah percakapan sulit yang harus mereka hadapi, dan AI akan memberikan panduan terstruktur yang mencakup beberapa opsi kalimat pembuka, poin-poin kunci yang harus dibahas, dan tips untuk menjaga agar percakapan tetap produktif dan tidak eskalatif.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Asisten 'Obrolan Sulit' AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Jelaskan percakapan sulit yang harus Anda lakukan:". Berikan placeholder seperti "Contoh 1: Saya perlu memberitahu rekan kerja bahwa kualitas pekerjaannya menurun. Contoh 2: Saya ingin meminta kenaikan gaji kepada atasan saya."
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Siapkan Strategi Percakapan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun Strategi...".
4.  **Area Output:**
    *   Judul (H3): "Strategi Percakapan Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh panduan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi percakapan dan mengklik tombol "Siapkan Strategi Percakapan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pelatih komunikasi (communication coach) dan ahli resolusi konflik yang empatik dan strategis.

    Berdasarkan deskripsi percakapan sulit berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah membuat panduan yang jelas dan dapat ditindaklanjuti. Panduan harus mencakup tiga bagian utama:

    1.  **Opsi Kalimat Pembuka:** Berikan 2-3 opsi kalimat pembuka yang berbeda (misalnya, satu langsung, satu lebih lembut) untuk memulai percakapan dengan cara yang tidak konfrontatif.
    2.  **Poin-Poin Kunci untuk Dibahas:** Buat daftar poin-poin utama yang harus disampaikan oleh pengguna untuk memastikan pesannya jelas dan didukung oleh fakta atau perasaan (menggunakan metode "I-message").
    3.  **Tips Menjaga Percakapan Tetap Produktif:** Berikan beberapa saran tentang cara menjaga nada bicara, mendengarkan secara aktif, dan menghindari eskalasi konflik.

    Gunakan format Markdown untuk menyusun panduan dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan panduan strategi di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan percakapan sulit yang harus Anda lakukan:" dengan:**
    `Saya harus memberitahu rekan satu tim saya, Budi, bahwa dia sering terlambat mengumpulkan pekerjaannya, yang berdampak pada seluruh tim. Saya tidak ingin merusak hubungan kerja kami.`
---