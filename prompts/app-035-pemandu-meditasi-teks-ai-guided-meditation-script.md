## Nama Aplikasi
Pemandu Meditasi Teks AI: Guided Meditation Script

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai generator naskah meditasi terpandu. Pengguna memilih tema dan durasi, dan AI akan menghasilkan sebuah naskah yang menenangkan dan siap dibacakan, lengkap dengan arahan untuk jeda dan pernapasan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pemandu Meditasi Teks AI".
2.  **Form Input Pengguna:**
    *   **Input Tema:** Sebuah kolom input teks dengan label "Pilih Tema Meditasi Anda:".
    *   **Pilihan Durasi:** Sebuah menu dropdown (select) dengan label "Pilih Durasi Sesi:" dan opsi: "Singkat (3 Menit)", "Sedang (5 Menit)", "Panjang (10 Menit)".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Naskah Meditasi". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menenangkan Pikiran...".
4.  **Area Output:**
    *   Judul (H3): "Naskah Meditasi Terpandu:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh naskah.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*` untuk arahan) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memilih tema, durasi, dan mengklik tombol "Buat Naskah Meditasi".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pemandu meditasi dan instruktur mindfulness yang berpengalaman. Suara tulisan Anda tenang, lembut, dan menenangkan.

    Berdasarkan kriteria berikut:
    - Tema Meditasi: [Tema dari input pengguna]
    - Durasi Sesi: [Durasi dari pilihan pengguna]

    Tugas Anda adalah menulis naskah meditasi terpandu yang lengkap. Naskah harus memiliki struktur yang jelas:
    1.  **Pembukaan:** Ajak pendengar untuk menemukan posisi yang nyaman dan fokus pada napas.
    2.  **Isi Utama:** Pandu pendengar melalui visualisasi atau latihan kesadaran yang sesuai dengan tema yang diberikan.
    3.  **Penutup:** Bawa kembali kesadaran pendengar secara perlahan ke ruangan dan berikan afirmasi positif.

    PENTING: Gunakan arahan dalam tanda kurung dan teks miring untuk menandakan jeda atau instruksi non-verbal. Contoh: *(jeda sejenak)* atau *(tarik napas dalam-dalam)*. Pastikan panjang naskah sesuai dengan durasi yang diminta.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan naskah meditasi yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Pilih Tema Meditasi Anda:" dengan:**
    `Mengurangi stres sebelum tidur`
*   **Atur pilihan "Pilih Durasi Sesi:" ke:**
    `Sedang (5 Menit)`
---