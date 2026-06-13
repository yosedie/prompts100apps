## Application Name
AI Surprise Party Planner

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a confidential event planner. Users enter details about the person to be surprised, budget, and date, then AI will put together a complete surprise party plan from A to Z, including theme ideas, event rundown, and a countdown preparation timeline.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Surprise Party Planner".
2.  **User Input Form:**
    *   **Input Name:** A text input field labeled "Who will be surprised?".
    *   **Input Interests:** A text area with the label "What are his hobbies & interests? (example: games, movies, music, sports)".
    *   **Party Date Input:** A date input field (type="date") labeled "Surprise Party Date:".
    *   **Budget Options:** A dropdown (select) menu with the label "Estimated Budget:" and options: "Frugal (under 500k)", "Medium (500k - 1.5m)", "Large (above 1.5m)".
3.  **Action Buttons:** A main button with the text "Plan a Party!". While the process is running, the button should be activated and display the status "Drawing Up a Secret Plan...".
4.  **Output Area:**
    *   Title (H3): "The Complete Plan for the Surprise Party:"
    *   A single content area to display the entire plan.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the party details and clicks the “Plan a Party!” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang perencana acara (event planner) profesional yang ahli dalam merancang pesta kejutan yang detail dan tak terlupakan.

    Berdasarkan informasi berikut:
    - Untuk Siapa: [Nama dari input pengguna]
    - Hobi & Minat: [Minat dari input pengguna]
    - Tanggal Pesta: [Tanggal dari input pengguna]
    - Budget: [Budget dari pilihan pengguna]

    Tugas Anda adalah membuat rencana pesta kejutan yang lengkap dan dapat ditindaklanjuti. Rencana harus mencakup:

    1.  **Ide Tema Pesta:** Berikan 2-3 ide tema kreatif yang sesuai dengan hobi dan minat orang tersebut.
    2.  **Timeline Persiapan:** Buat timeline persiapan MUNDUR dari tanggal pesta (misal: 2 Minggu Sebelumnya, 1 Minggu Sebelumnya, 1 Hari Sebelumnya, Hari-H). Rincikan tugas-tugas penting di setiap tahap.
    3.  **Rundown Acara (Hari-H):** Buat jadwal acara yang detail untuk hari pesta, dari persiapan akhir hingga momen kejutan.
    4.  **Tips Menjaga Kerahasiaan:** Berikan beberapa tips kunci agar kejutan tidak bocor.

    Gunakan format Markdown untuk menyusun seluruh rencana dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted party plan in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow for live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "Who will be surprised?" with:**
`Andi`
*   **Fill in the "What are his hobbies & interests?..." column with:**
`Likes watching science fiction (sci-fi) films, playing board games, and listening to classic rock music.`
*   **Set "Surprise Party Date:" to:**
`(Choose any date, about 3 weeks from now)`
*   **Set the "Estimated Budget:" option to:**
`Medium (500 thousand - 1.5 million)`
---
