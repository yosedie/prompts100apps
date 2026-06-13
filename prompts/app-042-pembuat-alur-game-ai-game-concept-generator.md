## Application Name
AI Game Flow Generator: Game Concept Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for game designers and writers. Users enter the game genre and one sentence of the main idea, and the AI ​​will generate a more complete game concept, including the title, core mechanics, and basic storyline.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Gameplay Generator".
2.  **User Input Form:**
    *   **Genre Selection:** A dropdown menu (select) with the label "Select Game Genre:" and options: "Fantasy RPG", "Sci-Fi Adventure", "Psychological Horror", "Puzzle Platformer", "Strategy".
    *   **Main Idea Input:** A text input field labeled "Game Main Idea (1 Sentence):".
3.  **Action Button:** A main button with the text "Create a Game Concept!". While the process is running, the button should be activated and display the status "Developing...".
4.  **Output Area:**
    *   Title (H3): "Your Game Concept:"
    *   A single content area to showcase the entire concept.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users select a genre, enter an idea, and click the "Create Game Concept!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang desainer game (game designer) dan penulis naratif yang berpengalaman.

    Berdasarkan informasi awal berikut:
    - Genre: [Genre dari pilihan pengguna]
    - Ide Utama: [Ide dari input pengguna]

    Tugas Anda adalah mengembangkan ide singkat ini menjadi konsep game yang lebih konkret. Konsep tersebut harus mencakup:

    1.  **Judul Game (Working Title):** Berikan satu judul yang menarik.
    2.  **Konsep Inti (Core Concept):** Tulis satu paragraf singkat yang menjelaskan premis utama game.
    3.  **Mekanik Utama (Core Mechanic):** Jelaskan secara singkat apa yang dilakukan pemain dalam game (gameplay loop).
    4.  **Alur Cerita Dasar (Basic Plot Outline):** Buat kerangka cerita sederhana dalam tiga babak: Awal (pengenalan konflik), Tengah (eskalasi dan tantangan), dan Akhir (klimaks dan resolusi).

    Gunakan format Markdown untuk menyusun konsep dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted game concept in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Select Game Genre:" option to:**
`Fantasy RPG`
*   **Fill in the "Main Idea of ​​the Game (1 Sentence):" column with:**
`A librarian discovers that books in an ancient library can change reality.`
---
