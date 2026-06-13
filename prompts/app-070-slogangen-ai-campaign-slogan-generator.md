## Application Name
SloganGen AI: Campaign Slogan Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a campaign slogan generator. Users describe the main goal and target audience of their campaign, then AI will generate several slogan options that are catchy, concise and easy to remember.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Gen Slogan".
2.  **User Input Form:**
    *   **Input Campaign Goal:** A text area labeled "What is the Main Goal of Your Campaign?".
    *   **Target Audience Input:** A text input field labeled "Who is your Main Target Audience?".
3.  **Action Button:** A main button with the text "Create a Slogan!". While the process is running, the button should be activated and display the status "Brainstorming...".
4.  **Output Area:**
    *   Headline (H3): "5 Campaign Slogan Options:"
    *   A single content area to display 5 slogans in a numbered list.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the campaign details and clicks the “Create Slogan!” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang copywriter senior dan ahli branding yang berspesialisasi dalam menciptakan slogan kampanye yang kuat dan berkesan.

    Berdasarkan informasi kampanye berikut:
    - Tujuan Utama: """[Tujuan dari input pengguna]"""
    - Target Audiens: """[Audiens dari input pengguna]"""

    Tugas Anda adalah membuat **5 opsi slogan** yang berbeda. Setiap slogan harus:
    - Ringkas (idealnya 3-7 kata).
    - Mudah diingat dan diucapkan.
    - Menarik secara emosional atau rasional bagi target audiens.
    - Mencerminkan tujuan utama kampanye.

    Sajikan hasilnya dalam format daftar bernomor.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 5 slogan options in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What is the Main Goal of Your Campaign?" with:**
`Encouraging people to reduce the use of single-use plastics and switch to more environmentally friendly alternatives.`
*   **Fill in the column "Who is your main target audience?" with:**
`Young people and families who care about the environment.`
---
