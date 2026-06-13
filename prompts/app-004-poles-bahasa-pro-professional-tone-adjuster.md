## Application Name
Pro Language Polish: Professional Tone Adjuster

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a communications assistant. The user enters a draft of text (email, chat message, etc.) that is awkward or too blunt, then selects the desired context and language style. The app will rewrite the text into a more professional, persuasive, or diplomatic version.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Pro Language Polish".
2.  **User Input Form:**
    *   **Input Original Text:** A large text area labeled "Your Original Text:".
    *   **Input Context:** A text input field labeled "What is the Main Purpose of This Message?".
    *   **Language Style Selection:** A dropdown (select) menu with the label "Select the Desired Language Style:" and the following options:
        *   Professional & Formal
        *   Persuasive & Friendly
        *   Diplomatic & Firm
3.  **Action Button:** A home button with the text "Polish Text Now!". While the process is running, the button should be disabled and display the status "Polishing Language...".
4.  **Output Area:**
    *   Title (H3): "Enhanced Version:"
    *   A content area (read-only) to display polished text.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area for user convenience.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert the Markdown syntax (if any) into formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the original text, purpose, and selects a language style, then clicks the "Polish Text Now!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli komunikasi profesional dan editor ahli.

    Berdasarkan informasi berikut:
    - Teks Asli: """[Teks dari input pengguna]"""
    - Konteks/Tujuan: [Tujuan dari input pengguna]
    - Gaya Bahasa yang Diinginkan: [Gaya bahasa dari pilihan pengguna]

    Tugas Anda adalah menulis ulang "Teks Asli" menjadi versi yang jauh lebih baik sesuai dengan konteks dan gaya bahasa yang diinginkan. Perbaiki tata bahasa, hilangkan kalimat yang canggung, dan gunakan kosa kata yang lebih profesional. Pastikan pesan utama tersampaikan dengan jelas dan efektif.

    PENTING: Hanya berikan hasil akhir teks yang sudah dipoles, tanpa tambahan komentar atau penjelasan dari Anda.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content (if any) of the response into HTML.
5.  The application displays the refined text in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Your Original Text:" field with:**
`This is your work wrong, revise it again. Don't be late tomorrow's deadline.`
*   **Fill in the column "What is the Main Purpose of This Message?" with:**
`Provide revision feedback to colleagues in a constructive manner.`
*   **Set the "Select the Desired Language Style:" option to:**
`Professional & Formal`
---
