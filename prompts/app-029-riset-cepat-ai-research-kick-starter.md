## Application Name
AI Rapid Research: Research Kick-starter

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that serves as a starting point for research. Users enter a research question, and AI will provide an initial summary, identify key points, and suggest keywords for further literature searches, speeding up the research process significantly.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Rapid Research".
2.  **User Input Form:**
    *   A large text area labeled "Enter Your Research Question:".
3.  **Action Buttons:** A main button with the text "Start Research". While the process is running, the button should be disabled and display the status "Searching for Information...".
4.  **Output Area:** Designed like a summary dashboard with three clear sections:
    *   **Section 1: Initial Summary:** Heading (H3) "Preliminary Summary" followed by the content area for a brief summary.
    *   **Section 2: Key Points:** Heading (H3) "Key Points" followed by a content area for the bullet list.
    *   **Section 3: Keywords for Advanced Research:** Heading (H3) "Keywords for Advanced Research" followed by the content area for the keyword list.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `###`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to all three sections in the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a research question and clicks the “Start Research” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang asisten riset AI yang terlatih untuk mensintesis informasi dan mengidentifikasi konsep-konsep inti dengan cepat.

    Berdasarkan pertanyaan riset berikut:
    """
    [Pertanyaan dari input pengguna]
    """

    Tugas Anda adalah memberikan tiga hal untuk membantu memulai proses riset:

    1.  **Ringkasan Awal:** Tulis ringkasan singkat (2-4 kalimat) yang menjawab pertanyaan secara umum dan memberikan konteks.
    2.  **Poin-Poin Kunci:** Identifikasi 3-5 poin atau sub-topik paling penting yang terkait dengan pertanyaan. Sajikan dalam bentuk daftar poin.
    3.  **Kata Kunci untuk Riset Lanjutan:** Berikan daftar kata kunci dan frasa yang bisa digunakan pengguna di database akademik (seperti Google Scholar, JSTOR) untuk menemukan literatur yang relevan.

    Gunakan format Markdown untuk seluruh respons Anda, dengan sub-judul yang jelas untuk setiap bagian.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the analysis results in three appropriate sections in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Enter Your Research Question:" column with:**
`What is the impact of social media use on teenagers' mental health?`
---
