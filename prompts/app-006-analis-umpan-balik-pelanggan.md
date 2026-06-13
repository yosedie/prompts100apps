## Application Name
Customer Feedback Analyst

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an analytical web application capable of summarizing hundreds of customer reviews. Users paste a set of reviews, and the app will analyze them to identify key themes discussed, overall sentiment (positive, negative, or mixed), and provide a list of actionable improvement suggestions.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Customer Feedback Analyst".
2.  **User Input Form:**
    *   A very large text area labeled "Paste all customer reviews here (separate each review with a new line):".
3.  **Action Button:** A main button with the text "Feedback Analysis". While the process is running, the button should be disabled and display the status "Analyzing...".
4.  **Output Area:** Designed like a summary dashboard with three clear sections:
    *   **Section 1: Main Theme:** Heading (H3) "Main Theme" followed by a content area to list the main points.
    *   **Section 2: Sentiment Analysis:** Heading (H3) "Sentiment Analysis" followed by the content area for the sentiment summary paragraph.
    *   **Section 3: Improvement Suggestions:** Heading (H3) "Improvement Suggestions (Actionable)" followed by a content area for a numbered list of suggestions.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `###`, `**`, `*`, and `1.`) into properly formatted HTML elements. Apply this rendering to all three sections in the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user pastes the review text and clicks the “Feedback Analysis” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang analis data dan peneliti pasar yang ahli dalam mengolah data kualitatif dari umpan balik pelanggan.

    Berikut adalah sekumpulan ulasan pelanggan untuk dianalisis:
    """
    [Teks ulasan dari input pengguna]
    """

    Tugas Anda adalah menganalisis semua ulasan tersebut dan menyajikan hasilnya dalam tiga bagian yang jelas:

    ### 1. Tema Utama
    Identifikasi 3-5 tema atau topik utama yang paling sering dibicarakan pelanggan (contoh: Kualitas Produk, Harga, Layanan Pelanggan, Pengiriman). Sajikan dalam bentuk daftar poin.

    ### 2. Analisis Sentimen
    Berikan ringkasan singkat mengenai sentimen keseluruhan dari ulasan tersebut. Apakah cenderung positif, negatif, atau campuran? Sebutkan aspek apa yang paling disukai dan paling tidak disukai.

    ### 3. Saran Perbaikan (Actionable)
    Berdasarkan tema negatif atau keluhan yang muncul, berikan daftar saran perbaikan yang konkret dan bisa ditindaklanjuti oleh tim produk atau bisnis. Sajikan dalam bentuk daftar bernomor.

    Gunakan format Markdown untuk seluruh respons Anda.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the analysis results in three appropriate sections in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste all customer reviews here..." field with:**
    ```
    Kopi dari mesin ini enak sekali, aromanya mantap! Sangat puas.
    Barangnya sampai dengan cepat, tapi bodinya terasa agak ringkih, terlalu banyak plastik.
    Saya suka desainnya yang minimalis, cocok di dapur saya. Tapi suaranya agak berisik saat menggiling kopi.
    Sulit sekali membersihkan wadah ampas kopinya, desainnya kurang praktis.
    Harga sangat terjangkau untuk kualitas kopi yang dihasilkan. Recommended!
    Mesin saya rusak setelah dipakai 2 minggu, layanan pelanggannya lambat merespons.
    Fitur timer otomatisnya sangat membantu di pagi hari.
    ```
---
