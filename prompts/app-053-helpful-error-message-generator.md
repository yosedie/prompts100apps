## Application Name
Helpful Error Message Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for developers that functions as an error message writer. Users describe a technical error situation, and AI will write clear, informative, and user-friendly error messages, complete with explanations and suggested fixes for developers.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large header says "Helpful Error Message Generator".
2.  **User Input Form:**
    *   **Input Error Situation:** A text area labeled "Describe the Error Situation Technically:".
    *   **Message Style Options:** A dropdown (select) menu with the label "Select Message Style:" and options: "Helpful & Professional", "Helpful & Humorous".
3.  **Action Button:** A main button with the text "Generate Error Message". While the process is running, the button should be activated and display the status "Searching for Reason...".
4.  **Output Area:**
    *   Title (H3): "Error Message Generated:"
    *   A single content area to display the entire message.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and code blocks) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the error situation, selects a style, and clicks the "Generate Error Message" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang developer senior sekaligus UX writer yang ahli dalam membuat pesan error yang tidak membuat frustrasi.

    Berdasarkan informasi berikut:
    - Situasi Error: [Deskripsi dari input pengguna]
    - Gaya Pesan yang Diinginkan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah menulis pesan error yang lengkap. Pesan harus mencakup:

    1.  **Pesan Error:** Teks yang akan ditampilkan kepada pengguna akhir. Harus jelas, ringkas, dan sesuai dengan gaya yang diminta.
    2.  **Penjelasan untuk Developer:** Penjelasan singkat tentang kemungkinan penyebab error ini.
    3.  **Saran Perbaikan:** Langkah-langkah konkret yang bisa dicoba oleh developer untuk mengatasi masalah ini.

    Gunakan format Markdown untuk menyusun jawaban dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted error message in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe the Error Situation Technically:" column with:**
`The API call failed because the provided API key was invalid or expired.`
*   **Set the "Choose Message Style:" option to:**
`Helpful & Humorous`
---
