## Application Name
Quick Agenda: Meeting Agenda Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a highly efficient web application for creating structured meeting agendas. Users only need to enter one sentence of the meeting objective, start time, and duration, then the application will automatically generate a complete agenda with time allocation, discussion topics, and objectives for each session.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Quick Agenda".
2.  **User Input Form:** Created in one row or neat grid.
    *   **Input Meeting Objective:** A text input field with the label "Main Objective of Meeting (1 Sentence):".
    *   **Start Time Input:** A time input field (type="time") labeled "Start Time:".
    *   **Duration Input:** A number input field (type="number") with the label "Total Duration (minutes):".
3.  **Action Button:** A main button with the text "Create Agenda". While the process is running, the button should be disabled and display the status "Creating Agenda...".
4.  **Output Area:**
    *   A single content area to display all generated agendas.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `#Title`, `**bold**`, `*list item`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in the goal, start time, and duration of the meeting, then click the "Create Agenda" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang fasilitator rapat profesional dan asisten eksekutif yang sangat terorganisir.

    Berdasarkan informasi berikut:
    - Tujuan Utama Rapat: [Tujuan dari input pengguna]
    - Waktu Mulai: [Waktu dari input pengguna]
    - Total Durasi: [Durasi dari input pengguna] menit

    Tugas Anda adalah membuat agenda rapat yang detail, logis, dan efisien. Agenda harus mencakup:
    1.  Alokasi waktu yang tepat untuk setiap sesi (contoh: 09:00 - 09:10).
    2.  Topik bahasan yang jelas.
    3.  Tujuan atau hasil yang diharapkan dari setiap sesi.

    Strukturkan agenda secara logis, dimulai dengan perkenalan, diikuti oleh pembahasan inti, dan diakhiri dengan rangkuman serta langkah selanjutnya (action items). Gunakan format Markdown untuk kejelasan (judul, sub-judul, daftar, dan teks tebal).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted agenda in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Main Objective of the Meeting (1 Sentence):" column with:**
`Discuss and decide on a new product launch strategy for the next quarter.`
*   **Fill in the "Start Time:" column with:**
`09:00`
*   **Fill in the "Total Duration (minutes):" column with:**
`60`
---
