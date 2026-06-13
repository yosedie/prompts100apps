## Application Name
Test Case Generator AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for software testers and developers. Users describe an application feature, and AI will automatically create a comprehensive list of test cases, including normal scenarios (happy path), negative scenarios, and edge cases.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Test Case Generator AI".
2.  **User Input Form:**
    *   A large text area labeled "Describe the Application Feature to be Tested:".
3.  **Action Button:** A main button with the text "Create Test Case". While the process is running, the button should be activated and display the status "Analyzing Features...".
4.  **Output Area:**
    *   Title (H3): "List of Test Cases:"
    *   A single content area to display the entire list.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a feature description and clicks the “Create Test Case” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang Quality Assurance (QA) Engineer senior yang sangat teliti dan ahli dalam merancang kasus uji (test cases).

    Berdasarkan deskripsi fitur aplikasi berikut:
    """
    [Deskripsi fitur dari input pengguna]
    """

    Tugas Anda adalah membuat daftar kasus uji yang komprehensif. Kelompokkan kasus uji ke dalam tiga kategori:

    1.  **Skenario Normal (Happy Path):** Uji coba untuk alur kerja yang diharapkan dan berhasil.
    2.  **Skenario Negatif:** Uji coba untuk input yang salah atau tindakan pengguna yang tidak valid.
    3.  **Kasus Tepi (Edge Cases):** Uji coba untuk kondisi-kondisi ekstrem atau yang jarang terjadi.

    Sajikan hasilnya dalam format Markdown, menggunakan sub-judul untuk setiap kategori dan daftar poin untuk setiap kasus uji.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted list of test cases in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Describe the Application Features to be Tested:" column with:**
`A login page with input fields for email and password, as well as a "Login" button. The email must be in a valid format. Password must be at least 8 characters.`
---
