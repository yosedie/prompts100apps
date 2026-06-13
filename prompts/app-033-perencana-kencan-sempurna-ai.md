## Nama Aplikasi
Perencana Kencan Sempurna AI

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai perencana kencan pribadi. Pengguna memasukkan minat pasangan, budget, dan suasana yang diinginkan, lalu AI akan merancang sebuah itinerary kencan yang unik, personal, dan lengkap dari awal hingga akhir.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Perencana Kencan Sempurna AI".
2.  **Form Input Pengguna:**
    *   **Input Minat:** Sebuah area teks (textarea) dengan label "Apa minat pasangan Anda? (contoh: seni, alam, kuliner, film, musik)".
    *   **Pilihan Budget:** Sebuah menu dropdown (select) dengan label "Budget Kencan:" dan opsi: "Hemat (di bawah 200rb)", "Sedang (200rb - 500rb)", "Spesial (di atas 500rb)".
    *   **Pilihan Suasana:** Sebuah menu dropdown (select) dengan label "Suasana yang Diinginkan:" dan opsi: "Romantis & Tenang", "Seru & Aktif", "Santai & Kasual", "Unik & Anti-Mainstream".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Rancang Kencan Sempurna!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Merancang Momen...".
4.  **Area Output:**
    *   Judul (H3): "Rencana Kencan Spesial Untukmu:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh rencana.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna mengisi detail kencan dan mengklik tombol "Rancang Kencan Sempurna!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang perencana kencan (date planner) yang kreatif, romantis, dan sangat detail.

    Berdasarkan kriteria berikut:
    - Minat Pasangan: [Minat dari input pengguna]
    - Budget: [Budget dari pilihan pengguna]
    - Suasana Kencan: [Suasana dari pilihan pengguna]

    Tugas Anda adalah merancang SATU ide kencan yang lengkap dan personal. Rencana tersebut harus mencakup:
    1.  **Nama Kencan:** Berikan judul yang kreatif untuk ide kencan ini.
    2.  **Ringkasan Singkat:** Jelaskan secara singkat mengapa kencan ini cocok.
    3.  **Itinerary Lengkap:** Buat jadwal langkah-demi-langkah (misal: Aktivitas Sore, Makan Malam, Aktivitas Malam). Untuk setiap langkah, jelaskan aktivitasnya dan berikan estimasi biaya agar sesuai dengan budget.

    Pastikan seluruh rencana sesuai dengan minat, budget, dan suasana yang dipilih. Gunakan format Markdown untuk menyusun rencana dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan rencana kencan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Apa minat pasangan Anda?..." dengan:**
    `Suka seni, mengunjungi galeri, minum kopi, dan mendengarkan musik jazz.`
*   **Atur pilihan "Budget Kencan:" ke:**
    `Sedang (200rb - 500rb)`
*   **Atur pilihan "Suasana yang Diinginkan:" ke:**
    `Romantis & Tenang`
---