## Application Name
Fictitious Conspiracy Generator: The Truth Is In Here AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that creates a conspiracy theory that sounds convincing (but is completely fictional and for entertainment). Users enter an object or everyday event, and the AI ​​will generate an elaborate and humorous conspiracy theory about it.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Fictitious Conspiracy Generator".
2.  **User Input Form:**
    *   A text input field labeled "What Everyday Object or Event Do You Want to Reveal?".
3.  **Action Button:** A main button with the text "Reveal the Truth!". While the process is running, the button should be activated and display the status "Connecting the Dots...".
4.  **Output Area:**
    *   Title (H3): "The 'True' Conspiracy Theory:"
    *   A single content area to display the entire theory.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the object/event and clicks the "Reveal the Truth!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli teori konspirasi veteran dan peneliti 'kebenaran tersembunyi'. Anda mampu melihat pola dan hubungan rahasia di balik hal-hal yang paling biasa sekalipun.

    Berdasarkan objek/peristiwa sehari-hari berikut:
    """
    [Input dari pengguna]
    """

    Tugas Anda adalah menciptakan SATU teori konspirasi yang terdengar meyakinkan, rumit, namun sepenuhnya fiktif dan menghibur. Teori harus memiliki struktur berikut:

    - **Apa yang 'Mereka' Ingin Anda Percaya:** Jelaskan penjelasan yang umum atau membosankan.
    - **Kebenaran yang Sebenarnya:** Ungkap "kebenaran" yang tersembunyi di baliknya.
    - **'Bukti' yang Tak Terbantahkan:** Berikan beberapa "bukti" yang terdengar masuk akal tapi sebenarnya tidak berhubungan.
    - **Apa Tujuan Mereka Sebenarnya?:** Jelaskan motif tersembunyi di balik konspirasi ini.

    Gunakan format Markdown untuk menyusun teori dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays conspiracy theories that have been formatted in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What everyday objects or events do you want to reveal?" with:**
`A sock is missing one side`
---
