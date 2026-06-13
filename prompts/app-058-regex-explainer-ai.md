## Application Name
Regex Explainer AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a utility web application that functions as a regular expression (regex) translator. Users enter a complex regex pattern, and AI will break it down piece by piece and explain it in easy-to-understand human language.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Regex Explainer AI".
2.  **User Input Form:**
    *   A text input field with the label "Paste your Regular Expression (Regex):". This input must use a monospaced font.
3.  **Action Button:** A main button with the text "Explain This Regex!". While the process is running, the button should be activated and display the status "Deciphering...".
4.  **Output Area:**
    *   Title (H3): "Regex Explanation:"
    *   A single content area to display detailed explanations.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**`, `*`, and small code blocks) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a regex pattern and clicks the "Explain This Regex!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang programmer senior dan ahli ekspresi reguler (regex). Anda sangat pandai dalam membaca pola regex yang paling rumit sekalipun dan menjelaskannya kepada orang lain.

    Berdasarkan ekspresi reguler berikut:
    """
    [Regex dari input pengguna]
    """

    Tugas Anda adalah memberikan penjelasan yang terperinci untuk setiap bagian dari regex ini. Uraikan pola tersebut secara berurutan dan jelaskan apa yang dicocokkan oleh setiap token atau grup.

    Gunakan format Markdown untuk menyajikan penjelasan dengan rapi, misalnya dengan daftar poin atau tabel.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted explanation in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Paste your Regular Expression (Regex):" column with:**
`^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$`
---
