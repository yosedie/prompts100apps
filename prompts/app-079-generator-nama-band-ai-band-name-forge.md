## Application Name
AI Band Name Generator: Band Name Forge

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps musicians find cool and unique band names. Users select their music genre, and the AI ​​will generate 10 creative band name ideas that fit that genre.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Band Name Generator".
2.  **User Input Form:**
    *   **Genre Selection:** A dropdown (select) menu with the label "Select Your Music Genre:" and the options: "Indie Rock", "Heavy Metal", "Pop Punk", "Electronic Dance Music (EDM)", "Acoustic Folk", "Alternative Hip Hop".
3.  **Action Buttons:** A main button with the text "Generate Band Name!". While the process is running, the button should be disabled and display the status "Tuning Up...".
4.  **Output Area:**
    *   Title (H3): "10 Band Name Ideas For You:"
    *   A single content area to display 10 names in a numbered list.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a genre and clicks the "Generate Band Name!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang produser musik dan pencari bakat (A&R scout) yang sangat keren dan memiliki selera musik yang tinggi. Anda tahu nama seperti apa yang akan terlihat bagus di poster konser.

    Berdasarkan genre musik berikut:
    """
    [Genre dari pilihan pengguna]
    """

    Tugas Anda adalah membuat **10 ide nama band** yang unik, keren, dan cocok dengan nuansa genre tersebut.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 10 band name ideas in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Choose Your Music Genre:" option to:**
`Indie Rock`
---
