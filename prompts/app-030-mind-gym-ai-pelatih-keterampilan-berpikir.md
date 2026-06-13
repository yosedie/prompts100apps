## Application Name
Mind Gym AI: Thinking Skills Trainer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an interactive web application that functions as a trainer to hone thinking skills. Users select the type of skill they want to train (critical, lateral, or systemic), and the AI ​​will present a scenario or puzzle specifically designed to practice that skill, complete with the option to ask for hints and view answers.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Mind Gym AI".
2.  **User Input Form:**
    *   **Skill Selection:** A dropdown (select) menu with the label "Select the Skill You Want to Train:" and the options: "Critical Thinking", "Lateral Thinking", "Systemic Thinking".
3.  **Action Buttons:** A main button with the text "Start Workout". While the process is running, the button should be activated and display the status "Designing Exercise...".
4.  **Interactive Output Area:**
    *   **Scenario:** Title (H3) "Practice Scenario:" followed by a content area to display the puzzle from the AI.
    *   **Hint Button:** A button with the text "Request a Hint". When clicked, a hidden area underneath will appear showing clues.
    *   **Answer Button:** A button with the text "Show Answer & Explanation". When clicked, a hidden area underneath will appear showing the complete answer.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax into properly formatted HTML elements. Apply this rendering to all sections in the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a skill and clicks the "Start Practice" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang fasilitator dan pelatih keterampilan berpikir (thinking skills coach) yang ahli dalam merancang skenario dan teka-teki yang menantang.

    Berdasarkan keterampilan yang dipilih:
    - Keterampilan: [Keterampilan dari pilihan pengguna]

    Tugas Anda adalah membuat TIGA bagian konten yang terpisah:
    1.  **Skenario/Teka-Teki:** Buat sebuah skenario atau teka-teki yang dirancang khusus untuk melatih keterampilan yang dipilih.
        - Untuk 'Berpikir Kritis', berikan skenario dengan informasi yang mungkin bias atau tidak lengkap.
        - Untuk 'Berpikir Lateral', berikan teka-teki klasik yang membutuhkan solusi "out-of-the-box".
        - Untuk 'Berpikir Sistemik', berikan skenario tentang sistem yang saling terhubung dan tanyakan tentang konsekuensi yang tidak terduga.
    2.  **Petunjuk (Hint):** Berikan satu kalimat petunjuk yang mengarahkan pemikiran tanpa memberikan jawaban.
    3.  **Jawaban & Penjelasan:** Berikan jawaban yang jelas, dan yang terpenting, jelaskan MENGAPA jawaban itu benar dan BAGAIMANA cara berpikir yang benar digunakan untuk mencapainya.

    Gunakan format berikut dengan pemisah yang jelas:
    [Teks Skenario/Teka-Teki Anda di sini]
    ---HINT---
    [Teks Petunjuk Anda di sini]
    ---SOLUTION---
    [Teks Jawaban & Penjelasan Anda di sini]
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response, the application parses the text using `---HINT---` and `---SOLUTION---` separators to separate the three pieces of content.
5.  The application displays the main scenario, and stores clues and answers to display when the appropriate button is clicked.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, set the default options in the dropdown menu when the page first loads:**

*   **Set the "Select Skills You Want to Train:" option to:**
`Critical Thinking`
---
