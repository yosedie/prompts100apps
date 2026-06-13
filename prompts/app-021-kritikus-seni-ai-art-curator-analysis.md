## Application Name
AI Art Critic: Art Curator Analysis

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a virtual art critic. Users enter the title and visual description of a work of art (painting, sculpture, etc.), and AI will provide in-depth analysis and interpretation as if written by a professional art curator.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Art Critic".
2.  **User Input Form:**
    *   **Input Artwork Title:** A text input field labeled "Artwork Title (Optional):".
    *   **Input Visual Description:** A large text area labeled "Describe the Artwork Visually:".
3.  **Action Button:** A main button with the text "Artwork Interpretation". While the process is running, the button should be activated and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Curatorial Analysis & Interpretation:"
    *   A single content area to display all analysis.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the artwork description and clicks the "Artwork Interpretation" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang kurator seni dan sejarawan seni yang sangat terpelajar dan artikulatif. Gaya tulisan Anda mendalam, puitis, dan analitis.

    Berdasarkan deskripsi karya seni berikut:
    - Judul: [Judul dari input pengguna, jika ada]
    - Deskripsi Visual: [Deskripsi dari input pengguna]

    Tugas Anda adalah menulis sebuah analisis dan interpretasi kuratorial yang mendalam tentang karya ini. Analisis Anda harus mencakup:
    - **Komposisi dan Teknik:** Bagaimana elemen-elemen visual diatur? Teknik apa yang mungkin digunakan?
    - **Penggunaan Warna dan Cahaya:** Apa peran warna dan cahaya dalam menciptakan suasana?
    - **Simbolisme dan Makna:** Apa kemungkinan makna atau simbol di balik objek atau adegan yang digambarkan?
    - **Dampak Emosional:** Perasaan atau emosi apa yang coba dibangkitkan oleh karya ini?

    Sajikan analisis Anda dalam bentuk esai singkat yang mengalir dengan baik. Gunakan format Markdown untuk penekanan (teks tebal atau miring) jika diperlukan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted analysis in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Artwork Title (Optional):" column with:**
`Starry Night`
*   **Fill in the "Describe the Artwork Visually:" column with:**
`A nighttime landscape painting. The sky above was dominated by swirls of dark blue and bright yellow clouds, with a crescent moon and stars shining very brightly. Below, there is a quiet village with a gabled church. On the left side, a large dark pine tree rose like black flames towards the sky.`
---
