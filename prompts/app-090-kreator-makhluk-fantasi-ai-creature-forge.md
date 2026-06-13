## Nama Aplikasi
Kreator Makhluk Fantasi AI: Creature Forge

## Konfigurasi & Atribusi
*   **Model AI Target:** Gemini 2.5 Pro
*   **Pembuat:** yosedie

---

## Ringkasan Proyek
Bangun sebuah aplikasi web untuk para world-builder yang secara otomatis merancang makhluk fantasi unik. Pengguna mendeskripsikan sebuah lingkungan atau habitat, dan AI akan menciptakan makhluk yang logis untuk hidup di sana, lengkap dengan deskripsi fisik, perilaku, dan perannya dalam ekosistem fiktif tersebut.

## Komponen Antarmuka Pengguna (UI Components)

1.  **Header:** Judul besar bertuliskan "Kreator Makhluk Fantasi AI".
2.  **Form Input Pengguna:**
    *   Sebuah area teks (textarea) yang besar dengan label "Jelaskan Lingkungan atau Habitat Fiktif Anda:".
3.  **Tombol Aksi:** Sebuah tombol utama dengan teks "Ciptakan Makhluk!". Saat proses berjalan, tombol harus dinaktifkan dan menampilkan status "Menciptakan...".
4.  **Area Output:**
    *   Judul (H3): "Makhluk yang Dihasilkan:"
    *   Sebuah area konten tunggal untuk menampilkan seluruh deskripsi makhluk.
    *   **Tombol Salin (Copy):** Harus ada tombol "Salin Teks" di sebelah area output.
5.  **Footer:** Sebuah footer sederhana berisi tautan (hyperlink) dengan teks **'Created by yosedie'**. Tautan ini harus mengarah ke URL `https://github.com/yosedie` dan terbuka di tab baru.

## Persyaratan Rendering Konten

*   **Render Markdown ke HTML:** Aplikasi **wajib** mem-parsing respons teks dari AI sebelum menampilkannya di UI. Gunakan library JavaScript seperti `marked.js` atau yang setara untuk mengubah semua sintaks Markdown (seperti `##`, `**`, dan `*`) menjadi elemen HTML yang diformat dengan benar. Terapkan rendering ini pada Area Output.

## Alur Kerja & Logika (Workflow & Logic)

1.  Pengguna memasukkan deskripsi habitat dan mengklik tombol "Ciptakan Makhluk!".
2.  Aplikasi membuat sebuah *prompt* terstruktur untuk dikirim ke model AI.
    ```
    Anda adalah seorang ahli ekologi fiksi dan xenobiologist. Anda ahli dalam merancang makhluk hidup yang beradaptasi secara logis dengan lingkungan mereka yang fantastis.

    Berdasarkan deskripsi habitat berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah merancang SATU makhluk unik yang hidup di habitat ini. Deskripsi makhluk harus mencakup:

    1.  **Nama Makhluk:** Berikan nama yang terdengar pas untuk makhluk tersebut.
    2.  **Deskripsi Fisik:** Jelaskan penampilan, ukuran, dan fitur-fitur uniknya. Jelaskan bagaimana fisiknya merupakan adaptasi terhadap habitatnya.
    3.  **Perilaku & Makanan:** Jelaskan bagaimana perilakunya (nokturnal, soliter, dll.) dan apa yang dimakannya.
    4.  **Peran dalam Ekosistem:** Jelaskan posisinya dalam rantai makanan atau perannya dalam ekosistem (misalnya, penyerbuk, dekomposer, predator puncak).

    Gunakan format Markdown untuk menyusun deskripsi dengan rapi.
    ```
3.  Aplikasi mengirimkan prompt ini ke API model **Gemini 2.5 Pro**.
4.  Setelah menerima respons, aplikasi merender konten Markdown dari respons tersebut menjadi HTML.
5.  Aplikasi menampilkan deskripsi makhluk di Area Output.

---
## Skenario Pengujian Cepat (Quick Test Scenario)

**Untuk memungkinkan pengujian langsung, isi otomatis area input dengan data contoh berikut saat halaman pertama kali dimuat:**

*   **Isi kolom "Jelaskan Lingkungan atau Habitat Fiktif Anda:" dengan:**
    `Sebuah rawa-rawa yang airnya bercahaya karena mineral aneh, dipenuhi oleh jamur-jamur raksasa yang memancarkan spora berkilauan.`
---