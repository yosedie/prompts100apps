## Application Name
SMART AI Resolution: Personal Goal Setter

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a goal-setting coach. Users enter a general goal or resolution, and AI will help reformulate it into a **SMART** (Specific, Measurable, Achievable, Relevant, Time-bound) goal.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "SMART AI Resolution".
2.  **User Input Form:**
    *   A text area labeled "What are your still general goals or resolutions?".
3.  **Action Button:** A main button with the text "Make it SMART!". While the process is running, the button should be activated and display the status "Making a Plan...".
4.  **Output Area:**
    *   Title (H3): "Your Resolution in SMART Format:"
    *   A single content area to display SMART goal details.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a general goal and clicks the "Make It SMART!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pelatih pengembangan diri (life coach) dan ahli produktivitas yang berspesialisasi dalam metode penetapan tujuan SMART.

    Berikut adalah tujuan umum dari seorang pengguna:
    """
    [Tujuan dari input pengguna]
    """

    Tugas Anda adalah mengubah tujuan umum ini menjadi sebuah tujuan yang terstruktur menggunakan kerangka SMART. Rincikan setiap komponen dengan jelas:

    - **Specific (Spesifik):** Apa yang sebenarnya ingin dicapai? Siapa yang terlibat? Di mana?
    - **Measurable (Terukur):** Bagaimana cara mengukur kemajuannya? Angka apa yang bisa dilacak?
    - **Achievable (Dapat Dicapai):** Apakah tujuan ini realistis? Langkah pertama apa yang bisa diambil?
    - **Relevant (Relevan):** Mengapa tujuan ini penting bagi Anda saat ini?
    - **Time-bound (Berbatas Waktu):** Kapan target ini harus tercapai? Apa tenggat waktunya?

    Setelah merinci kelima komponen tersebut, tulis satu **Pernyataan Tujuan Akhir** yang menggabungkan semua elemen SMART menjadi satu kalimat yang kuat. Gunakan format Markdown untuk menyusun jawaban dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays SMART goal details in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the column "What are your still general goals or resolutions?" with:**
`I want to be healthier this year.`
---
