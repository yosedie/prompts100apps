## Application Name
AI Recruiter: Job Description Writer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that automatically generates complete and engaging job descriptions. Users only need to enter the position name and three key responsibilities, and AI will compile the rest, including a summary of the position, required qualifications, and what the company offers.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Recruiter".
2.  **User Input Form:**
    *   **Input Position Name:** A text input field labeled "Position Name:".
    *   **Input Responsibilities:** Three separate text input fields:
        *   "Primary Responsibilities 1:"
        *   "Main Responsibility 2:"
        *   "Main Responsibility 3:"
3.  **Action Button:** A main button with the text "Create Job Description". While the process is running, the button should be disabled and display the status "Compiling...".
4.  **Output Area:**
    *   Title (H3): "Job Vacancy Description:"
    *   A single content area to display all generated descriptions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in the position name and three responsibilities, then click the "Create Job Description" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang Manajer Perekrutan (Hiring Manager) dan copywriter ahli yang berspesialisasi dalam membuat deskripsi lowongan kerja yang menarik bagi talenta terbaik.

    Berdasarkan informasi singkat berikut:
    - Nama Posisi: [Nama Posisi dari input pengguna]
    - Tanggung Jawab Utama 1: [Teks dari input 1]
    - Tanggung Jawab Utama 2: [Teks dari input 2]
    - Tanggung Jawab Utama 3: [Teks dari input 3]

    Tugas Anda adalah mengubah informasi singkat ini menjadi deskripsi lowongan kerja yang lengkap, profesional, dan menarik. Deskripsi harus mencakup bagian-bagian berikut:
    - Ringkasan Posisi
    - Tanggung Jawab Utama (gunakan 3 poin yang diberikan)
    - Kualifikasi yang Dibutuhkan (simpulkan kualifikasi teknis dan non-teknis yang paling relevan dari nama posisi dan tanggung jawab)
    - Kualifikasi Tambahan (Nilai Plus)
    - Apa yang Kami Tawarkan (buat daftar penawaran standar yang menarik seperti gaji kompetitif, lingkungan kerja kolaboratif, dll.)

    Gunakan format Markdown untuk kejelasan, termasuk judul, sub-judul, dan daftar poin.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted job description in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Position Name:" column with:**
`Senior Frontend Developer`
*   **Fill in the "Main Responsibility 1:" column with:**
`Develop and maintain the user interface (UI) of our web applications.`
*   **Fill in the "Main Responsibility 2:" column with:**
`Collaborate with backend teams and UI/UX designers.`
*   **Fill in the "Main Responsibility 3:" column with:**
`Optimizes applications for maximum speed and scalability.`
---
