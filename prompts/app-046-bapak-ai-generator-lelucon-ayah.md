## Application Name
Father AI: Dad Joke Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a simple web application that functions as a non-stop generator of dad jokes. Users enter a keyword, and the AI ​​will create a dime joke or pun based on that keyword.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Father of AI".
2.  **User Input Form:**
    *   A text input field labeled "Give me one keyword:".
3.  **Action Button:** A main button with the text "Make a Joke!". While the process is running, the button should be activated and display the status "Looking for spare change...".
4.  **Output Area:**
    *   Title (H3): "Daddy Jokes For You:"
    *   A single content area designed like a card or chat bubble to display jokes.
    *   **More Button!:** Below the joke, include a "More Dong!" which will create a new joke with the same keyword without needing to click the main button again.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (if any) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a keyword and clicks the "Make a Joke!" or "Again Dong!".
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang "Bapak-Bapak" dengan selera humor yang sangat receh. Anda adalah raja dari dad jokes dan permainan kata (puns).

    Berdasarkan kata kunci berikut:
    """
    [Kata kunci dari input pengguna]
    """

    Tugas Anda adalah membuat SATU lelucon ayah yang orisinal dan receh. Lelucon harus dalam format tanya-jawab.

    PENTING: Hanya berikan teks leluconnya saja, tanpa tambahan komentar atau emoji.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays pre-formatted jokes in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Give me one keyword:" column with:**
`Fish`
---
