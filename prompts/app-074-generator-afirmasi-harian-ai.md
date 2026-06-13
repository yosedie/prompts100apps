## Application Name
AI Daily Affirmations Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a personalized positive affirmation generator. Users write down their goals, focuses, or challenges they face that day, and AI will create a specific, empowering, and ready-to-speak affirmation.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Daily Affirmation Generator".
2.  **User Input Form:**
    *   A text area labeled "What is your focus or challenge today?".
3.  **Action Button:** A main button with the text "Create My Affirmation". While the process is running, the button should be activated and display the status "Seeking Power...".
4.  **Output Area:**
    *   Title (H3): "Your Affirmation for Today:"
    *   A single content area to display affirmations. The design can be made to stand out like a quote card.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a focus/challenge and clicks the “Create My Affirmation” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pelatih mindfulness dan ahli dalam psikologi positif. Anda mampu merumuskan kalimat yang memberdayakan.

    Berdasarkan fokus atau tantangan pengguna berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah mengubah input tersebut menjadi SATU kalimat afirmasi positif yang kuat. Afirmasi harus:
    - Ditulis dari sudut pandang orang pertama ("Saya...").
    - Bersifat aktif dan berorientasi pada tindakan.
    - Mengubah tantangan menjadi pernyataan kekuatan.
    - Spesifik dan relevan dengan input pengguna.

    PENTING: Hanya berikan kalimat afirmasinya saja, tanpa tambahan komentar atau penjelasan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted affirmation in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the column "What is your focus or challenge today?" with:**
`I have an important presentation in front of a client and am feeling very nervous.`
---
