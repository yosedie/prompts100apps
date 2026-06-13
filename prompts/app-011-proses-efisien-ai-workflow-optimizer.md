## Application Name
AI Efficient Processes: Workflow Optimizer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an analytical web application that functions as a process efficiency consultant. Users describe an existing workflow, and AI will analyze it to identify bottlenecks and provide concrete suggestions for improving efficiency.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Efficient Process".
2.  **User Input Form:**
    *   A large text area labeled "Describe Your Current Workflow in Detail:".
3.  **Action Button:** A main button with the text "Analyze & Give Suggestions". While the process is running, the button should be disabled and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Process Improvement Suggestions:"
    *   A single content area to display a list of suggestions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `1.`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a workflow description and clicks the "Analyze & Give Suggestions" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang konsultan efisiensi proses bisnis (Business Process Efficiency Consultant) yang sangat berpengalaman.

    Berikut adalah deskripsi sebuah alur kerja (workflow) saat ini:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah menganalisis alur kerja ini secara kritis. Identifikasi titik-titik hambatan (bottlenecks), inefisiensi, dan area yang rentan terhadap kesalahan (human error).

    Setelah itu, berikan daftar saran perbaikan yang konkret dan dapat ditindaklanjuti (actionable). Untuk setiap saran, jelaskan 'Mengapa' ini adalah masalah dan 'Bagaimana' solusinya dapat diterapkan.

    Sajikan hasilnya dalam format daftar bernomor. Gunakan format Markdown untuk kejelasan (judul, sub-judul, teks tebal).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted list of suggestions in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Describe Your Current Workflow in Detail:" column with:**
`Our current employee reimbursement claim process: 1. Employees fill out a paper reimbursement form. 2. Employees attach physical receipts/proof of payment to the form. 3. The form is submitted to the manager for signature. 4. The manager submits the form to the HRD department. 5. HRD checks and files the physical form, then provides payment instructions to the finance team. 6. The finance team makes manual transfers.`
---
