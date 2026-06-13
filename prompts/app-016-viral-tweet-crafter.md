## Nama Aplikasi
Viral Tweet Crafter

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web yang berfungsi sebagai generator konten untuk platform X (Twitter). Pengguna memasukkan sebuah ide, topik, atau link artikel, dan AI akan menghasilkan 3 draf tweet atau thread yang dirancang untuk viralitas, lengkap dengan hashtag yang relevan dan call-to-action.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Viral Tweet Crafter".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Masukkan Ide, Topik, atau Link Artikel Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Buat Draf Tweet". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menyusun...".
4.  **Area Output:**
    *   Judul (H3): "3 Draf Tweet/Thread untuk Anda:"
    *   Sebuah area konten tunggal untuk menampilkan 3 draf. Setiap draf harus dipisahkan dengan jelas.
    *   **Tombol Salin (Copy):** Setiap draf harus memiliki tombol "Salin" individual di sebelahnya.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `**tebal**` dan `*italic*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan ide/link dan mengklik tombol "Buat Draf Tweet".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang Social Media Manager dan ahli growth hacking yang sangat berpengalaman dalam menciptakan konten viral di platform X (Twitter).

    Berdasarkan input berikut:
    """
    [Input dari pengguna]
    """

    Tugas Anda adalah membuat **3 draf tweet atau thread yang berbeda** untuk memaksimalkan engagement (likes, retweets, replies). Setiap draf harus memiliki pendekatan yang unik.

    Untuk setiap draf, sertakan:
    - **Hook yang Kuat:** Kalimat pertama yang provokatif atau membuat penasaran.
    - **Isi yang Padat:** Sajikan informasi utama dengan ringkas.
    - **Hashtag Relevan:** 2-3 hashtag yang relevan.
    - **Call-to-Action (CTA):** Sebuah pertanyaan atau ajakan untuk memancing interaksi.

    Gunakan format Markdown untuk memisahkan setiap draf dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan 3 draf tweet yang sudah diformat di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Masukkan Ide, Topik, atau Link Artikel Anda:" dengan:**
    `Ide: Kebiasaan tidur yang buruk ternyata bisa menurunkan produktivitas kerja lebih dari 50%.`
---