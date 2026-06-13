## Application Name
AI Congratulations Writer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users write sincere and personal congratulations. Users select the type of event, their relationship with the recipient, and the desired style, then the AI ​​will create several greeting drafts that can be used or modified immediately.

## User Interface Components (UI Components)

1.  **Header:** The large headline says "AI Congratulations Writer".
2.  **User Input Form:**
    *   **Event Selection:** A dropdown (select) menu labeled "For What Event?" and options: "Birthday", "Wedding", "Graduation", "Birth of a Child".
    *   **Relationship Input:** A text input field with the label "Your Relationship with the Recipient? (example: best friend, coworker, younger sibling)".
    *   **Style Selection:** A dropdown (select) menu with the label "Speech Style:" and options: "Sincere & Touching", "Funny & Casual", "Formal & Respectful".
3.  **Action Button:** A main button with the text "Create Congratulations". While the process is running, the button should be disabled and display the "Word Stringing..." status.
4.  **Output Area:**
    *   Title (H3): "3 Draft Greetings For You:"
    *   A single content area to display 3 speech drafts. Each draft should be clearly separated.
    *   **Copy Button:** Each draft should have an individual "Copy" button next to it.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `---` or `**`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the event details and clicks the “Create Congratulations” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis kartu ucapan yang sangat empatik dan pandai merangkai kata-kata yang tulus.

    Berdasarkan kriteria berikut:
    - Acara: [Acara dari pilihan pengguna]
    - Hubungan dengan Penerima: [Hubungan dari input pengguna]
    - Gaya Ucapan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah menulis **3 draf ucapan selamat yang berbeda**. Setiap draf harus:
    - Sesuai dengan acara, hubungan, dan gaya yang dipilih.
    - Terasa personal dan tidak generik.
    - Menyertakan tempat kosong seperti `[Nama Penerima]` agar mudah disesuaikan oleh pengguna.

    Gunakan format Markdown untuk memisahkan setiap draf dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 3 formatted speech drafts in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "For What Occasion?" to:**
`Wedding`
*   **Fill in the "Your Relationship with the Recipient?..." column with:**
`Friends since childhood`
*   **Set the "Speech Style:" option to:**
`Sincere & Touching`
---
