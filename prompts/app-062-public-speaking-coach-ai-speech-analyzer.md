## Nama Aplikasi
Public Speaking Coach AI: Speech Analyzer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai pelatih public speaking virtual. Pengguna menempelkan draf pidato mereka, dan AI akan menganalisisnya untuk memberikan saran konkret tentang cara membuatnya lebih berdampak, termasuk saran untuk kalimat pembuka dan penutup, serta di mana harus memberikan jeda untuk penekanan.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Public Speaking Coach AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Tempelkan Draf Pidato Anda di Sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Analisis Pidato Saya". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:**
    *   Judul (H3): "Saran & Masukan untuk Pidato Anda:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh analisis.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan draf pidato dan mengklik tombol "Analisis Pidato Saya".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang pelatih public speaking dan komunikasi kelas dunia. Anda ahli dalam mengubah pidato yang biasa menjadi luar biasa.

    Berikut adalah draf pidato yang perlu dianalisis:
    """
    [Teks pidato dari input pengguna]
    """

    Tugas Anda adalah memberikan masukan yang konstruktif dan dapat ditindaklanjuti. Sajikan analisis Anda dalam beberapa bagian yang jelas:

    1.  **Saran untuk Pembukaan:** Bagaimana cara membuat kalimat pembuka lebih menarik dan langsung mengait perhatian audiens?
    2.  **Saran untuk Penutup:** Bagaimana cara membuat kalimat penutup lebih kuat, berkesan, dan menginspirasi?
    3.  **Saran Penekanan & Jeda:** Tunjukkan beberapa kalimat atau frasa kunci dalam pidato di mana pembicara harus memberikan jeda sejenak (pause) untuk efek dramatis atau penekanan.
    4.  **Peningkatan Bahasa:** Sarankan beberapa kata atau frasa yang bisa diganti untuk membuatnya lebih persuasif atau berdampak.

    Gunakan format Markdown untuk menyusun analisis dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan analisis yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan Draf Pidato Anda di Sini:" dengan:**
    `Selamat pagi semuanya. Terima kasih sudah datang. Hari ini saya akan berbicara tentang proyek baru kita. Proyek ini penting untuk perusahaan. Kita sudah bekerja keras dan hasilnya cukup bagus. Mari kita terus bekerja sama. Terima kasih.`
---