## Application Name
AI Bottle Message Author: Message in a Bottle Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a creative web application that writes short, mysterious and thoughtful letters. Users enter a theme or feeling, and the AI ​​will write a message as if it were put in a bottle and floated out to sea for future strangers to discover.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Bottle Message Author".
2.  **User Input Form:**
    *   A text input field labeled "What is the Feeling or Theme of Your Message?".
3.  **Action Button:** A main button with the text "Compose Message". While the process is running, the button should be activated and display the status "Driving into the Sea...".
4.  **Output Area:**
    *   Title (H3): "Message in a Bottle:"
    *   A single content area to display the entire message.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the theme and clicks the "Compose Message" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penyair, filsuf, dan pengelana waktu yang sendirian. Anda menulis pesan-pesan singkat untuk dimasukkan ke dalam botol dan dilempar ke lautan waktu.

    Berdasarkan tema berikut:
    """
    [Tema dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah surat pendek yang misterius dan penuh perenungan. Surat ini ditujukan kepada 'Wahai Penemu', orang asing yang akan menemukannya di masa depan.

    Surat harus:
    - Singkat dan puitis.
    - Merenungkan tema yang diberikan dari sudut pandang yang tak lekang oleh waktu.
    - Berakhir dengan sebuah pertanyaan terbuka atau pernyataan yang menggugah pikiran.

    Gunakan format Markdown untuk penekanan jika diperlukan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted message in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What is the Feeling or Theme of Your Message?" with:**
`Hope`
---
