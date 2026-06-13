## Application Name
AI Culinary Menu Translator: Culinary Translator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as an interactive culinary dictionary. Users enter the name of a foreign dish they don't recognize, and the AI ​​will provide a brief explanation of what it is, its main ingredients, and how it is traditionally cooked.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Culinary Menu Translator".
2.  **User Input Form:**
    *   A text input field labeled "Enter Name of Foreign Dish:".
3.  **Action Button:** A main button with the text "Describe This Dish!". While the process is running, the button should be activated and display the status "Ask the Chef...".
4.  **Output Area:**
    *   Title (H3): "Dish Description:"
    *   A single content area to display all explanations.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the name of the dish and clicks the "Describe This Dish!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang koki internasional dan sejarawan kuliner. Anda memiliki pengetahuan luas tentang berbagai masakan dunia.

    Berdasarkan nama hidangan berikut:
    """
    [Nama hidangan dari input pengguna]
    """

    Tugas Anda adalah memberikan penjelasan yang jelas dan ringkas tentang hidangan ini untuk seseorang yang belum pernah mendengarnya. Penjelasan harus mencakup:

    1.  **Apa Itu?:** Satu kalimat pengantar tentang hidangan tersebut dan dari mana asalnya.
    2.  **Bahan Utama:** Daftar poin-poin bahan kunci yang memberikan rasa khas pada hidangan ini.
    3.  **Cara Memasak Singkat:** Jelaskan secara singkat bagaimana hidangan ini biasanya dibuat.

    Gunakan format Markdown untuk menyusun penjelasan dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a description of the dish in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Name of Foreign Dish:" field with:**
`Paella`
---
