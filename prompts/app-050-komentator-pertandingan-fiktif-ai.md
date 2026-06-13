## Application Name
AI Fictitious Match Commentator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an entertainment web application that writes exciting play-by-play commentary narratives for completely fictional sports games. Users enter the name of a strange sport, and the AI ​​will generate a dramatic and passionate commentary script as if it were broadcasting the peak moments of the game.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Fictitious Match Commentator".
2.  **User Input Form:**
    *   A text input field labeled "Name of Fictitious Sport to Comment on:".
3.  **Action Button:** A main button with the text "Start Commenting!". While the process is running, the button should be disabled and display the status "Setting up Microphone...".
4.  **Output Area:**
    *   Title (H3): "Play-by-Play Commentary:"
    *   A single content area to display the entire narrative.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the name of the sport and clicks the "Start Commenting!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang komentator olahraga legendaris dengan energi tinggi. Anda mampu membuat pertandingan paling aneh sekalipun terdengar seru, dramatis, dan menegangkan.

    Berdasarkan nama olahraga fiktif berikut:
    """
    [Nama olahraga dari input pengguna]
    """

    Tugas Anda adalah menulis naskah komentar play-by-play yang seru untuk momen-momen puncak dari pertandingan final olahraga ini. Naskah harus:
    - Menciptakan nama-nama atlet fiktif.
    - Menggambarkan aksi dengan detail yang hidup.
    - Membangun ketegangan hingga mencapai klimaks.
    - Menggunakan frasa-frasa khas komentator olahraga ("Luar biasa!", "Tidak bisa dipercaya!", "Sejarah tercipta hari ini!").

    Gunakan format Markdown untuk penekanan pada momen-momen dramatis.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted comment narrative in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Name of the Fictitious Sport to be Commented on:" column with:**
`Extreme Snail Racing World Championship Final`
---
