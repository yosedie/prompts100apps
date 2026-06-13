## Application Name
AI Silence Breaker: Ice Breaker Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users start conversations. Users enter the context of a social event, and AI will generate a list of ice breaker questions that are unique, interesting, and appropriate to the atmosphere of the event.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Silence Breaker".
2.  **User Input Form:**
    *   A text input field labeled "What is the Context of Your Social Event?".
3.  **Action Buttons:** A main button with the text "Give Me an Ice Breaker!". While the process is running, the button should be activated and display the status "Searching for Topics...".
4.  **Output Area:**
    *   Title (H3): "5 Conversation Starter Questions:"
    *   A single content area to display 5 questions in a numbered list.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the event context and clicks the "Give Me an Ice Breaker!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli komunikasi sosial dan fasilitator acara yang sangat pandai membuat orang merasa nyaman dan terhubung.

    Berdasarkan konteks acara berikut:
    """
    [Konteks dari input pengguna]
    """

    Tugas Anda adalah membuat **5 pertanyaan pembuka percakapan (ice breaker)** yang bagus. Pertanyaan-pertanyaan ini harus:
    - Sesuai dengan konteks acara yang diberikan.
    - Bersifat terbuka (bukan pertanyaan ya/tidak).
    - Menarik dan tidak terlalu personal atau aneh.
    - Dirancang untuk memicu cerita atau opini, bukan jawaban satu kata.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 5 questions in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "What is the Context of Your Social Event?" with:**
`Networking event for professionals in the technology industry.`
---
