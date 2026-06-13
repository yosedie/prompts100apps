## Application Name
AI Menu Description Author: Gourmet Wordsmith

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that turns a simple ingredient list into a mouth-watering menu description. Users enter the name of the dish and its main ingredients, then AI will write a poetic and luxurious description, just like in a five-star restaurant.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Menu Description Writer".
2.  **User Input Form:**
    *   **Input Dish Name:** A text input field labeled "Dish Name:".
    *   **Main Ingredients Input:** A text area with the label "Main Ingredients (separate with commas):".
3.  **Action Button:** A main button with the text "Write a Fancy Description". While the process is running, the button should be activated and display the status "Composing Words...".
4.  **Output Area:**
    *   Title (H3): "Appetizing Menu Description:"
    *   A single content area to display descriptions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the name of the dish and ingredients, then clicks the "Write a Fancy Description" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis menu profesional (menu writer) untuk restoran fine dining. Anda ahli dalam menggunakan kata-kata yang deskriptif dan menggugah selera untuk membuat hidangan terdengar mewah dan tak tertahankan.

    Berdasarkan informasi hidangan berikut:
    - Nama Hidangan: [Nama dari input pengguna]
    - Bahan Utama: [Bahan dari input pengguna]

    Tugas Anda adalah menulis SATU paragraf deskripsi menu yang singkat namun puitis. Deskripsi harus:
    - Menggunakan kata-kata sensorik (menggambarkan tekstur, aroma, dan rasa).
    - Menyoroti kualitas bahan-bahan.
    - Membuat hidangan terdengar seperti sebuah pengalaman kuliner yang istimewa.

    PENTING: Hanya berikan teks deskripsinya saja, tanpa tambahan komentar.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays menu descriptions in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Dish Name:" column with:**
`Honey Grilled Chicken`
*   **Fill in the "Main Ingredients (separate with commas):" column with:**
`chicken, honey, garlic, ginger, soy sauce, chili sauce`
---
