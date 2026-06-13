## Application Name
Clean Code Namer AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a utility web application for programmers. The user describes the purpose of a variable or function in plain language, and the AI ​​will provide some descriptive name suggestions in various coding conventions (camelCase, PascalCase, snake_case, kebab-case).

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Clean Code Namer AI".
2.  **User Input Form:**
    *   A text input field labeled "Describe the Purpose of Your Variable or Function:".
3.  **Action Button:** A main button with the text "Suggest a Name". While the process is running, the button should be activated and display the status "Thinking...".
4.  **Output Area:**
    *   Title (H3): "Variable/Function Name Suggestion:"
    *   A content area that displays name suggestions in a clear table or list format, grouped by convention.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (especially tables or lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a description and clicks the "Suggest a Name" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang programmer senior yang sangat peduli dengan clean code dan konvensi penamaan yang baik.

    Berdasarkan deskripsi berikut:
    """
    [Deskripsi dari input pengguna]
    """

    Tugas Anda adalah memberikan beberapa saran nama variabel atau fungsi yang deskriptif. Sajikan saran tersebut dalam beberapa konvensi penulisan kode yang umum.

    Gunakan format tabel Markdown berikut untuk jawaban Anda:

    | Konvensi       | Saran Nama                 |
    |----------------|----------------------------|
    | camelCase      | [saran Anda]               |
    | PascalCase     | [saran Anda]               |
    | snake_case     | [saran Anda]               |
    | kebab-case     | [saran Anda]               |
    | CONSTANT_CASE  | [saran Anda]               |
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a table of formatted name suggestions in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe the Purpose of Your Variable or Function:" column with:**
`A function to retrieve user data from the database based on ID.`
---
