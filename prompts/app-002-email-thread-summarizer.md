## Nama Aplikasi
Email Thread Summarizer

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi untuk meringkas utas email yang panjang. Pengguna menempelkan seluruh konten email ke dalam area input, dan aplikasi akan menganalisisnya untuk menghasilkan ringkasan utama dalam 3 poin serta daftar tugas (action items) lengkap dengan penanggung jawabnya dalam format tabel.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Email Thread Summarizer".
2.  **Area Input:**
    *   Sebuah area teks (textarea) yang besar dan tinggi dengan label "Tempelkan seluruh utas email di sini:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ringkas Sekarang!". Saat proses berjalan, tombol harus dinonaktifkan dan menampilkan status "Menganalisis...".
4.  **Area Output:** Dibagi menjadi dua bagian yang jelas:
    *   **Bagian Ringkasan:**
        *   Judul (H3): "Ringkasan Utama"
        *   Area konten untuk menampilkan 3 poin ringkasan dalam format daftar bernomor.
    *   **Bagian Action Items:**
        *   Judul (H3): "Action Items"
        *   Area konten untuk menampilkan tabel tugas dan penanggung jawab.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (terutama daftar bernomor dan tabel) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada kedua bagian di Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna menempelkan teks utas email dan mengklik tombol "Ringkas Sekarang!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang asisten eksekutif AI yang sangat efisien, berspesialisasi dalam menganalisis utas email yang panjang dan mengekstrak informasi paling penting.

    Berikut adalah utas email untuk dianalisis:
    """
    [Utas email dari input pengguna]
    """

    Tugas Anda adalah:
    1.  **Ringkasan Utama:** Sajikan 3 poin ringkasan utama dari keseluruhan diskusi.
    2.  **Action Items:** Identifikasi semua tugas spesifik (action items), siapa yang bertanggung jawab (penanggung jawab), dan sajikan dalam format tabel yang jelas.

    Gunakan Markdown untuk format. Untuk tabel, gunakan format Markdown table dengan header "Tugas (Action Item)" dan "Penanggung Jawab (PIC)".
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi mem-parsing teks tersebut, memisahkan bagian ringkasan dan bagian tabel action items.
5.  Aplikasi merender konten Markdown dari setiap bagian menjadi HTML, lalu menampilkannya di area output yang sesuai.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Tempelkan seluruh utas email di sini:" dengan:**
    ```
    From: Andi (Project Manager)
    To: Tim Proyek Phoenix
    Subject: Status Terkini Proyek Phoenix

    Halo tim,

    Saya ingin mengecek status terkini untuk Proyek Phoenix yang deadline-nya semakin dekat. Kita sepertinya sedikit tertinggal dari jadwal. Mohon update dari masing-masing penanggung jawab.

    Terima kasih,
    Andi

    ---
    From: Budi (Developer)
    To: Tim Proyek Phoenix
    Subject: Re: Status Terkini Proyek Phoenix

    Hai Andi,

    Untuk bagian backend, API utama sudah selesai 100%. Saya sekarang sedang menunggu aset desain final dari Citra untuk bisa melanjutkan integrasi ke antarmuka pengguna.

    Salam,
    Budi

    ---
    From: Citra (Designer)
    To: Tim Proyek Phoenix
    Subject: Re: Status Terkini Proyek Phoenix

    Mohon maaf atas keterlambatannya. Ada beberapa revisi minor dari klien. Mockup final sudah siap dan akan saya unggah ke folder Google Drive bersama semua asetnya paling lambat sore ini.

    Terima kasih,
    Citra

    ---
    From: Andi (Project Manager)
    To: Tim Proyek Phoenix
    Subject: Re: Status Terkini Proyek Phoenix

    Baik, terima kasih atas updatenya Budi dan Citra.

    Kalau begitu, Budi, tolong segera mulai proses integrasi setelah aset dari Citra tersedia. Saya sendiri akan memperbarui timeline proyek di Asana dan melaporkannya ke manajemen.

    Kerja bagus semua!
    Andi
    ```
---