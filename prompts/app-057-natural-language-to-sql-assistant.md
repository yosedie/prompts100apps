## Application Name
Natural Language to SQL Assistant

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a human language translator to SQL queries. Users write data queries in plain sentences and describe their table schema, and then AI generates appropriate SQL queries.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large header says "SQL Assistant".
2.  **User Input Form:**
    *   **Request Input:** A text input field labeled "Request Your Data (in plain language):".
    *   **Input Table Schema:** A text area labeled "Describe Your Table Schema:". Provide a placeholder like "Example: The 'users' table has columns id (INT), name (VARCHAR), email (VARCHAR), registration_date (DATETIME)."
3.  **Action Button:** A main button with the text "Generate SQL Query". While the process is running, the button should be activated and display the status "Querying...".
4.  **Output Area (Code Block):**
    *   Title (H3): "Generated SQL Query:"
    *   A special **code block container** (such as `<pre><code>...</code></pre>`) for displaying SQL queries. This container should have a dark background and use a monospaced font.
    *   **Copy Code Button:** In the top right corner of the code block container, **required** there is a "Copy" button that allows the user to copy the entire query to the clipboard with one click.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Code Blocks with Syntax Highlighting:** The application **must** use a JavaScript library such as `highlight.js` or `prism.js` to render the response from the AI. This library will automatically detect the SQL language from the Markdown fence (```sql) and provide appropriate syntax coloring within the code block container.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the query and schema, then clicks the "Generate SQL Query" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang Data Analyst dan ahli SQL senior. Tugas Anda adalah menerjemahkan permintaan data dalam bahasa manusia menjadi query SQL yang bersih dan efisien.

    Berdasarkan informasi berikut:
    - Permintaan Data: """[Permintaan dari input pengguna]"""
    - Skema Tabel: """[Skema dari input pengguna]"""

    Tulis query SQL yang sesuai untuk mendapatkan data yang diminta. Asumsikan dialek SQL standar.

    PENTING: Respons Anda HARUS HANYA berisi blok kode SQL mentah dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response (which contains only a block of SQL code), the application uses the syntax highlighting library to render it into a beautifully formatted code block in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Request Your Data (in plain language):" column with:**
`Show the names and emails of all users who registered last month and sort by most recent registration date.`
*   **Fill in the "Describe Your Table Schema:" field with:**
`The 'users' table has columns id (INT), name (VARCHAR), email (VARCHAR), registration_date (DATETIME).`
---
