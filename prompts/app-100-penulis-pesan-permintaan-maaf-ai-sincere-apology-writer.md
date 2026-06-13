## Application Name
AI Apology Message Writer: Sincere Apology Writer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users formulate a sincere and responsible apology message. The user explains the situation and the mistake they made, and the AI ​​will draft an apology that shows regret, admits the mistake, and expresses an intention to make amends.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Apology Message Author AI".
2.  **User Input Form:**
    *   **Situation Input:** A text area labeled "Describe Your Situation & Mistake:".
    *   **Recipient Input:** A text input field with the label "To Whom is this Apology Addressed?".
3.  **Action Button:** A main button with the text "Compose an Apology". While the process is running, the button should be activated and display the status "Stringing Words...".
4.  **Output Area:**
    *   Headline (H3): "Draft Your Apology Message:"
    *   A single content area to display the entire message.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the details of the situation and clicks the “Compose Apology” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli komunikasi interpersonal dan mediator yang sangat empatik. Anda memahami cara merumuskan permintaan maaf yang tulus dan efektif.

    Berdasarkan situasi berikut:
    - Situasi & Kesalahan: """[Teks dari input situasi]"""
    - Ditujukan Kepada: [Teks dari input penerima]

    Tugas Anda adalah menulis sebuah draf pesan permintaan maaf yang bertanggung jawab. Pesan harus mengikuti struktur:
    1.  **Akui Kesalahan:** Mulai dengan mengakui kesalahan secara spesifik tanpa membuat alasan.
    2.  **Tunjukkan Penyesalan & Empati:** Jelaskan bahwa Anda memahami dampak negatif dari tindakan Anda terhadap perasaan mereka.
    3.  **Ambil Tanggung Jawab:** Nyatakan bahwa itu adalah kesalahan Anda.
    4.  **Tawarkan Perbaikan (jika memungkinkan):** Sebutkan niat Anda untuk memperbaiki situasi atau untuk tidak mengulanginya lagi.

    Gunakan placeholder `[Nama Penerima]` dan `[Nama Anda]` agar mudah disesuaikan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the draft apology in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe Your Situation & Mistake:" column with:**
`I forgot my best friend's birthday yesterday. I was really busy with work and just remembered today. He must feel sad and ignored.`
*   **Fill in the column "To Whom is this Apology Addressed?" with:**
`My friend, Rina`
---
