## Application Name
JSON Data Factory AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a sample data generator (dummy data) in JSON format. Users describe the data schema they need in plain language, and AI will generate an array of appropriate JSON objects, very useful for prototyping and testing.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "JSON Data Factory AI".
2.  **User Input Form:**
    *   **Input Schema Description:** A large text area labeled "Describe the Data Schema You Need:".
    *   **Input Number of Objects:** A number input field (type="number") with the label "Desired Number of Data Objects:" and a default value of 5.
3.  **Action Button:** A main button with the text "Generate JSON Data". While the process is running, the button should be activated and display the status "Generating...".
4.  **Output Area (Code Block):**
    *   Title (H3): "Generated JSON Data:"
    *   A special **code block container** (such as `<pre><code>...</code></pre>`) for displaying JSON data. This container should have a dark background and use a monospaced font.
    *   **Copy Code Button:** In the top right corner of the code block container, **required** there is a "Copy" button that allows users to copy the entire JSON data to the clipboard with one click.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Code Blocks with Syntax Highlighting:** The application **must** use a JavaScript library such as `highlight.js` or `prism.js` to render the response from the AI. This library will automatically detect the JSON format of Markdown fence (```json) and provide appropriate syntax coloring within the code block container.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a schema description, number of objects, and clicks the "Generate JSON Data" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah sebuah API data generator. Tugas Anda adalah membuat data sampel dalam format JSON berdasarkan deskripsi skema dari pengguna.

    Berdasarkan permintaan berikut:
    - Deskripsi Skema: """[Teks dari input pengguna]"""
    - Jumlah Objek: [Jumlah dari input pengguna]

    Buat sebuah array JSON yang berisi [Jumlah dari input pengguna] objek. Setiap objek harus sesuai dengan skema yang dideskripsikan. Gunakan data acak yang realistis (nama, email, tanggal, dll.).

    PENTING: Respons Anda HARUS HANYA berisi blok kode JSON mentah yang valid dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response (which contains only a JSON code block), the application uses the syntax highlighting library to render it into a beautifully formatted code block in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe the Data Schema You Need:" column with:**
`I need user data. Each user must have:
    - id (unique number)
    - name (random full name)
    - email (random email address)
    - join_date (random date in the last year)`
*   **Set "Desired Number of Data Objects:" to:**
`5`
---
