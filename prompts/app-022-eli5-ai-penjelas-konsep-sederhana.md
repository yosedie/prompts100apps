## Application Name
ELI5 AI: Simple Concept Explainer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that can simplify a very complex topic. Users enter a difficult subject, and the AI ​​will explain it with the “Explain Like I'm 5” (ELI5) method, using simple analogies, easy language, and no technical jargon.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "ELI5 AI: Explain Like I'm 5 Years Old".
2.  **User Input Form:**
    *   A text input field labeled "Enter a Complex Topic You Want to Explain:".
3.  **Action Button:** A main button with the text "Make It Easy!". While the process is running, the button should be disabled and display the status "Simplifying...".
4.  **Output Area:**
    *   Title (H3): "Simple Explanation:"
    *   A single content area to display explanations.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` or `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users enter a topic and click the "Make It Easy!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang guru yang sangat sabar dan ahli dalam menyederhanakan konsep-konsep yang rumit untuk anak-anak.

    Berikut adalah topik yang perlu Anda jelaskan:
    """
    [Topik dari input pengguna]
    """

    Tugas Anda adalah menjelaskan topik ini seolah-olah Anda sedang berbicara kepada anak berusia 5 tahun (Explain Like I'm 5).

    Gunakan aturan berikut:
    - Gunakan kalimat yang sangat pendek dan bahasa yang sederhana.
    - Gunakan analogi atau perumpamaan yang mudah dimengerti oleh anak-anak (misalnya, mainan, makanan, hewan, taman bermain).
    - HINDARI jargon teknis sama sekali.
    - Fokus pada ide utamanya, bukan pada detail teknis yang akurat.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted explanation in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter the Complex Topic You Want to Explain:" column with:**
`Blockchain`
---
