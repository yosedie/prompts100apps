## Application Name
AI Fake Product Review Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that generates detailed, authentic-sounding fake product reviews for testing or sampling purposes. Users enter the product name and select a sentiment, then the AI ​​will write a complete review as if it were from a real customer.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Fake Product Review Generator".
2.  **User Input Form:**
    *   **Input Product Name:** A text input field labeled "Fictitious Product Name:".
    *   **Sentiment Selection:** A dropdown (select) menu with the label "Select Review Sentiment:" and options: "Positive (5 Stars)", "Negative (1 Star)", "Balanced (3 Stars)".
3.  **Action Button:** A main button with the text "Write a Review". While the process is running, the button should be activated and display the status "Writing...".
4.  **Output Area:**
    *   Headline (H3): "Resulted Product Review:"
    *   A single content area to display all reviews.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the product name, selects a sentiment, and clicks the “Write a Review” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis yang sangat pandai meniru gaya tulisan ulasan produk online. Anda bisa menulis ulasan yang terdengar sangat otentik dan detail.

    Berdasarkan informasi berikut:
    - Nama Produk: [Nama produk dari input pengguna]
    - Sentimen yang Diinginkan: [Sentimen dari pilihan pengguna]

    Tugas Anda adalah menulis SATU ulasan produk palsu yang detail. Ulasan harus memiliki:
    - **Judul Ulasan:** Sebuah judul yang menarik dan sesuai dengan sentimen.
    - **Isi Ulasan:** Beberapa paragraf yang menjelaskan pengalaman "pengguna". Sebutkan detail spesifik (baik atau buruk) tentang fitur, desain, atau penggunaan produk.
    - **Rating Bintang:** Tampilkan rating bintang yang sesuai di akhir (misal: ★★★★★ untuk positif).

    Pastikan gaya bahasa dan detailnya cocok dengan sentimen yang diminta.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays product reviews in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Fictitious Product Name:" column with:**
`Soundproof Headphones "AuraSound Pro"`
*   **Set the "Select Review Sentiment:" option to:**
`Positive (5 Stars)`
---
