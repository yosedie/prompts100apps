## Application Name
AI Points to Paragraph Converter: Paragraph Weaver

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that turns a list of raw bullet points into a cohesive, smooth-flowing narrative paragraph. Users simply paste in a list of points, and AI will organize them into readable text.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Points to Paragraph Converter".
2.  **User Input Form:**
    *   A large text area labeled "Paste Your Bullet Points Here:".
3.  **Action Button:** A main button with the text "Convert to Paragraph". While the process is running, the button should be activated and display the status "Compiling...".
4.  **Output Area:**
    *   Title (H3): "Resulting Paragraph:"
    *   A single content area to display entire paragraphs.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a bulleted list and clicks the "Convert to Paragraph" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang editor dan penulis yang ahli dalam menciptakan teks yang mengalir lancar dan kohesif.

    Berdasarkan daftar poin-poin berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah mengubah daftar poin ini menjadi SATU paragraf naratif yang terstruktur dengan baik.
    - Gunakan kalimat transisi untuk menghubungkan setiap poin secara logis.
    - Jangan hanya mengubah setiap poin menjadi kalimat, tetapi rangkailah menjadi sebuah cerita atau penjelasan yang utuh.
    - Pastikan hasilnya adalah paragraf yang enak dibaca.

    PENTING: Hanya berikan hasil paragrafnya saja, tanpa tambahan komentar.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted paragraph in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste Your Bullet Points List Here:" column with:**
`- This project aims to increase efficiency.
    - The main feature is monthly report automation.
    - The target user is department managers.
    - It is hoped that it can reduce manual work time by up to 40%.`
---
