## Application Name
AI Healthy Recipe Modifier: Healthy Recipe Makeover

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a virtual nutritionist. Users paste in a recipe, and AI will analyze it to provide suggestions for ingredient substitutions and cooking methods to make the recipe healthier, without significantly sacrificing taste.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Healthy Recipe Modifier".
2.  **User Input Form:**
    *   A large text area labeled "Paste Your Complete Recipe Here (Ingredients & Steps):".
3.  **Action Button:** A main button with the text "Make It Healthier!". While the process is running, the button should be activated and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Healthy Recipe Modification Suggestions:"
    *   A single content area to display all suggestions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users paste in a recipe and click the "Make It Healthier!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli gizi (nutritionist) dan koki yang ahli dalam memasak sehat. Anda tahu cara memodifikasi resep agar lebih bergizi tanpa membuatnya hambar.

    Berikut adalah resep yang perlu dimodifikasi:
    """
    [Teks resep dari input pengguna]
    """

    Tugas Anda adalah memberikan saran modifikasi untuk membuat resep ini lebih sehat. Kelompokkan saran Anda ke dalam dua bagian:

    1.  **Substitusi Bahan:** Sarankan bahan-bahan pengganti yang lebih sehat (misalnya, ganti tepung terigu dengan tepung gandum, gula dengan pemanis alami, minyak goreng dengan minyak zaitun). Jelaskan mengapa penggantian ini lebih baik.
    2.  **Modifikasi Metode Memasak:** Sarankan perubahan dalam cara memasak untuk mengurangi lemak atau kalori (misalnya, ganti 'goreng' dengan 'panggang' atau 'kukus').

    Gunakan format Markdown untuk menyusun saran dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays modification suggestions in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste Your Complete Recipe Here..." column with:**
`Fried Chicken Recipe with Flour

Material:
    - 1 chicken, cut into 8
    - 200g all-purpose flour
    - 1 tsp salt
    - 1 tsp pepper
    - Sufficient cooking oil

Step:
    1. Mix flour, salt and pepper.
    2. Coat the chicken pieces in the flour mixture until evenly coated.
    3. Heat a large amount of oil.
    4. Fry the chicken submerged in oil until golden brown and cooked.`
---
