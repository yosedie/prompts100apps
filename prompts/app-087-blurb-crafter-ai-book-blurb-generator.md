## Nama Aplikasi
Blurb Crafter AI: Book Blurb Generator

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para penulis yang secara otomatis menciptakan blurb (teks sampul belakang buku) yang menarik. Pengguna memasukkan sinopsis singkat cerita mereka, dan AI akan menulis 3 pilihan blurb yang menegangkan, membuat penasaran, dan dirancang untuk membuat pembaca ingin membeli buku tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Blurb Crafter AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Sinopsis Singkat Cerita Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Blurb!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menulis...".
4.  **Area Output:**
    *   Judul (H3): "3 Pilihan Blurb Untuk Buku Anda:"
    *   Sebuah area konten tunggal untuk menampilkan 3 pilihan blurb. Setiap pilihan harus dipisahkan dengan jelas.
    *   **Tombol Salin (Copy):** Setiap pilihan blurb harus memiliki tombol "Salin" individual di sebelahnya.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `---` atau `**`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan sinopsis dan mengklik tombol "Buat Blurb!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang editor akuisisi di sebuah penerbit besar dan seorang copywriter ahli. Anda tahu persis bagaimana cara menulis blurb yang menjual buku.

    Berdasarkan sinopsis cerita berikut:
    """
    [Sinopsis dari input pengguna]
    """

    Tugas Anda adalah menulis **3 pilihan blurb yang berbeda**. Setiap blurb harus:
    - Memperkenalkan protagonis dan konflik utama.
    - Membangun ketegangan dan misteri.
    - TIDAK membocorkan akhir cerita.
    - Berakhir dengan sebuah 'hook' atau pertanyaan yang membuat pembaca sangat penasaran.

    Gunakan format Markdown untuk memisahkan setiap pilihan blurb dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 3 pilihan blurb di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Sinopsis Singkat Cerita Anda:" dengan:**
    `Seorang ahli bahasa kuno bernama Dr. Aris menemukan sebuah artefak yang memuat peta ke kota mitos Atlantis. Namun, sebuah organisasi rahasia yang dikenal sebagai 'The Order' juga menginginkan peta itu untuk menguasai teknologi kuno Atlantis. Aris harus memecahkan teka-teki peta sambil melarikan diri dari kejaran agen-agen The Order yang mematikan.`
---