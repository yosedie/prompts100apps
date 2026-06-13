## Application Name
AI Protest Letter Writer: Complaint Letter Assistant

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users compose formal and effective complaint or protest letters. Users describe the problem they are facing and the desired solution, then the AI ​​will draft a letter that is clear, firm, but still polite.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Protest Letter Writer".
2.  **User Input Form:**
    *   **Input Company Name:** A text input field with the label "Name of the Company/Institution Destined:".
    *   **Input Problem:** A text area labeled "Describe Your Problem in Detail:".
    *   **Solution Input:** A text area with the label "What is the Solution or Result You Want?".
3.  **Action Button:** A main button with the text "Compose a Protest Letter". While the process is running, the button should be activated and display the status "Compiling...".
4.  **Output Area:**
    *   Title (H3): "Draft Your Protest Letter:"
    *   A single content area to display the entire letter.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the complaint details and clicks on the "Compose Protest Letter" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis surat bisnis profesional dan advokat konsumen. Anda ahli dalam menyusun komunikasi yang jelas, formal, dan persuasif.

    Berdasarkan informasi keluhan berikut:
    - Perusahaan yang Dituju: [Nama dari input pengguna]
    - Deskripsi Masalah: """[Masalah dari input pengguna]"""
    - Solusi yang Diinginkan: """[Solusi dari input pengguna]"""

    Tugas Anda adalah menulis draf surat keluhan atau protes yang formal. Surat harus:
    - Memiliki struktur yang jelas: pembukaan (menyatakan tujuan surat), isi (merinci masalah secara kronologis dan faktual), dan penutup (menyatakan solusi yang diinginkan dan batas waktu untuk tanggapan).
    - Menggunakan nada yang tegas dan serius, namun tetap sopan dan profesional.
    - Menghindari bahasa yang emosional atau menuduh.

    Gunakan placeholder seperti `[Nama Anda]` dan `[Tanggal]` agar mudah disesuaikan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the draft letter in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "Name of the Company/Institution Addressed:" with:**
`SuperNet ISP`
*   **Fill in the "Describe Your Problem in Detail:" field with:**
`My internet connection with customer number 12345 has been completely lost for the last 3 days, since September 15 2025. I have called customer service 5 times and each time they were only promised that it would be repaired immediately without any certainty of time.`
*   **Fill in the column "What Solution or Result Do You Want?" with:**
`I demand a technician to come and fix the problem within the next 24 hours. Additionally, I request compensation in the form of a bill reduction for the days I did not receive service.`
---
