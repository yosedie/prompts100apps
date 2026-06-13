## Application Name
Fantasy Name Forge AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a creative web application that functions as a fantasy name generator. Users select a category (Characters, Places, Artifacts) and provide an optional theme, then the AI ​​will create a number of unique names, complete with a short fictional etymology for each name.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Fantasy Name Forge AI".
2.  **User Input Form:**
    *   **Category Selection:** A dropdown (select) menu with the label "Select Category Name:" and options: "Characters", "Places", "Artifacts".
    *   **Theme Input:** A text input field labeled "Theme or Race (Optional):".
    *   **Amount Input:** A number input field (type="number") with the label "Desired Number of Names:" and a default value of 5.
3.  **Action Button:** A main button with the text "Forge a Name!". While the process is running, the button should be disabled and display the status "Forging...".
4.  **Output Area:**
    *   Title (H3): "Generated Fantasy Name:"
    *   A single content area to display a list of names.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users select a category, fill in a theme (optional), and quantity, then click the "Forge Name!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang world-builder, loremaster, dan ahli bahasa fiktif untuk dunia fantasi.

    Berdasarkan kriteria berikut:
    - Kategori Nama: [Kategori dari pilihan pengguna]
    - Tema/Ras: [Tema dari input pengguna, jika ada]
    - Jumlah Nama: [Jumlah dari input pengguna]

    Tugas Anda adalah menciptakan nama-nama fantasi yang unik dan terdengar otentik. Untuk setiap nama, berikan juga etimologi fiktif (asal-usul atau makna nama) yang singkat dan menarik.

    Gunakan format Markdown berikut untuk setiap entri:
    **[Nama yang Dihasilkan]** - *[Etimologi fiktif singkat]*
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted list of names in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Select Category Name:" option to:**
`Character`
*   **Fill in the "Theme or Race (Optional):" column with:**
`Ancient forest guardian elves`
*   **Set "Number of Desired Names:" to:**
`5`
---
