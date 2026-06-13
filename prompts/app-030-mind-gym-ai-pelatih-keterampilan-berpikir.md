## Nama Aplikasi
Mind Gym AI: Pelatih Keterampilan Berpikir

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web interaktif yang berfungsi sebagai pelatih untuk mengasah keterampilan berpikir. Pengguna memilih jenis keterampilan yang ingin dilatih (kritis, lateral, atau sistemik), dan AI akan memberikan sebuah skenario atau teka-teki yang dirancang khusus untuk melatih keterampilan tersebut, lengkap dengan opsi untuk meminta petunjuk dan melihat jawaban.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Mind Gym AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Keterampilan:** Sebuah menu dropdown (select) dengan label "Pilih Keterampilan yang Ingin Dilatih:" dan opsi: "Berpikir Kritis", "Berpikir Lateral", "Berpikir Sistemik".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Mulai Latihan". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Merancang Latihan...".
4.  **Area Output yang Interaktif:**
    *   **Skenario:** Judul (H3) "Skenario Latihan:" diikuti area konten untuk menampilkan teka-teki dari AI.
    *   **Tombol Petunjuk:** Sebuah tombol dengan teks "Minta Petunjuk". Saat diklik, sebuah area tersembunyi di bawahnya akan muncul menampilkan petunjuk.
    *   **Tombol Jawaban:** Sebuah tombol dengan teks "Tampilkan Jawaban & Penjelasan". Saat diklik, sebuah area tersembunyi di bawahnya akan muncul menampilkan jawaban lengkap.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada semua bagian di Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih keterampilan dan mengklik tombol "Mulai Latihan".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang fasilitator dan pelatih keterampilan berpikir (thinking skills coach) yang ahli dalam merancang skenario dan teka-teki yang menantang.

    Berdasarkan keterampilan yang dipilih:
    - Keterampilan: [Keterampilan dari pilihan pengguna]

    Tugas Anda adalah membuat TIGA bagian konten yang terpisah:
    1.  **Skenario/Teka-Teki:** Buat sebuah skenario atau teka-teki yang dirancang khusus untuk melatih keterampilan yang dipilih.
        - Untuk 'Berpikir Kritis', berikan skenario dengan informasi yang mungkin bias atau tidak lengkap.
        - Untuk 'Berpikir Lateral', berikan teka-teki klasik yang membutuhkan solusi "out-of-the-box".
        - Untuk 'Berpikir Sistemik', berikan skenario tentang sistem yang saling terhubung dan tanyakan tentang konsekuensi yang tidak terduga.
    2.  **Petunjuk (Hint):** Berikan satu kalimat petunjuk yang mengarahkan pemikiran tanpa memberikan jawaban.
    3.  **Jawaban & Penjelasan:** Berikan jawaban yang jelas, dan yang terpenting, jelaskan MENGAPA jawaban itu benar dan BAGAIMANA cara berpikir yang benar digunakan untuk mencapainya.

    Gunakan format berikut dengan pemisah yang jelas:
    [Teks Skenario/Teka-Teki Anda di sini]
    ---HINT---
    [Teks Petunjuk Anda di sini]
    ---SOLUTION---
    [Teks Jawaban & Penjelasan Anda di sini]
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi mem-parsing teks tersebut menggunakan pemisah `---HINT---` dan `---SOLUTION---` untuk memisahkan ketiga bagian konten.
5.  Aplikasi menampilkan skenario utama, dan menyimpan petunjuk serta jawaban untuk ditampilkan saat tombol yang sesuai diklik.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, atur pilihan default pada menu dropdown saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Keterampilan yang Ingin Dilatih:" ke:**
    `Berpikir Kritis`
---