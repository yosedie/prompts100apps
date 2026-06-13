## Application Name
AI Perfect Date Planner

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a personal date planner. Users enter their partner's interests, budget, and desired atmosphere, then AI will design a date itinerary that is unique, personal, and complete from start to finish.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI's Perfect Dating Planner".
2.  **User Input Form:**
    *   **Input Interests:** A text area with the label "What are your partner's interests? (example: art, nature, culinary, film, music)".
    *   **Budget Selection:** A dropdown (select) menu with the label "Dating Budget:" and options: "Frugal (under 200k)", "Medium (200k - 500k)", "Special (above 500k)".
    *   **Atmosphere Options:** A dropdown (select) menu with the label "Desired Atmosphere:" and options: "Romantic & Calm", "Fun & Active", "Relaxed & Casual", "Unique & Anti-Mainstream".
3.  **Action Button:** A home button with the text "Plan the Perfect Date!". While the process is running, the button should be disabled and display the status "Designing Moments...".
4.  **Output Area:**
    *   Title (H3): "Special Dating Plans For You:"
    *   A single content area to display the entire plan.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the date details and clicks the "Plan the Perfect Date!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang perencana kencan (date planner) yang kreatif, romantis, dan sangat detail.

    Berdasarkan kriteria berikut:
    - Minat Pasangan: [Minat dari input pengguna]
    - Budget: [Budget dari pilihan pengguna]
    - Suasana Kencan: [Suasana dari pilihan pengguna]

    Tugas Anda adalah merancang SATU ide kencan yang lengkap dan personal. Rencana tersebut harus mencakup:
    1.  **Nama Kencan:** Berikan judul yang kreatif untuk ide kencan ini.
    2.  **Ringkasan Singkat:** Jelaskan secara singkat mengapa kencan ini cocok.
    3.  **Itinerary Lengkap:** Buat jadwal langkah-demi-langkah (misal: Aktivitas Sore, Makan Malam, Aktivitas Malam). Untuk setiap langkah, jelaskan aktivitasnya dan berikan estimasi biaya agar sesuai dengan budget.

    Pastikan seluruh rencana sesuai dengan minat, budget, dan suasana yang dipilih. Gunakan format Markdown untuk menyusun rencana dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted date plan in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "What is your partner's interest?..." column with:**
`Likes art, visiting galleries, drinking coffee and listening to jazz.`
*   **Set the "Dating Budget:" option to:**
`Medium (200k - 500k)`
*   **Set the "Desired Scene:" option to:**
`Romantic & Calm`
---
