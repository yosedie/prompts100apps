## Application Name
Blurb Crafter AI: Book Blurb Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for authors that automatically creates attractive blurbs (book back cover text). Users enter a brief synopsis of their story, and the AI ​​will write a choice of 3 blurbs that are suspenseful, intriguing, and designed to make readers want to buy the book.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Blurb Crafter AI".
2.  **User Input Form:**
    *   A large text area labeled "Paste a Short Synopsis of Your Story:".
3.  **Action Button:** A main button with the text "Create Blurb!". While the process is running, the button should be activated and display the status "Writing...".
4.  **Output Area:**
    *   Title (H3): "3 Blurb Options for Your Book:"
    *   A single content area to display 3 blurb options. Each option must be clearly separated.
    *   **Copy Button:** Each blurb selection should have an individual "Copy" button next to it.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `---` or `**`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a synopsis and clicks the "Create Blurb!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang editor akuisisi di sebuah penerbit besar dan seorang copywriter ahli. Anda tahu persis bagaimana cara menulis blurb yang menjual buku.

    Berdasarkan sinopsis cerita berikut:
    """
    [Sinopsis dari input pengguna]
    """

    Tugas Anda adalah menulis **3 pilihan blurb yang berbeda**. Setiap blurb harus:
    - Memperkenalkan protagonis dan konflik utama.
    - Membangun ketegangan dan misteri.
    - TIDAK membocorkan akhir cerita.
    - Berakhir dengan sebuah 'hook' atau pertanyaan yang membuat pembaca sangat penasaran.

    Gunakan format Markdown untuk memisahkan setiap pilihan blurb dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 3 blurb options in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste a Short Synopsis of Your Story:" column with:**
`An ancient linguist named Dr. Aris finds an artifact containing a map to the mythical city of Atlantis. However, a secret organization known as 'The Order' also wants the map to gain control of Atlantis' ancient technology. Aris must solve a map puzzle while escaping from the pursuit of deadly agents of The Order.`
---
