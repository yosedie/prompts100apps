## Application Name
Code Weaver AI: Pseudocode Translator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a translator from human language logic or pseudocode into functional programming code. Users write their logic flow, select the target language, and AI will generate ready-to-use code.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Code Weaver AI".
2.  **User Input Form:**
    *   A large text area labeled "Write Your Logic or Pseudocode Here:".
    *   **Target Language Selection:** A dropdown (select) menu with the label "Translate to Language:" and options: "Python", "JavaScript".
3.  **Action Buttons:** A main button with the text "Translate to Code". While the process is running, the button should be activated and display the status "Weaving Code...".
4.  **Output Area (Code Block):**
    *   Title (H3): "Generated Code:"
    *   A special **code block container** (such as `<pre><code>...</code></pre>`) to display the generated code. This container should have a dark background and use a monospaced font.
    *   **Copy Code Button:** In the top right corner of the code block container, **required** there is a "Copy" button that allows the user to copy the entire code to the clipboard with one click.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Code Blocks with Syntax Highlighting:** The application **must** use a JavaScript library such as `highlight.js` or `prism.js` to render the response from the AI. This library will automatically detect the language (Python/JavaScript) of the Markdown fence (```python) and provide appropriate syntax coloring within the code block container.

## Workflow & Logic (Workflow & Logic)

1.  The user enters pseudocode, selects a language, and clicks the "Translate to Code" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang programmer ahli dan code generator. Tugas Anda adalah menerjemahkan pseudocode atau logika bahasa manusia menjadi kode yang bersih dan fungsional.

    Berdasarkan permintaan berikut:
    - Pseudocode: """[Teks dari input pengguna]"""
    - Bahasa Target: [Bahasa dari pilihan pengguna]

    Terjemahkan pseudocode tersebut ke dalam bahasa [Bahasa dari pilihan pengguna].

    PENTING: Respons Anda HARUS HANYA berisi blok kode Markdown mentah untuk bahasa yang diminta dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response (which only contains a code block), the application uses the syntax highlighting library to render it into a beautifully formatted code block in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Write Your Logic or Pseudocode Here:" field with:**
`Create a function called 'greet'.
This function accepts one parameter: 'name'.
Inside the function, print the sentence "Hello, [name]! Welcome."`
*   **Set the "Translate to Language:" option to:**
`Python`
---
