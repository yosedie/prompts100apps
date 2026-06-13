## Application Name
AI Short Biography Author: Bio in Brief

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that writes short biographies (around 150 words) about historical or fictional figures. Users only need to enter a figure's name, and the AI ​​will generate a concise summary, highlighting their most important achievements and impact.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "A Short Biography of AI".
2.  **User Input Form:**
    *   A text input field labeled "Enter Name of Character (Historical or Fictional):".
3.  **Action Button:** A main button with the text "Write a Biography". While the process is running, the button should be activated and display the status "Researching...".
4.  **Output Area:**
    *   Title (H3): "Brief Biography:"
    *   A single content area to display the entire biography.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the character's name and clicks the "Write Biography" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang sejarawan dan penulis biografi yang ahli dalam merangkum kehidupan seseorang secara ringkas namun berdampak.

    Berdasarkan nama tokoh berikut:
    """
    [Nama tokoh dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah biografi singkat, sekitar 150 kata. Biografi harus:
    - Memperkenalkan siapa tokoh tersebut.
    - Menyoroti pencapaian atau kontribusi mereka yang paling signifikan.
    - Menjelaskan dampak atau warisan abadi mereka.
    - Ditulis dalam gaya ensiklopedis yang jelas dan informatif.

    PENTING: Hanya berikan teks biografinya saja, tanpa tambahan komentar.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a biography in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Name of Character (Historical or Fictional):" column with:**
`Albert Einstein`
---
