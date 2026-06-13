## Application Name
AI Microfinance Consultant

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a personal financial consultant. Users describe their lifestyle, spending habits and financial goals, and AI provides a series of practical, actionable tips for saving and managing daily finances.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Microfinance Consultant".
2.  **User Input Form:**
    *   **Lifestyle Input:** A text area labeled "Describe your lifestyle & spending habits:".
    *   **Input Financial Goals:** A text area labeled "What is your main financial goal right now?".
3.  **Action Button:** A home button with the text "Give Me Financial Tips". While the process is running, the button should be disabled and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Practical Financial Tips For You:"
    *   A single content area to display all tips.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in lifestyle and goal details, then click the "Give Me Financial Tips" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang perencana keuangan pribadi (personal financial planner) yang ramah dan praktis. Anda ahli dalam memberikan saran yang mudah diterapkan, bukan teori yang rumit.

    Berdasarkan profil pengguna berikut:
    - Gaya Hidup & Kebiasaan: [Deskripsi dari input pengguna 1]
    - Tujuan Finansial: [Tujuan dari input pengguna 2]

    Tugas Anda adalah memberikan serangkaian tips keuangan yang personal dan dapat ditindaklanjuti. Kelompokkan tips Anda ke dalam dua kategori:

    1.  **Kebiasaan Harian & Mingguan (Quick Wins):** Berikan tips-tips kecil yang bisa langsung diterapkan untuk mengurangi pengeluaran dan meningkatkan tabungan berdasarkan gaya hidup yang dijelaskan.
    2.  **Strategi Mencapai Tujuan:** Berikan langkah-langkah konkret untuk mencapai tujuan finansial yang spesifik tersebut.

    Gunakan format Markdown untuk menyusun tips dengan rapi (judul, sub-judul, daftar poin).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays financial tips that have been formatted in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow for live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Describe your lifestyle & spending habits:" column with:**
`I am a student with an irregular income from part-time work. I often snack on coffee and eat out because I'm busy with my college schedule.`
*   **Fill in the column "What is your main financial goal right now?" with:**
`Want to save to buy a new laptop worth 10 million within 6 months.`
---
