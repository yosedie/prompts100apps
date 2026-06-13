## Application Name
AI Personal Stylist: Personal Outfit Stylist

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a virtual personal stylist. Users enter the type of event, clothing style and desired style, then AI will provide a complete and coherent outfit recommendation, from tops to shoes and accessories.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Personal Stylist".
2.  **User Input Form:**
    *   **Event Input:** A text input field labeled "For What Event?".
    *   **Fashion Style Selection:** A dropdown (select) menu with the label "Fashion Style For:" and options: "Men", "Women".
    *   **Style Selection:** A dropdown (select) menu with the label "Desired Style:" and options: "Formal & Professional", "Casual & Casual", "Elegant & Chic", "Creative & Unique".
3.  **Action Buttons:** A main button with the text "Recommend Outfit!". While the process is running, the button should be activated and display the status "Seeking Inspiration...".
4.  **Output Area:**
    *   Title (H3): "Outfit Recommendations for You:"
    *   A single content area to display all recommendations.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in event and style details, then click the "Recommend Outfit!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penata gaya pribadi (personal stylist) dan fashion consultant yang berpengalaman dengan selera mode yang tinggi.

    Berdasarkan kriteria berikut:
    - Acara: [Acara dari input pengguna]
    - Gaya Busana Untuk: [Gaya busana dari pilihan pengguna]
    - Gaya yang Diinginkan: [Gaya dari pilihan pengguna]

    Tugas Anda adalah merancang SATU rekomendasi outfit yang lengkap dan koheren. Rekomendasi harus mencakup:
    - **Atasan (Top):**
    - **Bawahan (Bottom):**
    - **Lapisan Luar (Outerwear, jika perlu):**
    - **Sepatu (Footwear):**
    - **Aksesori (Accessories):**
    - **Tips Tambahan:** (Berikan satu tips singkat tentang cara memakainya).

    Pastikan semua item saling melengkapi dan sesuai dengan acara serta gaya yang diinginkan. Gunakan format Markdown untuk menyusun rekomendasi dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays outfit recommendations that have been formatted in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "For What Event?" with:**
`Job interviews at technology companies`
*   **Set the "Fashion Style For:" option to:**
`Woman`
*   **Set the "Desired Style:" option to:**
`Formal & Professional`
---
