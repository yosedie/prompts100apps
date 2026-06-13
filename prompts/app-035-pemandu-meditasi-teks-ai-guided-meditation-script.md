## Application Name
Guided Meditation Text AI: Guided Meditation Script

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a guided meditation script generator. Users select a theme and duration, and AI will generate a calming, ready-to-read script, complete with directions for pausing and breathing.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Text Meditation Guide".
2.  **User Input Form:**
    *   **Theme Input:** A text input field labeled "Choose Your Meditation Theme:".
    *   **Duration Selection:** A dropdown (select) menu with the label "Select Session Duration:" and options: "Short (3 Minutes)", "Medium (5 Minutes)", "Long (10 Minutes)".
3.  **Action Button:** A main button with the text "Create Meditation Script". While the process is running, the button should be activated and display the status "Relaxing Mind...".
4.  **Output Area:**
    *   Title (H3): "Guided Meditation Script:"
    *   A single content area to display the entire manuscript.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*` for directives) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a theme, duration, and clicks the “Create Meditation Script” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pemandu meditasi dan instruktur mindfulness yang berpengalaman. Suara tulisan Anda tenang, lembut, dan menenangkan.

    Berdasarkan kriteria berikut:
    - Tema Meditasi: [Tema dari input pengguna]
    - Durasi Sesi: [Durasi dari pilihan pengguna]

    Tugas Anda adalah menulis naskah meditasi terpandu yang lengkap. Naskah harus memiliki struktur yang jelas:
    1.  **Pembukaan:** Ajak pendengar untuk menemukan posisi yang nyaman dan fokus pada napas.
    2.  **Isi Utama:** Pandu pendengar melalui visualisasi atau latihan kesadaran yang sesuai dengan tema yang diberikan.
    3.  **Penutup:** Bawa kembali kesadaran pendengar secara perlahan ke ruangan dan berikan afirmasi positif.

    PENTING: Gunakan arahan dalam tanda kurung dan teks miring untuk menandakan jeda atau instruksi non-verbal. Contoh: *(jeda sejenak)* atau *(tarik napas dalam-dalam)*. Pastikan panjang naskah sesuai dengan durasi yang diminta.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted meditation script in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Choose Your Meditation Theme:" column with:**
`Reducing stress before bed`
*   **Set the "Select Session Duration:" option to:**
`Medium (5 Minutes)`
---
