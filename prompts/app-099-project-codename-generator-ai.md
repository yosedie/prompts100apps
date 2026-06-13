## Application Name
Project Codename Generator AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for developers and project managers that provides creative codename ideas. Users enter a brief description of the project's goals, and AI will generate 10 unique and thematic codename ideas.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Project Codename Generator AI".
2.  **User Input Form:**
    *   A text area labeled "Describe the Main Goal of Your Project:".
3.  **Action Buttons:** A main button with the text "Generate Codenames!". While the process is running, the button should be activated and display the status "Brainstorming...".
4.  **Output Area:**
    *   Title (H3): "10 Project Code Name Ideas:"
    *   A single content area to display 10 names in a numbered list.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a project description and clicks the "Generate Codenames!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang manajer produk di sebuah laboratorium inovasi rahasia (skunkworks). Anda ahli dalam memberikan nama kode yang keren, misterius, dan tematik untuk proyek-proyek baru.

    Berdasarkan deskripsi tujuan proyek berikut:
    """
    [Deskripsi dari input pengguna]
    """

    Tugas Anda adalah membuat **10 ide nama kode (codename)** yang unik. Nama-nama ini harus:
    - Terdiri dari satu atau dua kata.
    - Terdengar keren dan profesional.
    - Secara tematis berhubungan dengan tujuan proyek (misalnya, proyek tentang kecepatan bisa dinamai 'Project Velocity' atau 'Project Cheetah').

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 10 code name ideas in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe the Main Goal of Your Project:" column with:**
`A classified project to rebuild a company website from scratch with the latest technology, with a focus on speed and a modern user experience.`
---
