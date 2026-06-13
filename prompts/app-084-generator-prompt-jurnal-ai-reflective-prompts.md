## Application Name
AI Journal Prompt Generator: Reflective Prompts

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a simple web application that functions as a trigger for journaling. Users enter one word that describes how they are feeling today, and the AI ​​will generate 5 deep, introspective journal questions to help users reflect and understand those feelings.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Journal Prompt Generator".
2.  **User Input Form:**
    *   A text input field labeled "One Word That Describes How You Feel Today:".
3.  **Action Button:** A main button with the text "Give Me a Journal Prompt". While the process is running, the button should be activated and display the status "Searching for Questions...".
4.  **Output Area:**
    *   Title (H3): "5 Journal Prompts For You:"
    *   A single content area to display 5 questions in a numbered list.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users enter one feeling word and click the “Give Me a Journal Prompt” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang terapis dan pemandu jurnal (journaling facilitator) yang bijaksana. Anda ahli dalam membuat pertanyaan yang menggugah pikiran untuk refleksi diri.

    Berdasarkan satu kata perasaan dari pengguna berikut:
    """
    [Kata dari input pengguna]
    """

    Tugas Anda adalah membuat **5 pertanyaan jurnal yang mendalam**. Pertanyaan-pertanyaan ini harus membantu pengguna untuk:
    - Mengeksplorasi akar dari perasaan tersebut.
    - Memahami bagaimana perasaan itu bermanifestasi dalam tubuh dan pikiran mereka.
    - Menemukan apa yang bisa mereka pelajari dari perasaan itu.
    - Mempertimbangkan tindakan apa yang bisa diambil (jika perlu).

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 5 journal prompts in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "One Word That Describes How You Feel Today" column with:**
`Tired`
---
