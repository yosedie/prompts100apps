## Application Name
SEO Blog Framework: SEO Outline Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as an SEO content planner. Users enter one main keyword, and the AI ​​will generate a blog article template that is structured (H1, H2, H3) and optimized for search engines, complete with relevant sub-topic suggestions.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "SEO Blog Framework".
2.  **User Input Form:**
    *   A text input field labeled "Enter Your Primary Keyword:".
3.  **Action Button:** A main button with the text "Create Blog Framework". While the process is running, the button should be activated and display the status "Analyzing SEO...".
4.  **Output Area:**
    *   Title (H3): "SEO-Friendly Article Framework:"
    *   A single content area to display the entire framework.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (especially `H1`, `H2`, `H3`, and lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters keywords and clicks the “Create Blog Template” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang Spesialis SEO Konten (Content SEO Specialist) dan ahli strategi digital yang sangat berpengalaman.

    Berdasarkan kata kunci utama berikut:
    """
    [Kata kunci dari input pengguna]
    """

    Tugas Anda adalah membuat kerangka artikel blog yang komprehensif dan SEO-friendly. Kerangka ini harus membantu penulis untuk membuat konten yang mendalam dan berperingkat tinggi di mesin pencari.

    Struktur kerangka harus menggunakan format Markdown hierarkis yang jelas:

    - **H1 (Judul Utama):** Buat satu judul yang menarik, mengandung kata kunci, dan memancing klik.
    - **H2 (Sub-Judul Utama):** Buat beberapa H2 yang mencakup aspek-aspek utama dari topik, menjawab pertanyaan umum (apa, mengapa, bagaimana).
    - **H3 (Poin-Poin Detail):** Di bawah setiap H2, berikan beberapa H3 yang lebih spesifik sebagai poin-poin pembahasan.
    - **Saran Sub-Topik Tambahan:** Di akhir, berikan daftar poin berisi saran kata kunci turunan atau pertanyaan terkait (LSI keywords, People Also Ask) yang bisa dimasukkan ke dalam artikel.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted outline in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Your Main Keyword:" column with:**
`The health benefits of coffee`
---
