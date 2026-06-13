## Application Name
AI Writer's Block Breaker: Plot Unsticker

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that serves as a brainstorming companion for writers. Users describe a scene or plot point where they feel stuck, and the AI ​​will make three different and unexpected suggestions about how the story could progress.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Writer's Block Breaker".
2.  **User Input Form:**
    *   A large textarea labeled "Explain where you feel stuck in your story:".
3.  **Action Button:** A main button with the text "Give Me Ideas!". While the process is running, the button should be activated and display the status "Brainstorming...".
4.  **Output Area:**
    *   Title (H3): "3 Ideas to Continue the Story:"
    *   A single content area to showcase 3 ideas. Each idea must be clearly separated.
    *   **Copy Button:** There should be a "Copy All" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##` and `---`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users enter a description of their deadlock and click the "Give Me Ideas!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang editor cerita (story editor) dan penulis kreatif yang sangat imajinatif. Anda ahli dalam menemukan solusi tak terduga untuk masalah plot.

    Berikut adalah deskripsi kebuntuan (writer's block) dari seorang penulis:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah memberikan **3 saran yang sangat berbeda** tentang bagaimana cerita bisa berlanjut dari titik ini. Setiap saran harus:
    - Menawarkan arah yang unik (misalnya, satu saran bisa berupa aksi, satu berupa pengungkapan karakter, satu berupa plot twist).
    - Cukup detail untuk memicu imajinasi penulis.
    - Dirancang untuk memecahkan kebuntuan dan membuka kemungkinan baru.

    Gunakan format Markdown untuk memisahkan setiap saran dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 3 ideas in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Describe where you got stuck in your story:" column with:**
`My protagonist, a detective, finally manages to corner the main villain on the roof of the building. They both pointed guns at each other. I don't know how to end this scene without it feeling cliche.`
---
