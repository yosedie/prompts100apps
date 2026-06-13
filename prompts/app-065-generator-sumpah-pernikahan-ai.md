## Application Name
AI Wedding Vow Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users write personal and touching wedding vows. Users enter several memories, likes, and promises for their partner, and then the AI ​​will assemble them into a beautiful and poetic script.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Wedding Vow Generator".
2.  **User Input Form:**
    *   **Input Memories:** A text area labeled "Tell me about one favorite memory with your partner:".
    *   **Input Traits:** A text area with the label "Name 3 traits you love most about him:".
    *   **Promise Input:** A text area labeled "What is the main promise you want to make for the future?".
3.  **Action Button:** A main button with the text "Write Wedding Vows". While the process is running, the button should be activated and display the status "Composing Words of Love...".
4.  **Output Area:**
    *   Title (H3): "Draft Your Wedding Vows:"
    *   A single content area to display the entire manuscript.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in details of memories, traits, and vows, then click the "Write Wedding Vows" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis pidato dan penyair yang sangat romantis dan empatik. Anda ahli dalam merangkai cerita personal menjadi kata-kata yang menyentuh hati.

    Berdasarkan poin-poin personal berikut:
    - Kenangan Favorit: """[Teks dari input kenangan]"""
    - Sifat yang Dicintai: """[Teks dari input sifat]"""
    - Janji untuk Masa Depan: """[Teks dari input janji]"""

    Tugas Anda adalah menulis sebuah draf sumpah pernikahan yang indah dan personal. Naskah harus:
    - Dimulai dengan menyapa pasangan.
    - Mengintegrasikan kenangan favorit yang diberikan secara naratif.
    - Memuji sifat-sifat yang dicintai.
    - Diakhiri dengan janji untuk masa depan.
    - Menggunakan bahasa yang tulus, romantis, dan puitis.

    Gunakan placeholder `[Nama Pasangan]` agar mudah disesuaikan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the draft wedding vows in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Tell me about one favorite memory with your partner:" column with:**
`I will never forget the first time we got caught in the rain on the way home and we ended up laughing while dancing in the rain.`
*   **Fill in the "Name 3 qualities you love most about him" column with:**
`His infectious laugh, his kindness to everyone, and the way he made me feel calm when I was panicking.`
*   **Fill in the column "What is the main promise you want to make for the future?" with:**
`I promise to always be your partner in your adventures and the most comfortable place to come home to.`
---
