## Nama Aplikasi
Text Adventure RPG AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web interaktif yang berfungsi sebagai permainan petualangan berbasis teks (text-based RPG). AI akan berperan sebagai Game Master (GM), mendeskripsikan dunia dan skenario, sementara pengguna mengetikkan tindakan yang ingin mereka lakukan. AI akan merespons tindakan tersebut dan melanjutkan cerita.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Text Adventure RPG AI".
2.  **Layar Pengaturan Awal (Setup Screen):**
    *   **Pilihan Skenario:** Sebuah menu dropdown (select) dengan label "Pilih Skenario Petualangan:" dan opsi: "Detektif Noir di Kota Hujan", "Penjelajah Luar Angkasa di Kapal Terbengkalai", "Penyihir Muda di Hutan Terlarang".
    *   **Tombol Mulai:** Sebuah tombol utama dengan teks "Mulai Petualangan!".
3.  **Layar Permainan (Game Screen, setelah setup):**
    *   **Jendela Cerita:** Sebuah area konten utama yang menampilkan riwayat narasi dari AI dan tindakan dari pengguna, seperti log percakapan.
    *   **Input Tindakan:** Sebuah kolom input teks di bagian bawah dengan label "Apa yang kamu lakukan?".
    *   **Tombol Kirim:** Tombol untuk mengirim tindakan pengguna.
    *   **Tombol Restart:** Tombol untuk kembali ke Layar Pengaturan Awal.
4.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*` untuk deskripsi suasana) menjadi elemen HTML yang diformat dengan benar.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih skenario dan mengklik "Mulai Petualangan!".
2.  Aplikasi mengirimkan *prompt sistem awal* ke model AI untuk memulai cerita.
3.  **Logika Percakapan (Sangat Penting):**
    *   Setiap kali pengguna mengirimkan tindakan, aplikasi harus mengirim **seluruh riwayat percakapan** (narasi AI sebelumnya + tindakan pengguna) kembali ke model AI. Ini memungkinkan AI untuk mengingat konteks dan merespons secara koheren.
    *   Aplikasi kemudian menambahkan respons baru dari AI ke Jendela Cerita.

4.  **Prompt Sistem Awal (Initial System Prompt):**
    ```
    Anda adalah seorang Game Master (GM) yang ahli untuk permainan petualangan berbasis teks. Tugas Anda adalah menciptakan cerita yang imersif dan interaktif.

    Aturan Anda:
    1.  Deskripsikan dunia dengan detail yang kaya (pemandangan, suara, bau).
    2.  Hadirkan tantangan, teka-teki, dan karakter non-pemain (NPC).
    3.  Respons secara realistis terhadap tindakan yang ditulis oleh pengguna.
    4.  Selalu akhiri respons Anda dengan pertanyaan "Apa yang kamu lakukan?" untuk memancing input dari pengguna.

    Berdasarkan skenario yang dipilih: "[Skenario dari pilihan pengguna]"

    Mulailah sekarang dengan menulis paragraf pembuka yang menarik untuk memulai petualangan.
    ```
5.  Aplikasi menampilkan respons pertama di Jendela Cerita, dan menunggu input tindakan dari pengguna.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, atur pilihan default pada menu dropdown saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Skenario Petualangan:" ke:**
    `Detektif Noir di Kota Hujan`
---