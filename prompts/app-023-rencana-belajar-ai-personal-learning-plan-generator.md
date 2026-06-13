## Application Name
AI Learning Plan: Personal Learning Plan Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a personal curriculum designer. Users enter a topic or major skill they want to learn, and the AI ​​will create a structured, logical, and gradual weekly study plan from basic to advanced.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Learning Plan".
2.  **User Input Form:**
    *   A text input field labeled "What Topic Do You Want to Learn?".
3.  **Action Buttons:** A main button with the text "Create a Study Plan". While the process is running, the button should be disabled and display the status "Designing Curriculum...".
4.  **Output Area:**
    *   Title (H3): "Your Study Plan:"
    *   A single content area to display the entire plan.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a topic and clicks the "Create Study Plan" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli perancang kurikulum dan tutor berpengalaman yang mampu memecah topik kompleks menjadi langkah-langkah yang mudah dipelajari.

    Berdasarkan topik besar berikut:
    """
    [Topik dari input pengguna]
    """

    Tugas Anda adalah membuat rencana belajar mingguan yang terstruktur dan realistis. Rencana ini harus membawa seseorang dari tingkat pemula absolut hingga memiliki pemahaman yang kuat.

    Strukturkan rencana per minggu (misalnya, Minggu 1, Minggu 2, dst.). Untuk setiap minggu, sertakan:
    - **Fokus Utama:** Tema atau tujuan utama untuk minggu tersebut.
    - **Topik yang Dipelajari:** Daftar poin-poin konsep atau keterampilan spesifik yang harus dipelajari.
    - **Proyek/Latihan Praktis:** Saran tugas kecil atau proyek untuk menerapkan pengetahuan yang baru dipelajari.

    Pastikan urutan topiknya logis, dimulai dari dasar-dasar fundamental sebelum beralih ke konsep yang lebih mahir. Gunakan format Markdown untuk kejelasan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted study plan in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "What Topic Do You Want to Learn?" with:**
`Learn Python from Zero`
---
