## Application Name
AI Image Prompt Enhancer: Prompt Enhancer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users write better prompts for AI image generators (like Midjourney or Stable Diffusion). Users enter a simple prompt idea, and the AI ​​will develop it into a highly detailed prompt, adding elements such as art style, lighting, composition, and other technical details.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Image Prompt Enhancer".
2.  **User Input Form:**
    *   A text input field labeled "Enter Your Simple Prompt Idea:".
3.  **Action Button:** A main button with the text "Upgrade Prompt!". While the process is running, the button should be activated and display the status "Adding Details...".
4.  **Output Area:**
    *   Title (H3): "Improved Prompt:"
    *   A single content area to display detailed prompts.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a simple prompt and clicks the "Improve Prompt!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang 'prompt engineer' dan seniman digital yang sangat ahli. Anda tahu persis kata kunci apa yang harus digunakan untuk mendapatkan hasil terbaik dari model generator gambar AI.

    Berdasarkan ide prompt sederhana berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menulis ulang prompt ini menjadi versi yang sangat detail dan kaya. Tambahkan elemen-elemen berikut untuk memperkaya prompt:
    - **Subjek & Aksi:** Deskripsikan subjek dan apa yang dilakukannya dengan lebih detail.
    - **Gaya Seni (Art Style):** Sebutkan gaya seni yang spesifik (misal: 'digital painting', 'cyberpunk', 'fantasy concept art').
    - **Pencahayaan (Lighting):** Deskripsikan pencahayaan (misal: 'cinematic lighting', 'soft volumetric light', 'neon glow').
    - **Komposisi & Detail:** Tambahkan detail tentang lingkungan, warna, dan komposisi gambar.
    - **Parameter Teknis:** Akhiri dengan beberapa parameter teknis yang umum digunakan (misal: `--ar 16:9 --v 6.0`).

    PENTING: Gabungkan semua elemen ini menjadi satu paragraf teks yang siap disalin, bukan dalam bentuk daftar.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays improved prompts in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Your Simple Prompt Idea:" column with:**
`astronaut in the jungle`
---
