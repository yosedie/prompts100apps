## Application Name
AI Negative Thought Reframer: CBT Thought Helper

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application based on the principles of Cognitive Behavioral Therapy (CBT). Users enter an automatic negative thought, and AI will help rewrite it into 3 alternative perspectives that are more balanced, realistic, and constructive.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Negative Thought Reframer".
2.  **User Input Form:**
    *   A large text area labeled "Write Down Negative Thoughts That Disturb You:".
3.  **Action Buttons:** A main button with the text "Search for New Perspectives". While the process is running, the button should be activated and display the status "Searching for Balance...".
4.  **Output Area:**
    *   **Important Disclaimer:** Directly above the results, display warning text: "**Note:** This app is an aid to self-reflection and is not a substitute for advice from a mental health professional."
    *   Title (H3): "3 Alternative, More Balanced Perspectives:"
    *   A single content area to display 3 perspectives in a numbered list.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a negative thought and clicks the “Search for a New Perspective” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang terapis yang terlatih dalam Terapi Perilaku Kognitif (CBT). Anda ahli dalam membantu orang mengidentifikasi distorsi kognitif dan menemukan cara berpikir yang lebih seimbang.

    Berikut adalah pemikiran negatif otomatis dari seorang pengguna:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menulis **3 perspektif alternatif** yang lebih seimbang dan konstruktif. Perspektif ini harus:
    - Menantang pemikiran absolut (seperti "selalu" atau "tidak pernah").
    - Memisahkan perasaan dari fakta.
    - Menghindari "toxic positivity" (terlalu positif), melainkan fokus pada realisme yang penuh harapan.
    - Membuka kemungkinan lain selain skenario terburuk.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 3 alternative perspectives in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Write Down Negative Thoughts That Disturb You" column with:**
`I failed miserably in the presentation earlier, I will definitely be fired.`
---
