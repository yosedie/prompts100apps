## Application Name
Author Acknowledgments AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users write sincere and specific thank you notes. Users enter the gift or favor they received and from whom, and the AI ​​will draft a greeting that is personal and doesn't sound generic.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Author AI Acknowledgments".
2.  **User Input Form:**
    *   **Gift/Aid Input:** A text area labeled "What did you receive (gift/aid)?".
    *   **Giver Input:** A text input field labeled "From whom?".
    *   **Style Selection:** A dropdown (select) menu with the label "Speech Style:" and options: "Casual & Warm", "Formal & Professional".
3.  **Action Button:** A main button with the text "Write a Thank You Note". While the process is running, the button should be activated and display the status "Stringing Words...".
4.  **Output Area:**
    *   Title (H3): "Draft Your Acknowledgment:"
    *   A single content area to display the entire speech.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the details, chooses a style, and clicks the “Write a Thank You” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis yang ahli dalam mengekspresikan rasa terima kasih dengan tulus dan spesifik.

    Berdasarkan informasi berikut:
    - Hadiah/Bantuan yang Diterima: """[Teks dari input hadiah/bantuan]"""
    - Pemberi: [Nama dari input pemberi]
    - Gaya yang Diinginkan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah menulis sebuah draf ucapan terima kasih yang singkat. Ucapan harus:
    - Menyebutkan secara spesifik hadiah atau bantuan yang diterima.
    - Menjelaskan secara singkat mengapa hadiah/bantuan tersebut dihargai atau apa dampaknya.
    - Menggunakan nada yang sesuai dengan gaya yang dipilih.

    Gunakan placeholder `[Nama Pemberi]` dan `[Nama Anda]` agar mudah disesuaikan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a draft thank you note in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What did you receive (gift/aid)?" with:**
`A book about astronomy for my birthday. I've wanted it for a long time!`
*   **Fill in the "From whom?" with:**
`Aunt Rina`
*   **Set the "Speech Style:" option to:**
`Relaxing & Warm`
---
