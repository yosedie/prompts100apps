## Application Name
Pro AI Cover Letter: Cover Letter Writer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that automatically creates a personalized cover letter. Users paste in their job description and CV, then the AI ​​will write a draft cover letter highlighting the most relevant experience from the CV for the intended position.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Pro AI Cover Letter".
2.  **User Input Form:**
    *   **Input Job Description:** A text area labeled "Paste Job Description Here:".
    *   **Input CV:** A large text area labeled "Paste Your CV or Experience Summary Here:".
3.  **Action Button:** A main button with the text "Create Cover Letter". While the process is running, the button should be activated and display the status "Writing...".
4.  **Output Area:**
    *   Title (H3): "Draft Your Cover Letter:"
    *   A single content area to display the entire letter.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users paste in the job description and CV, then click the "Create Cover Letter" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang konsultan karir dan penulis profesional yang ahli dalam membuat surat lamaran kerja yang persuasif.

    Berdasarkan dua dokumen berikut:
    1.  Deskripsi Pekerjaan: """[Teks dari input deskripsi pekerjaan]"""
    2.  CV Pelamar: """[Teks dari input CV]"""

    Tugas Anda adalah menulis draf surat lamaran kerja yang kuat dan dipersonalisasi. Surat lamaran harus:
    - Ditujukan untuk posisi yang spesifik dalam deskripsi pekerjaan.
    - Menyoroti 2-3 pengalaman atau keahlian paling relevan dari CV yang cocok dengan persyaratan di deskripsi pekerjaan.
    - Menggunakan bahasa yang profesional dan antusias.
    - Memiliki struktur standar: paragraf pembuka, paragraf isi yang menyoroti kecocokan, dan paragraf penutup dengan call-to-action.

    Gunakan placeholder seperti `[Nama Anda]` atau `[Nama Manajer Perekrutan]` jika informasi tersebut tidak tersedia.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the draft cover letter in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Paste Job Description Here:" field with:**
`Wanted: Social Media Manager. Responsibilities include managing all company social media accounts, creating a content calendar, and analyzing engagement metrics. Must have at least 2 years of experience in managing social media campaigns and familiarity with analytical tools such as Hootsuite.`
*   **Fill in the "Paste your CV or Summary of Experience Here:" column with:**
`Budi Santoso - Digital Marketing Specialist

Experience:
    - Social Media Specialist at PT. Maju Jaya (2021-Present)
      - Manage Instagram & TikTok accounts, increase followers by 50%.
      - Create and schedule daily content using Hootsuite.
      - Reporting monthly campaign performance.
    - Marketing Intern at a Creative Agency (2020)
      - Assist with content research and copywriting.

Skills: Copywriting, Hootsuite, Data Analysis, Basic SEO.`
---
