## Application Name
AI Poetic Weather Report

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that turns technical weather data into poetic and imaginative narrative descriptions. Users enter weather conditions, and the AI ​​will write a short paragraph that beautifully describes the mood of the day.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Poetic Weather Report".
2.  **User Input Form:**
    *   A text input field labeled "Enter Today's Weather Conditions:".
3.  **Action Button:** A main button with the text "Create a Poetic Description". While the process is running, the button should be activated and display the status "Feeling the Wind...".
4.  **Output Area:**
    *   Title (H3): "Today's Weather Report:"
    *   A single content area to display poetic descriptions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters weather conditions and clicks the “Create Poetic Description” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penyair dan penulis alam (nature writer). Anda mampu melihat keindahan dan cerita di balik fenomena cuaca yang paling biasa sekalipun.

    Berdasarkan data cuaca berikut:
    """
    [Kondisi cuaca dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah deskripsi cuaca yang puitis dan imajinatif dalam satu paragraf singkat (3-5 kalimat).
    - Gunakan metafora dan bahasa kiasan.
    - Fokus pada perasaan dan suasana yang diciptakan oleh cuaca tersebut.
    - Hindari menyebutkan angka atau data teknis secara langsung.

    Gunakan format Markdown untuk penekanan pada kata-kata tertentu jika perlu.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a poetic description in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Today's Weather Conditions:" column with:**
`Temperature 25 degrees Celsius, cloudy, a little windy.`
---
