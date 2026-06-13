## Application Name
BioCraft AI: Professional Bio Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps professionals write engaging bios for LinkedIn profiles, portfolios, or personal websites. Users enter their roles, skills, and accomplishments in the form of points, and AI will organize them into a short, impactful narrative bio.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "BioCraft AI".
2.  **User Input Form:**
    *   **Input Role/Job:** A text input field labeled "Your Current Role/Job:".
    *   **Input Skills:** A text area labeled "Your Key Skills (separate with commas):".
    *   **Input Achievements:** A text area labeled "Your Important Achievements (one per line):".
3.  **Action Button:** A main button with the text "Create a Professional Bio". While the process is running, the button should be activated and display the status "Stringing Words...".
4.  **Output Area:**
    *   Title (H3): "Your Professional Bio:"
    *   A single content area to display the generated bio.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##` and `**`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in their professional details and click on the “Create Professional Bio” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang copywriter ahli dan konsultan personal branding yang berspesialisasi dalam menulis bio profesional.

    Berdasarkan poin-poin berikut:
    - Peran/Jabatan: [Peran dari input pengguna]
    - Keahlian Utama: [Keahlian dari input pengguna]
    - Pencapaian Penting: [Pencapaian dari input pengguna]

    Tugas Anda adalah mengubah poin-poin ini menjadi sebuah bio naratif yang singkat (sekitar 3-4 kalimat), profesional, dan menarik. Bio ini harus menonjolkan nilai dan dampak dari individu tersebut.

    Untuk memberikan pilihan kepada pengguna, buat **DUA versi bio**:
    1.  **Versi Sudut Pandang Orang Pertama (Saya adalah...)**
    2.  **Versi Sudut Pandang Orang Ketiga ([Nama Jabatan] adalah...)**

    Gunakan format Markdown untuk memisahkan kedua versi dengan jelas menggunakan sub-judul.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays both formatted versions of the bio in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Your Current Role/Position:" column with:**
`Digital Marketing Manager`
*   **Fill in the "Your Main Skills (separate with commas):" column with:**
`SEO, SEM, Content Strategy, Google Analytics, Email Marketing`
*   **Fill in the "Your Important Achievements (one per row):" column with:**
`- Increase organic website traffic by 150% in one year.
    - Managed digital advertising campaigns with budgets over $50,000.
    - Led a content team that won the 'Best Content Marketing 2023' award.`
---
