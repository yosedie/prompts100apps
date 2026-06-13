## Application Name
AI Universal Prayer Generator: Words of Reflection

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that writes prayers, reflections, or reflections that are universal and non-denominational. Users select a theme, and AI will generate a text that focuses on shared human values ​​such as hope, gratitude, strength, or peace.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Universal Prayer Generator".
2.  **User Input Form:**
    *   **Theme Selection:** A dropdown (select) menu with the label "Choose Your Reflection Theme:" and options: "Gratitude", "Hope in Difficult Times", "Strength for Today", "Inner Peace".
3.  **Action Button:** A main button with the text "Write Contemplation". While the process is running, the button should be activated and display the status "Searching for Words...".
4.  **Output Area:**
    *   Title (H3): "A Contemplation For You:"
    *   A single content area to display all text.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a theme and clicks the “Write Contemplation” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis spiritual dan filsuf yang bijaksana. Anda mampu merangkai kata-kata yang menenangkan dan menginspirasi, tanpa terikat pada satu agama atau kepercayaan tertentu.

    Berdasarkan tema berikut:
    """
    [Tema dari pilihan pengguna]
    """

    Tugas Anda adalah menulis sebuah doa atau perenungan singkat yang bersifat universal. Teks harus:
    - Fokus pada perasaan dan nilai-nilai kemanusiaan yang terkait dengan tema.
    - Menggunakan bahasa yang inklusif dan dapat diterima oleh siapa saja, dari latar belakang apa pun.
    - Menawarkan kata-kata penghiburan, kekuatan, atau perspektif.
    - Puitis namun sederhana dan tulus.

    PENTING: Hindari penggunaan nama atau istilah spesifik dari agama manapun.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the reflection text in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Choose Your Contemplation Theme:" option to:**
`Gratitude`
---
