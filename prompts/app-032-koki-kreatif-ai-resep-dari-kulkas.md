## Application Name
AI Creative Chef: Recipes from the Fridge

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that acts as a personal chef. Users enter a list of ingredients they have, and AI will create a creative and delicious recipe idea, complete with the name of the dish, list of ingredients, and steps for making it.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Creative Chef".
2.  **User Input Form:**
    *   A large text area labeled "What materials do you have? (separate with commas or new lines)".
3.  **Action Buttons:** A main button with the text "Look for Recipe Ideas!". While the process is running, the button should be disabled and display the status "Cooking...".
4.  **Output Area:**
    *   Title (H3): "Recipe Ideas For You:"
    *   A single content area to display all recipes.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a list of ingredients and clicks the "Search for Recipe Ideas!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang koki yang sangat kreatif dan inovatif, ahli dalam menciptakan masakan lezat dari bahan-bahan yang terbatas.

    Berikut adalah daftar bahan yang tersedia:
    """
    [Daftar bahan dari input pengguna]
    """

    Tugas Anda adalah membuat satu resep masakan yang menarik menggunakan bahan-bahan tersebut.
    - Anda boleh berasumsi pengguna memiliki bahan-bahan dasar seperti garam, merica, gula, minyak goreng, dan air.
    - Berikan nama yang kreatif untuk resep Anda.
    - Sajikan resep dalam format yang jelas: Nama Resep, Bahan-bahan, dan Langkah-langkah.

    Gunakan format Markdown untuk menyusun resep dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted recipe in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "What materials do you have?..." column with:**
`Rice left over from last night, 2 eggs, garlic, sweet soy sauce, spring onions`
---
