## Application Name
AI Generator README

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that automatically generates structured, professional README.md files for software projects. Users provide a project name, short description, and language/technology used, and AI will create a complete README template.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "README Generator AI".
2.  **User Input Form:**
    *   **Input Project Name:** A text input field labeled "Your Project Name:".
    *   **Input Description:** A text area labeled "Brief Description of Your Project:".
    *   **Technology Input:** A text input field labeled "Primary Language/Technology (separate with commas):".
3.  **Action Button:** A main button with the text "Generate README.md". While the process is running, the button should be activated and display the status "Writing Documentation...".
4.  **Output Area:**
    *   Title (H3): "Preview your README.md:"
    *   A single content area to display a preview of the rendered README.
    *   **Copy Markdown Button:** There should be a "Copy Markdown Code" button that will copy the raw Markdown text to the clipboard, ready to paste into GitHub.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI for preview. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax into properly formatted HTML elements.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the project details and clicks the "Generate README.md" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang developer senior dan kontributor open-source yang ahli dalam membuat dokumentasi proyek yang jelas dan profesional.

    Berdasarkan informasi proyek berikut:
    - Nama Proyek: [Nama dari input pengguna]
    - Deskripsi: [Deskripsi dari input pengguna]
    - Teknologi: [Teknologi dari input pengguna]

    Tugas Anda adalah membuat konten untuk file README.md yang terstruktur dengan baik. Gunakan format Markdown. Template harus mencakup bagian-bagian standar berikut:

    - Judul Proyek (H1)
    - Deskripsi Singkat
    - Fitur Utama (daftar poin)
    - Teknologi yang Digunakan (daftar poin)
    - Cara Instalasi (blok kode placeholder)
    - Cara Penggunaan (blok kode placeholder)
    - Lisensi (placeholder)

    PENTING: Respons Anda HARUS HANYA berisi teks Markdown mentah untuk file README.md dan TIDAK ADA teks atau penjelasan lain di luar itu.
    ```
3.  The application sends this prompt to the **Gemini 2.pro** model API.
4.  After receiving the response, the application saves the raw Markdown text for the "Copy" function.
5.  The application renders the Markdown content of the response into HTML and displays it in the preview area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Your Project Name:" column with:**
`TaskMaster Pro`
*   **Fill in the "Brief Description of Your Project:" field with:**
`A simple to-do list app built to help users manage their daily tasks more efficiently.`
*   **Fill in the "Primary Language/Technology (separate with commas):" column with:**
`React, Node.js, Express, MongoDB`
---
