## Application Name
Code Commenter AI: Docstring Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that automatically documents code. Users paste a code function, and AI will analyze it to write a clear comment or docstring, explaining the function's purpose, input parameters, and output values.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Code Commenter AI".
2.  **User Input Form:**
    *   A large text area labeled "Paste Your Code Function Here:". This text area must use monospaced font.
    *   **Comment Style Selection:** A dropdown (select) menu with the label "Select Comment Style:" and options: "Docstring (Python)", "JSDoc (JavaScript)".
3.  **Action Button:** A main button with the text "Generate Comment". While the process is running, the button should be activated and display the status "Analyzing Code...".
4.  **Output Area (Code Block):**
    *   Title (H3): "Code with Comments:"
    *   A special **code block container** (such as `<pre><code>...</code></pre>`) to display code with comments added. This container should have a dark background and use a monospaced font.
    *   **Copy Code Button:** In the top right corner of the code block container, **required** there is a "Copy" button that allows the user to copy the entire code to the clipboard with one click.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Code Blocks with Syntax Highlighting:** The application **must** use a JavaScript library such as `highlight.js` or `prism.js` to render the response from the AI. This library will automatically detect the language and provide appropriate syntax coloring within the code block container.

## Workflow & Logic (Workflow & Logic)

1.  The user pastes the code, chooses a style, and clicks the "Generate Comment" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang programmer senior yang sangat disiplin dalam menulis kode yang bersih dan terdokumentasi dengan baik.

    Berdasarkan fungsi kode berikut:
    ```
[Code from user input]
    ```

    Tugas Anda adalah menganalisis fungsi ini dan menulis komentar dokumentasi (docstring/JSDoc) yang sesuai dengan gaya "[Gaya dari pilihan pengguna]".

    Komentar harus mencakup:
    1.  Deskripsi singkat tentang apa yang dilakukan fungsi tersebut.
    2.  Penjelasan untuk setiap parameter (Args/Params).
    3.  Penjelasan tentang apa yang dikembalikan oleh fungsi (Returns).

    PENTING: Respons Anda HARUS HANYA berisi blok kode mentah yang sudah digabungkan dengan komentar barunya, dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response (which only contains a code block), the application uses the syntax highlighting library to render it into a beautifully formatted code block in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Paste Your Code Function Here:" field with:**
    ```python
    def calculate_area(length, width):
        if length < 0 or width < 0:
            return None
        area = length * width
        return area
    ```
*   **Set the "Choose Comment Style:" option to:**
`Docstring (Python)`
---
