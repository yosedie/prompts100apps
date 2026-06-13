## Application Name
AI Ornamental Plant Assistant: Plant Care Guide

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a virtual 'plant doctor'. Users enter the name of their houseplant, and AI will provide a complete, easy-to-follow care guide, covering watering frequency, light requirements, and how to deal with common pests.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Houseplant Assistant".
2.  **User Input Form:**
    *   A text input field labeled "Enter the Name of Your Houseplant:".
3.  **Action Button:** A main button with the text "Search for Maintenance Guide". While the process is running, the button should be activated and display the status "Seeking Guide...".
4.  **Output Area:**
    *   Title (H3): "Complete Care Guide:"
    *   A single content area to display the entire guide.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters the name of the plant and clicks the "Search Care Guide" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli hortikultura dan 'dokter tanaman' yang berpengalaman. Anda mampu memberikan saran perawatan yang jelas dan mudah diikuti bahkan untuk pemula.

    Berdasarkan nama tanaman berikut:
    """
    [Nama tanaman dari input pengguna]
    """

    Tugas Anda adalah memberikan panduan perawatan yang lengkap. Panduan harus mencakup bagian-bagian berikut:

    - **Penyiraman (Watering):** Jelaskan seberapa sering harus disiram dan bagaimana cara terbaik untuk mengecek kelembapan tanah.
    - **Kebutuhan Cahaya (Light Needs):** Jelaskan jenis pencahayaan yang ideal (cahaya terang tidak langsung, cahaya rendah, dll.).
    - **Kelembapan & Suhu (Humidity & Temperature):** Berikan saran tentang tingkat kelembapan dan suhu ruangan yang disukai.
    - **Hama Umum & Cara Mengatasi (Common Pests & Solutions):** Sebutkan 2-3 hama yang sering menyerang tanaman ini dan berikan solusi sederhana untuk mengatasinya.

    Gunakan format Markdown untuk menyusun panduan dengan rapi (judul, sub-judul, daftar poin).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a pre-formatted maintenance guide in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter the Name of Your Ornamental Plant:" column with:**
`Monstera Deliciosa`
---
