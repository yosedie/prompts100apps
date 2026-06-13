## Nama Aplikasi
Jurnal Awam AI: Perangkum Jurnal Ilmiah

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai penerjemah sains. Pengguna menempelkan abstrak atau teks lengkap dari sebuah jurnal ilmiah yang padat dan teknis, dan AI akan merangkumnya menjadi penjelasan yang mudah dipahami oleh orang awam, tanpa menghilangkan esensi temuan utamanya.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Jurnal Awam AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Abstrak atau Teks Jurnal Ilmiah di Sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Rangkum untuk Awam". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menerjemahkan Sains...".
4.  **Area Output:**
    *   Judul (H3): "Ringkasan Sederhana:"
    *   Sebuah area konten tunggal untuk menampilkan ringkasan.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan teks jurnal dan mengklik tombol "Rangkum untuk Awam".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang komunikator sains (science communicator) yang sangat berbakat. Anda mampu memahami penelitian ilmiah yang kompleks dan menjelaskannya kepada audiens non-ahli dengan cara yang menarik dan mudah dimengerti.

    Berikut adalah teks dari sebuah jurnal ilmiah:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah merangkum teks ini untuk orang awam. Ringkasan Anda harus:
    - Menghindari jargon teknis. Jika terpaksa digunakan, jelaskan dengan analogi sederhana.
    - Fokus pada "gambaran besar": Apa pertanyaan utama penelitian ini? Apa temuan utamanya? Mengapa ini penting?
    - Disajikan dalam bentuk narasi yang mengalir, bukan poin-poin teknis.

    Gunakan format Markdown untuk penekanan pada istilah-istilah kunci yang telah Anda sederhanakan.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan ringkasan yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Abstrak atau Teks Jurnal Ilmiah di Sini:" dengan:**
    `Abstrak: Penelitian ini menginvestigasi efek neuroprotektif dari kurkumin terhadap stres oksidatif yang diinduksi oleh glutamat pada kultur sel hipokampus. Hasil menunjukkan bahwa pra-perlakuan dengan kurkumin secara signifikan menekan produksi spesies oksigen reaktif (ROS) dan apoptosis seluler. Data kami mengindikasikan bahwa kurkumin dapat menjadi agen terapeutik potensial untuk gangguan neurodegeneratif yang dimediasi oleh eksitotoksisitas.`
---