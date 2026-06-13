## Application Name
Case Study Pro: Problem-Solution-Result Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that turns raw data or project points into a narrative and persuasive case study. Users enter project details, and AI will organize them into a proven effective “Problem-Solution-Result” structure.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Pro Case Study".
2.  **User Input Form:**
    *   A large text area labeled "Enter Your Project Bullet Points or Raw Data:".
3.  **Action Button:** A main button with the text "Create a Case Study". While the process is running, the button should be disabled and display the status "Creating Story...".
4.  **Output Area:**
    *   Title (H3): "Resulting Case Study:"
    *   A single content area to display all case studies.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##` for titles, `**` for bold, and `*` for lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the project data and clicks the "Create Case Study" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis konten pemasaran (marketing content writer) yang ahli dalam menyusun studi kasus yang persuasif dan berorientasi pada hasil.

    Berikut adalah poin-poin atau data mentah dari sebuah proyek:
    """
    [Data dari input pengguna]
    """

    Tugas Anda adalah mengubah data ini menjadi sebuah studi kasus yang naratif dan meyakinkan, dengan mengikuti struktur **Masalah-Solusi-Hasil** yang jelas.

    - **Masalah (The Problem):** Identifikasi dan jelaskan tantangan atau masalah utama yang dihadapi klien sebelum menggunakan solusi Anda.
    - **Solusi (The Solution):** Jelaskan bagaimana produk atau layanan Anda diimplementasikan untuk mengatasi masalah tersebut.
    - **Hasil (The Results):** Paparkan hasil positif yang dicapai. Jika ada data kuantitatif (angka, persentase), tonjolkan data tersebut sebagai bukti keberhasilan.

    Gunakan format Markdown untuk judul, sub-judul, dan poin-poin penting untuk membuat studi kasus ini mudah dibaca dan profesional.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays formatted case studies in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Enter Your Project Bullet Points or Raw Data:" column with:**
    ```
    - Klien: PT. Logistik Cepat
    - Masalah: Proses pelacakan inventaris masih manual menggunakan spreadsheet, sering terjadi human error dan data tidak real-time. Sulit mengetahui stok barang yang akurat.
    - Solusi: Mengimplementasikan sistem manajemen gudang (Warehouse Management System) berbasis web kami.
    - Hasil: Pengurangan human error sebesar 95%, peningkatan efisiensi waktu pencarian barang 80%, visibilitas stok real-time 100% di semua cabang.
    ```
---
