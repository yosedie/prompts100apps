## Application Name
Creator Studio AI: YouTube Video Idea Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for YouTube creators that can produce 5 complete video concepts from one topic. For each concept, AI will provide a click-worthy title idea, a visual description for a striking thumbnail, and a draft script for the first 30 seconds of the video designed to maximize audience retention.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Studio Creator".
2.  **User Input Form:**
    *   A text input field labeled "Enter Your Video Topic:".
3.  **Action Button:** A main button with the text "Create a Video Idea!". While the process is running, the button should be disabled and display the status "Seeking Inspiration...".
4.  **Output Area:**
    *   Title (H3): "5 Video Ideas for Your Topic:"
    *   A single content area to showcase 5 video concepts.
    *   **Copy Button:** There should be a "Copy All Ideas" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a topic and clicks the "Create Video Idea!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli strategi konten YouTube dan copywriter viral yang sangat berpengalaman dalam menciptakan video yang mendapatkan engagement tinggi.

    Berdasarkan topik berikut:
    """
    [Topik dari input pengguna]
    """

    Tugas Anda adalah menghasilkan **5 konsep video YouTube yang lengkap**. Setiap konsep harus dirancang untuk memaksimalkan klik, retensi penonton, dan interaksi.

    Untuk setiap dari 5 ide, berikan tiga elemen berikut dalam format Markdown yang jelas:

    ---
    ### Ide [Nomor Ide]

    **Judul Video:** (Buat judul yang menarik, mengandung kata kunci, dan membuat penasaran).

    **Ide Thumbnail:** (Jelaskan secara visual apa yang harus ada di thumbnail: gambar utama, ekspresi wajah, teks singkat yang mencolok, warna kontras).

    **Skrip Pembuka (30 detik pertama):** (Tulis draf narasi untuk 30 detik pertama yang langsung mengait penonton, menjanjikan nilai, dan membuat mereka ingin menonton sampai akhir).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 5 formatted video concepts in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Your Video Topic:" column with:**
`How to learn a new language quickly`
---
