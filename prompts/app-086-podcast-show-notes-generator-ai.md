## Application Name
Podcast Show Notes Generator AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps podcasters create interesting episode descriptions (show notes). Users enter key points or a brief summary of their episode, and the AI ​​will write a comprehensive description and come up with some compelling title suggestions.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Podcast Show Notes Generator AI".
2.  **User Input Form:**
    *   A large text area labeled "Enter Key Points or Summary of Your Episode:".
3.  **Action Button:** A main button with the text "Create Episode Description". While the process is running, the button should be activated and display the status "Mixing Audio...".
4.  **Output Area:**
    *   Title (H3): "Your Episode Description & Title:"
    *   A single content area to display all results.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the episode bullet points and clicks the “Create Episode Description” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang produser podcast dan copywriter yang ahli dalam membuat deskripsi episode yang membuat orang ingin langsung mendengarkan.

    Berdasarkan poin-poin kunci berikut dari sebuah episode podcast:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menghasilkan DUA hal:

    1.  **Usulan Judul Episode:** Berikan 3 opsi judul yang menarik, memancing rasa penasaran, dan mengandung kata kunci utama.
    2.  **Deskripsi Episode (Show Notes):** Tulis deskripsi yang menarik. Mulailah dengan sebuah 'hook' atau pertanyaan, jelaskan secara singkat apa saja yang akan dibahas (berdasarkan poin-poin yang diberikan), dan akhiri dengan ajakan untuk mendengarkan.

    Gunakan format Markdown untuk menyusun hasilnya dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the proposed title and description in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Enter Key Points or Summary of Your Episode:" field with:**
`- Interview with Dr. Anya, a psychologist.
    - Discusses the phenomenon of 'burnout' among young workers.
    - The early signs of burnout are often ignored.
    - Three practical strategies to prevent and overcome burnout.`
---
