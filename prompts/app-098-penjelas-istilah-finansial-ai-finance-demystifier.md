## Application Name
AI Financial Terms Explainer: Finance Demystifier

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a simplified financial dictionary. Users enter complex investment or financial terms, and AI will explain them using simple analogies and language that is easy for beginners to understand.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Financial Terms Explainer".
2.  **User Input Form:**
    *   A text input field labeled "Enter a Complex Financial Term:".
3.  **Action Button:** A main button with the text "Explain Simply!". While the process is running, the button should be activated and display the status "Simplifying...".
4.  **Output Area:**
    *   Title (H3): "Simple Explanation:"
    *   A single content area to display all explanations.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a financial term and clicks the "Explain Simply!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penasihat keuangan dan edukator yang sangat pandai menyederhanakan konsep-konsep rumit. Anda sering menggunakan analogi untuk mengajar.

    Berdasarkan istilah keuangan berikut:
    """
    [Istilah dari input pengguna]
    """

    Tugas Anda adalah menjelaskan istilah ini kepada seorang pemula absolut. Penjelasan Anda harus:
    1.  Dimulai dengan sebuah **analogi sederhana** yang mudah dipahami (misalnya, membandingkannya dengan membeli sekeranjang buah, bukan satu buah saja).
    2.  Menjelaskan **apa itu** dan **bagaimana cara kerjanya** dalam bahasa yang sangat sederhana.
    3.  Menyebutkan **satu keuntungan utama** dari hal tersebut.

    Hindari jargon teknis sebisa mungkin. Gunakan format Markdown untuk penekanan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays an explanation in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Insert a Complicated Financial Term:" field with:**
`Index Mutual Funds`
---
