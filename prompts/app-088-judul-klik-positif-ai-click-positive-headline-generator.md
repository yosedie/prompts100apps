## Application Name
AI Click-Positive Headlines: Click-Positive Headline Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps writers and content creators create attention-grabbing titles without being deceptive clickbait. Users enter an original topic or title, and the AI ​​will generate 5 alternative “click-positive” titles that are intriguing yet accurate.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Positive-Click Headline".
2.  **User Input Form:**
    *   A text input field labeled "Enter the Original Topic or Title of Your Article/Video:".
3.  **Action Button:** A main button with the text "Create a Catchy Title!". While the process is running, the button should be activated and display the status "Brainstorming...".
4.  **Output Area:**
    *   Headline (H3): "5 Click-Positive Headline Alternatives:"
    *   A single content area to display 5 titles in a numbered list.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a topic/title and clicks the "Create a Catchy Title!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli strategi konten digital dan copywriter viral. Anda memahami psikologi di balik judul yang membuat orang mengklik, tetapi Anda juga menjunjung tinggi etika dan akurasi.

    Berdasarkan topik atau judul asli berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah membuat **5 alternatif judul "klik-positif"**. Judul-judul ini harus:
    - Menarik perhatian dan memancing rasa penasaran.
    - Menggunakan angka, pertanyaan, atau kata-kata pemicu emosi positif.
    - Tetap akurat dan tidak menjanjikan sesuatu yang tidak ada di dalam konten.
    - Menghindari gaya clickbait yang menipu (contoh: "Anda tidak akan percaya apa yang terjadi selanjutnya!").

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 5 alternative titles in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter the Original Topic or Title of Your Article/Video:" column with:**
`Benefits of Drinking Water`
---
