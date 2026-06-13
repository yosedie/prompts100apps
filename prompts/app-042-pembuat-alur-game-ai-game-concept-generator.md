## Nama Aplikasi
Pembuat Alur Game AI: Game Concept Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para desainer game dan penulis. Pengguna memasukkan genre game dan satu kalimat ide utama, lalu AI akan menghasilkan konsep game yang lebih utuh, termasuk judul, mekanik inti, dan alur cerita dasar.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pembuat Alur Game AI".
2.  **Form Input Pengguna:**
    *   **Pilihan Genre:** Sebuah menu dropdown (select) dengan label "Pilih Genre Game:" dan opsi: "RPG Fantasi", "Petualangan Sci-Fi", "Horor Psikologis", "Puzzle Platformer", "Strategi".
    *   **Input Ide Utama:** Sebuah kolom input teks dengan label "Ide Utama Game (1 Kalimat):".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Konsep Game!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Developing...".
4.  **Area Output:**
    *   Judul (H3): "Konsep Game Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh konsep.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih genre, memasukkan ide, dan mengklik tombol "Buat Konsep Game!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang desainer game (game designer) dan penulis naratif yang berpengalaman.

    Berdasarkan informasi awal berikut:
    - Genre: [Genre dari pilihan pengguna]
    - Ide Utama: [Ide dari input pengguna]

    Tugas Anda adalah mengembangkan ide singkat ini menjadi konsep game yang lebih konkret. Konsep tersebut harus mencakup:

    1.  **Judul Game (Working Title):** Berikan satu judul yang menarik.
    2.  **Konsep Inti (Core Concept):** Tulis satu paragraf singkat yang menjelaskan premis utama game.
    3.  **Mekanik Utama (Core Mechanic):** Jelaskan secara singkat apa yang dilakukan pemain dalam game (gameplay loop).
    4.  **Alur Cerita Dasar (Basic Plot Outline):** Buat kerangka cerita sederhana dalam tiga babak: Awal (pengenalan konflik), Tengah (eskalasi dan tantangan), dan Akhir (klimaks dan resolusi).

    Gunakan format Markdown untuk menyusun konsep dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan konsep game yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Atur pilihan "Pilih Genre Game:" ke:**
    `RPG Fantasi`
*   **Isi kolom "Ide Utama Game (1 Kalimat):" dengan:**
    `Seorang pustakawan menemukan bahwa buku-buku di perpustakaan kuno bisa mengubah realitas.`
---