## Application Name
Cron Job AI Translator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a utility web application that translates schedule descriptions in human language into correct cron job syntax. Users write when they want a task to run, and the AI ​​will generate the appropriate cron string.

## User Interface Components (UI Components)

1.  **Header:** The large headline says "Cron Job AI Translator".
2.  **User Input Form:**
    *   A text input field labeled "Describe Your Desired Schedule:".
3.  **Action Buttons:** A main button with the text "Generate Cron Syntax". While the process is running, the button should be activated and display the status "Calculating...".
4.  **Output Area:**
    *   Title (H3): "Your Cron Job Syntax:"
    *   A **read-only text area** designed like a code block (dark background, monospaced font) to display cron strings.
    *   **Copy Button:** There should be a "Copy" button next to the output area.
    *   **Explanation Area:** Below the cron syntax, include an area for a brief explanation of the meaning of each part of the generated cron string.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*`) into properly formatted HTML elements. Apply this rendering to the Explanation Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a schedule description and clicks the "Generate Cron Syntax" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang System Administrator (SysAdmin) Linux senior yang sangat ahli dalam menjadwalkan tugas menggunakan cron.

    Berdasarkan deskripsi jadwal dalam bahasa manusia berikut:
    """
    [Deskripsi dari input pengguna]
    """

    Tugas Anda adalah menghasilkan DUA hal:
    1.  **Sintaks Cron:** String cron job yang benar (* * * * *) yang sesuai dengan deskripsi.
    2.  **Penjelasan:** Penjelasan singkat untuk setiap bagian dari string cron tersebut (Menit, Jam, Hari dalam Bulan, Bulan, Hari dalam Minggu).

    Gunakan format berikut dengan pemisah yang jelas:
    [String cron job Anda di sini]
    ---EXPLANATION---
    [Penjelasan Anda di sini]
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response, the application parses the text using `---EXPLANATION---` separators.
5.  The application displays the cron string in the main output area and a pre-rendered explanation below it.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe the Schedule You Want:" column with:**
`Run the script every Monday at 5am.`
---
