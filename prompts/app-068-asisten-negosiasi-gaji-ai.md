## Application Name
AI Salary Negotiation Assistant

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a salary negotiation coach. Users input data about their position, industry, and accomplishments, and AI generates strong argument points and key phrases that can be immediately used in negotiation conversations.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Salary Negotiation Assistant".
2.  **User Input Form:**
    *   **Position Input:** A text input field with the label "Your Position/Title:".
    *   **Industry Input:** A text input field labeled "Company Industry:".
    *   **Input Achievements:** A text area labeled "Name your 2-3 Best Quantitative Achievements:". Provide a placeholder such as "Example: Increase sales by 20%, Reduce operational costs by 15%".
3.  **Action Button:** A main button with the text "Set Up My Arguments". While the process is running, the button should be activated and display the status "Preparing...".
4.  **Output Area:**
    *   Title (H3): "Key Points & Phrases for Negotiation:"
    *   A single content area to display the entire guide.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in position and accomplishment details, then click the "Prepare My Arguments" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang negosiator ulung dan konsultan karir yang ahli dalam strategi negosiasi gaji.

    Berdasarkan profil pengguna berikut:
    - Posisi: [Posisi dari input pengguna]
    - Industri: [Industri dari input pengguna]
    - Pencapaian: """[Pencapaian dari input pengguna]"""

    Tugas Anda adalah membuat panduan negosiasi yang ringkas dan kuat. Panduan harus mencakup:

    1.  **Riset Pasar (Pembuka):** Sebuah kalimat pembuka yang menunjukkan bahwa pengguna telah melakukan riset, berdasarkan posisi dan industrinya.
    2.  **Poin Argumen Berbasis Nilai:** Ubah setiap pencapaian yang diberikan menjadi poin argumen yang kuat, menghubungkan kontribusi masa lalu dengan nilai masa depan bagi perusahaan.
    3.  **Frasa Kunci yang Bisa Digunakan:** Berikan beberapa contoh frasa diplomatis untuk digunakan saat mengajukan permintaan, menanggapi tawaran, atau saat hening.

    Gunakan format Markdown untuk menyusun panduan dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a negotiation guide in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Your Position/Title:" column with:**
`Senior Software Engineer`
*   **Fill in the "Company Industry:" column with:**
`Financial Technology (Fintech)`
*   **Fill in the column "Name your 2-3 Best Quantitative Achievements:" with:**
`- Led a project that increased application loading speed by 30%.
    - Reduced critical bugs in production by 50% through better implementation of unit testing.`
---
