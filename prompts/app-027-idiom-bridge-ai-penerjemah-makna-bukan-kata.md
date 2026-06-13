## Application Name
Idiom Bridge AI: Translator of Meanings, Not Words

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a linguistic web application capable of translating idioms. This application does not translate literally, but rather explains the actual meaning of the idiom and provides an equivalent idiom that has a similar meaning in the target language.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Idiom Bridge AI".
2.  **User Input Form:**
    *   **Input Idiom:** A text input field labeled "Enter Idiom:".
    *   **Language Selection:** Two dropdown (select) menus side by side:
        *   "From Language:" with options "Indonesia", "English".
        *   "To Language:" with options "English", "Indonesia".
3.  **Action Button:** A main button with the text "Translate Meaning". While the process is running, the button should be activated and display the status "Bridging Meaning...".
4.  **Output Area:** Designed with three clear sections:
    *   **Section 1: Literal Translation:** Heading (H3) "Literal Translation" followed by the content area.
    *   **Section 2: Actual Meaning:** Title (H3) "Real Meaning (Meaning)" followed by the content area.
    *   **Section 3: Equivalent Idioms:** Title (H3) "Equivalent Idioms" followed by the content area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters an idiom, selects a language, and clicks a button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli bahasa (linguist) dan pakar budaya yang memahami nuansa idiom di berbagai bahasa.

    Berdasarkan permintaan berikut:
    - Idiom: "[Idiom dari input pengguna]"
    - Terjemahkan dari: [Bahasa sumber dari pilihan pengguna]
    - Terjemahkan ke: [Bahasa target dari pilihan pengguna]

    Tugas Anda adalah memberikan TIGA informasi dalam format yang jelas:

    1.  **Terjemahan Harfiah:** Terjemahkan idiom ini kata per kata.
    2.  **Makna Sebenarnya:** Jelaskan arti atau makna sesungguhnya dari idiom ini.
    3.  **Padanan Idiom:** Berikan idiom dalam bahasa target yang memiliki makna paling mirip. Jika tidak ada padanan langsung, berikan frasa umum yang setara.

    Gunakan format Markdown berikut untuk jawaban Anda:
    **Terjemahan Harfiah:** [Jawaban Anda]
    **Makna Sebenarnya:** [Jawaban Anda]
    **Padanan Idiom:** [Jawaban Anda]
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application parses the text to separate the three parts.
5.  The application renders the Markdown content and displays it in three appropriate sections in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow for live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Idiom:" column with:**
`Black sheep`
*   **Set the "From Language:" option to:**
`Indonesia`
*   **Set the "To Language:" option to:**
`England`
---
