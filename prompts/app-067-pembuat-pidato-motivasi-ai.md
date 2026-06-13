## Application Name
AI Motivational Speech Maker

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a motivational speech writer. Users select a central theme, and AI will generate a short speech script that is powerful, inspiring, and ready to be delivered.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Motivational Speech Maker".
2.  **User Input Form:**
    *   **Theme Choice:** A dropdown (select) menu with the label "Choose Your Speech Theme:" and options: "Perseverance & Never Give Up", "Innovation & Change", "Teamwork & Collaboration", "Overcoming Failure".
3.  **Action Button:** A main button with the text "Fire the Spirit!". While the process is running, the button should be activated and display the status "Seeking Inspiration...".
4.  **Output Area:**
    *   Title (H3): "Your Motivational Speech Script:"
    *   A single content area to display the entire manuscript.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a theme and clicks the "Fire the Spirit!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang motivator dan pembicara publik kelas dunia, setara dengan Tony Robbins atau Simon Sinek. Gaya Anda penuh semangat, inspiratif, dan persuasif.

    Berdasarkan tema berikut:
    """
    [Tema dari pilihan pengguna]
    """

    Tugas Anda adalah menulis naskah pidato motivasi singkat (sekitar 2-3 menit jika dibacakan). Naskah harus memiliki struktur yang kuat:
    1.  **Pembukaan yang Menghentak:** Mulai dengan sebuah pertanyaan retoris, kutipan, atau pernyataan berani yang langsung menarik perhatian.
    2.  **Isi yang Menginspirasi:** Gunakan analogi, metafora, atau cerita pendek untuk mengilustrasikan tema utama.
    3.  **Penutup yang Menggugah:** Akhiri dengan panggilan untuk bertindak (call to action) yang kuat dan kalimat yang membangkitkan semangat.

    Gunakan format Markdown untuk penekanan pada kata-kata atau kalimat kunci.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the speech script in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Choose Your Speech Theme:" option to:**
`Perseverance & Never Give Up`
---
