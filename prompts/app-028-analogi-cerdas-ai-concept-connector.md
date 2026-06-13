## Application Name
AI Smart Analogy: Concept Connector

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a creative web application that helps users understand the relationship between two different concepts by creating clever analogies. Users enter two concepts, and the AI ​​will create an easy-to-understand analogy to explain how they are connected.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Smart Analogy".
2.  **User Input Form:**
    *   **Input Concept 1:** A text input field labeled "Concept 1:".
    *   **Input Concept 2:** A text input field labeled "Concept Two:".
3.  **Action Button:** A main button with the text "Create an Analogy". While the process is running, the button should be activated and display the status "Connecting Ideas...".
4.  **Output Area:**
    *   Title (H3): "Resulting Analogy:"
    *   A single content area to display analogies.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters two concepts and clicks the "Create Analogy" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang guru dan pemikir kreatif yang sangat ahli dalam membuat analogi untuk menjelaskan konsep-konsep yang sulit.

    Berdasarkan dua konsep berikut:
    - Konsep 1: [Teks dari input pengguna 1]
    - Konsep 2: [Teks dari input pengguna 2]

    Tugas Anda adalah menciptakan sebuah analogi yang cerdas dan mudah dipahami untuk menjelaskan hubungan atau kesamaan fungsional antara kedua konsep tersebut.

    Struktur jawaban Anda harus:
    1.  Sajikan analoginya dalam satu kalimat pembuka yang jelas (Contoh: "[Konsep 1] itu seperti [Konsep 2]").
    2.  Jelaskan MENGAPA analogi itu cocok dalam beberapa kalimat berikutnya, dengan menyoroti kesamaan peran atau prosesnya.

    Gunakan format Markdown untuk penekanan jika diperlukan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted analogy in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "First Draft:" column with:**
`API (Application Programming Interface)`
*   **Fill in the "Second Concept:" column with:**
`Waiter in restaurant`
---
