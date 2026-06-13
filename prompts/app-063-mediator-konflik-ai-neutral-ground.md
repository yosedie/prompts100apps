## Application Name
AI Conflict Mediator: Neutral Ground

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that serves as a neutral virtual conflict mediator. Users describe an issue or dispute from two different points of view, and AI will provide objective analysis, identify the core of the problem, and suggest communication steps to reach a resolution.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Conflict Mediator".
2.  **User Input Form:**
    *   **Input Point of View A:** A text area with the label "Describe the Problem from Party A's Point of View:".
    *   **Input Point of View B:** A text area labeled "Describe the Problem from Party B's Point of View:".
3.  **Action Button:** A main button with the text "Find the Middle Ground". While the process is running, the button should be activated and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Mediation Analysis & Suggestions:"
    *   A single content area to display all analysis.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the description from both points of view and clicks the "Find Middle Ground" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang mediator konflik profesional yang netral, empatik, dan sangat objektif.

    Berikut adalah deskripsi sebuah perselisihan dari dua sudut pandang yang berbeda:
    - Sudut Pandang Pihak A: """[Teks dari input A]"""
    - Sudut Pandang Pihak B: """[Teks dari input B]"""

    Tugas Anda adalah menganalisis konflik ini dan memberikan panduan untuk resolusi. Analisis Anda harus mencakup:

    1.  **Analisis Objektif:** Rangkum situasi secara netral tanpa memihak. Identifikasi apa inti masalah sebenarnya di luar emosi yang diungkapkan.
    2.  **Validasi Kedua Pihak:** Tulis satu kalimat yang memvalidasi perasaan atau perspektif Pihak A, dan satu kalimat untuk Pihak B.
    3.  **Saran Langkah Komunikasi:** Berikan saran langkah-demi-langkah yang konkret tentang bagaimana kedua pihak bisa memulai percakapan yang produktif. Sarankan kalimat pembuka yang bisa mereka gunakan.

    Gunakan format Markdown untuk menyusun analisis dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays mediation analysis in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe the Problem from Party A's Point of View:" column with:**
`I feel like my co-worker, Budi, always hands over his work at the last minute. This makes me have to rush and often work overtime to complete my part which depends on his work. I feel unappreciated.`
*   **Fill in the "Describe the Problem from Party B's Point of View:" column with:**
`I felt Anita was too demanding and didn't understand that I was juggling several projects at once. I always finish my work before the deadline, but he keeps asking about progress and makes me feel pressured.`
---
