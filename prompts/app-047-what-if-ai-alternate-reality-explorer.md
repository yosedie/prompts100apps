## Application Name
What If AI: Alternate Reality Explorer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that allows users to explore alternative historical or fictional scenarios. Users ask “What if…” questions, and the AI ​​will write a narrative essay exploring the consequences and alternative realities of the scenario.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "What If AI: Alternate Reality Explorer".
2.  **User Input Form:**
    *   A large text area labeled "Ask Your 'What If...' Question:".
3.  **Action Buttons:** A main button with the text "Explore Scenarios!". While the process is running, the button should be activated and display the status "Browsing the Timeline...".
4.  **Output Area:**
    *   Title (H3): "Exploration of Alternative Scenarios:"
    *   A single content area to display the entire essay.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a “What if” scenario and clicks the “Explore Scenarios!” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang sejarawan sejarah alternatif dan penulis fiksi spekulatif. Anda ahli dalam menganalisis titik-titik percabangan dalam sejarah dan mengeksplorasi konsekuensi jangka panjangnya.

    Berdasarkan pertanyaan "Bagaimana jika" berikut:
    """
    [Pertanyaan dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah esai naratif yang mendalam yang menjelajahi skenario ini. Esai Anda harus mencakup:
    - **Konsekuensi Langsung:** Apa yang akan langsung berubah setelah peristiwa percabangan ini?
    - **Efek Riak (Ripple Effects):** Bagaimana perubahan awal ini memengaruhi perkembangan teknologi, sosial, budaya, dan politik dalam dekade atau abad berikutnya?
    - **Dunia Saat Ini:** Gambarkan seperti apa dunia "saat ini" dalam lini masa alternatif ini.

    Gunakan gaya penulisan yang menarik dan informatif. Gunakan format Markdown untuk menyusun esai dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted essay in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Ask Your 'What If...' Question:" field with:**
`What if the internet had never been invented?`
---
