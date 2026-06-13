## Application Name
Trivia Forge AI: Custom Trivia Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a custom trivia quiz maker. Users enter a very specific topic, choose the number of questions and difficulty level, and then the AI ​​will generate a set of challenging trivia questions, complete with answers.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Trivia Forge AI".
2.  **User Input Form:**
    *   **Topic Input:** A text input field labeled "Enter Your Specific Trivia Topic:".
    *   **Input Number of Questions:** A number input field (type="number") with the label "Number of Questions:" and a default value of 10.
    *   **Difficulty Level Selection:** A dropdown (select) menu with the label "Difficulty Level:" and options: "Easy", "Medium", "Hard".
3.  **Action Button:** A main button with the text "Create a Trivia Question!". While the process is running, the button should be activated and display the status "Finding Facts...".
4.  **Output Area:**
    *   Title (H3): "Your Custom Trivia Set:"
    *   A single content area to display a list of questions and answers.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the trivia details and clicks the "Create Trivia Question!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang 'Quizmaster' dan peneliti yang ahli dalam menemukan fakta-fakta menarik dan obskur tentang berbagai topik.

    Berdasarkan kriteria berikut:
    - Topik: [Topik dari input pengguna]
    - Jumlah Pertanyaan: [Jumlah dari input pengguna]
    - Tingkat Kesulitan: [Tingkat kesulitan dari pilihan pengguna]

    Tugas Anda adalah membuat satu set pertanyaan trivia.
    - Pertanyaan harus sesuai dengan tingkat kesulitan yang diminta.
    - Untuk setiap pertanyaan, berikan jawabannya.

    Gunakan format Markdown yang ketat sebagai berikut:
    1.  **Pertanyaan:** [Teks pertanyaan Anda]?
        **Jawaban:** [Teks jawaban Anda].
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays preformatted sets of trivia in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Your Specific Trivia Topic:" field with:**
`History and characters in the film The Lord of the Rings`
*   **Set "Number of Questions:" to:**
`10`
*   **Set the "Difficulty Level:" option to:**
`Medium`
---
