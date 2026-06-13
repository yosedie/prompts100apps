## Application Name
AI Fictitious Tradition Designer: Cultural Weaver

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for writers and world-builders who create fictional cultural traditions. Users enter the name of the community and their core values, and then the AI ​​will design a unique festival, ritual, or tradition that reflects those values.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Fictitious Tradition Designer".
2.  **User Input Form:**
    *   **Input Society Name:** A text input field labeled "Your Fictitious Society Name:".
    *   **Core Values ​​Input:** A text area labeled "What are the Core Values ​​of This Society? (separate with commas)".
3.  **Action Button:** A main button with the text "Create a Tradition". While the process is running, the button should be activated and display the status "Culture Weaving...".
4.  **Output Area:**
    *   Title (H3): "Resulting Traditions:"
    *   A single content area to display all tradition descriptions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users enter the name of the society and its values, then click the "Create Tradition" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang antropolog budaya dan sejarawan fiksi. Anda ahli dalam merancang tradisi dan ritual yang terasa otentik dan memiliki makna mendalam bagi sebuah masyarakat.

    Berdasarkan informasi masyarakat fiktif berikut:
    - Nama Masyarakat: [Nama dari input pengguna]
    - Nilai-Nilai Inti: [Nilai-nilai dari input pengguna]

    Tugas Anda adalah merancang SATU tradisi, festival, atau ritual unik untuk masyarakat ini. Deskripsi tradisi harus mencakup:

    1.  **Nama Tradisi:** Berikan nama yang khas untuk tradisi ini.
    2.  **Tujuan & Makna:** Jelaskan mengapa tradisi ini ada dan nilai inti apa yang direpresentasikannya.
    3.  **Pelaksanaan:** Deskripsikan secara singkat bagaimana tradisi ini dirayakan atau dilakukan (misalnya, waktu, aktivitas, simbol yang digunakan).

    Gunakan format Markdown untuk menyusun deskripsi dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a description of the tradition in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Name of Your Fictitious Society:" column with:**
`The Mountain Forgers`
*   **Fill in the "What Are the Core Values ​​of This Society?..." column with:**
`Courage, Community, Honor to Ancestors`
---
