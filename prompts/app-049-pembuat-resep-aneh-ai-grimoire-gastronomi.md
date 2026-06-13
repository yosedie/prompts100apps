## Application Name
Weird Recipe Generator AI: Gastronomic Grimoire

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an entertainment web application that generates weird and funny food recipes. Users choose a persona (Alien or Witch) and a normal food name, then the AI ​​will rewrite the recipe as if it were from another world, complete with nonsensical ingredients and steps.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Weird Recipe Generator".
2.  **User Input Form:**
    *   **Persona Selection:** A dropdown (select) menu with the label "Select Recipe Author:" and options: "Alien from the Zorp Galaxy", "Witch from the Dark Forest".
    *   **Food Input:** A text input field labeled "Normal Food Name You Want to Make Weird:".
3.  **Action Buttons:** A main button with the text "Create Weird Recipes!". While the process is running, the button should be disabled and display the status "Stirring the Cauldron...".
4.  **Output Area:**
    *   Title (H3): "Recipe from Another Dimension:"
    *   A single content area to display all recipes.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a persona, enters a food name, and clicks the “Create a Weird Recipe!” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah [Persona dari pilihan pengguna] yang sedang menulis buku resep untuk kaum Anda.

    Berdasarkan makanan manusia berikut:
    """
    [Nama makanan dari input pengguna]
    """

    Tugas Anda adalah membuat versi resep yang aneh dan lucu dari makanan tersebut, dari sudut pandang Anda. Resep harus mencakup:

    1.  **Nama Resep Aneh:** Beri nama baru yang sesuai dengan persona Anda (contoh: "Tumis Meteor" atau "Sup Akar Mandrake").
    2.  **Bahan-Bahan Aneh:** Ganti bahan-bahan normal dengan bahan fiktif yang lucu dari dunia Anda (contoh: 'air mata naga', 'baut bekas kapal luar angkasa', 'bubuk cahaya bulan').
    3.  **Langkah-Langkah Aneh:** Tulis langkah-langkah memasak yang tidak masuk akal atau menggunakan alat-alat aneh (contoh: "Aduk menggunakan obeng sonik," atau "Bacakan mantra pemanggil rasa").

    Gunakan format Markdown untuk menyusun resep dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The app displays pre-formatted strange recipes in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Select Recipe Author:" option to:**
`Witch of the Dark Forest`
*   **Fill in the "Normal Food Name You Want to Make Weird" column with:**
`Fried Rice`
---
