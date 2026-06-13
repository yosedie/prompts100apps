## Application Name
AI Magic Spell Generator: Spellbook Crafter

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a creative web application that creates fictional "spells" or "magic spells." The user describes the desired magic effect, and the AI ​​will generate spell names, rhyming incantations, and interesting little side effects.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Magic Spell Generator".
2.  **User Input Form:**
    *   A text area labeled "What is the Desired Magic Effect?".
3.  **Action Button:** A main button with the text "Cast a Spell!". While the process is running, the button should be activated and display the status "Gathering Mana...".
4.  **Output Area:**
    *   Title (H3): "Created Spell:"
    *   A single content area to display all spell details.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a magic effect and clicks the "Cast a Spell!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang Archmage, penjaga perpustakaan sihir kuno. Anda adalah pencipta mantra yang tak tertandingi.

    Berdasarkan efek sihir yang diinginkan berikut:
    """
    [Efek dari input pengguna]
    """

    Tugas Anda adalah menciptakan satu mantra sihir yang lengkap. Mantra harus mencakup:

    1.  **Nama Mantra:** Nama yang terdengar magis dan sesuai dengan efeknya.
    2.  **Rapalan (Incantation):** Beberapa baris kalimat yang berima dan puitis untuk mengucapkan mantra.
    3.  **Efek Samping Kecil:** Sebuah efek samping yang menarik atau sedikit lucu (contoh: "rambut pengguna akan berkilau selama satu jam").

    Gunakan format Markdown untuk menyusun detail mantra dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The app displays spell details in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What is the Desired Magic Effect?" with:**
`Making a cup of warm tea appear in hand.`
---
