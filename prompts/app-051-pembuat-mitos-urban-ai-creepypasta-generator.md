## Nama Aplikasi
Pembuat Mitos Urban AI: Creepypasta Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang menciptakan cerita legenda urban atau creepypasta baru yang menyeramkan. Pengguna memasukkan sebuah lokasi atau objek yang umum, dan AI akan menulis sebuah cerita horor pendek yang terasa seperti mitos yang bisa menyebar dari mulut ke mulut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Pembuat Mitos Urban AI".
2.  **Form Input Pengguna:**
    *   Sebuah kolom input teks dengan label "Lokasi atau Objek Apa yang Menyimpan Kisah Seram?".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ciptakan Mitos". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Membisikkan Cerita...".
4.  **Area Output:**
    *   Judul (H3): "Legenda Urban yang Baru:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh cerita.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `*italic*` untuk penekanan) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan lokasi/objek dan mengklik tombol "Ciptakan Mitos".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pencerita horor ulung dan penulis creepypasta. Anda ahli dalam mengambil hal-hal biasa dan membuatnya terasa sangat menyeramkan.

    Berdasarkan lokasi/objek berikut:
    """
    [Input dari pengguna]
    """

    Tugas Anda adalah menulis sebuah cerita legenda urban atau creepypasta pendek yang baru dan orisinal. Cerita harus:
    - Dimulai dengan suasana yang normal dan familiar.
    - Memperkenalkan elemen yang aneh atau tidak pada tempatnya secara perlahan.
    - Membangun ketegangan dan rasa takut.
    - Berakhir dengan kesimpulan yang mengerikan atau pertanyaan yang menghantui.

    Gaya tulisan harus terasa personal, seolah-olah ini adalah cerita yang "benar-benar terjadi" dan diceritakan kembali. Gunakan format Markdown untuk penekanan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan cerita yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis kolom input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Lokasi atau Objek Apa yang Menyimpan Kisah Seram?" dengan:**
    `Jembatan penyeberangan orang di malam hari`
---