## Nama Aplikasi
Simulator Negosiasi AI: Negotiation Coach

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web interaktif yang berfungsi sebagai simulator untuk melatih kemampuan negosiasi. Pengguna mendefinisikan sebuah skenario dan peran mereka, lalu AI akan berperan sebagai lawan negosiasi, memberikan penawaran dan argumen balasan secara dinamis dalam format percakapan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Simulator Negosiasi AI".
2.  **Layar Pengaturan Awal (Setup Screen):**
    *   **Input Skenario:** Sebuah kolom input teks dengan label "Jelaskan Skenario Negosiasi Anda:".
    *   **Input Peran Anda:** Sebuah kolom input teks dengan label "Apa Peran Anda?".
    *   **Input Peran AI:** Sebuah kolom input teks dengan label "Apa Peran AI sebagai Lawan Negosiasi?".
    *   **Input Pembuka:** Sebuah area teks (textarea) dengan label "Tulis Tawaran atau Kalimat Pembuka Anda:".
    *   **Tombol Mulai:** Sebuah tombol utama dengan teks "Mulai Negosiasi!".
3.  **Layar Negosiasi (Setelah Setup):**
    *   **Jendela Percakapan:** Area utama yang menampilkan riwayat negosiasi (seperti chat).
    *   **Input Balasan:** Kolom input teks di bawah dengan label "Balasan Anda:".
    *   **Tombol Kirim:** Tombol untuk mengirim balasan.
    *   **Tombol Restart:** Tombol untuk kembali ke Layar Pengaturan Awal.
4.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown menjadi elemen HTML yang diformat dengan benar.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail skenario di Layar Pengaturan dan mengklik "Mulai Negosiasi!".
2.  Aplikasi membuat sebuah *prompt sistem awal* yang akan menjadi dasar peran AI.
3.  **Logika Percakapan (Penting):**
    *   Aplikasi harus menyimpan seluruh riwayat percakapan.
    *   Setiap kali pengguna mengirim balasan, aplikasi harus mengirim **seluruh riwayat percakapan** ditambah *prompt sistem awal* ke model AI untuk menjaga konteks.
    *   Respons baru dari AI kemudian ditambahkan ke Jendela Percakapan.

4.  **Prompt Sistem Awal (Initial System Prompt):**
    ```
    Anda adalah seorang negosiator ahli yang berperan sebagai [Peran AI dari input pengguna]. Tujuan Anda adalah untuk mendapatkan hasil terbaik bagi pihak Anda, namun tetap bersikap realistis dan profesional.

    Skenario negosiasinya adalah tentang [Skenario dari input pengguna]. Lawan negosiasi Anda (pengguna) berperan sebagai [Peran Pengguna dari input pengguna].

    Respons setiap argumen atau tawaran dari pengguna dengan argumen balasan yang logis. Jangan terlalu cepat menyerah. Berikan penawaran balasan jika perlu. Mulai sekarang, respons pesan pertama dari pengguna.
    ```
5.  Aplikasi menampilkan kalimat pembuka pengguna dan respons pertama AI di Jendela Percakapan, lalu menunggu balasan pengguna selanjutnya.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input di Layar Pengaturan Awal dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Skenario Negosiasi Anda:" dengan:**
    `Negosiasi harga mobil bekas.`
*   **Isi kolom "Apa Peran Anda?" dengan:**
    `Pembeli yang cermat dan ingin harga serendah mungkin.`
*   **Isi kolom "Apa Peran AI sebagai Lawan Negosiasi?" dengan:**
    `Penjual mobil bekas yang berpengalaman dan ingin harga setinggi mungkin.`
*   **Isi kolom "Tulis Tawaran atau Kalimat Pembuka Anda:" dengan:**
    `Saya lihat mobil ini diiklankan seharga 150 juta. Kondisinya bagus, tapi saya lihat ada beberapa goresan kecil di pintu. Saya tawar 135 juta.`
---