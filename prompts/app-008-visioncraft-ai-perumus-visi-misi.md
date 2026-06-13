## Application Name
VisionCraft AI: Vision & Mission Formulator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a strategic web application that helps business leaders formulate strong Vision and Mission statements. Users enter their company's core values ​​and business goals, and AI will draft an inspiring Vision statement and a concise, actionable Mission.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "VisionCraft AI".
2.  **User Input Form:**
    *   **Core Values ​​Input:** A text area labeled "What are your company's core values? (separate with commas)".
    *   **Input Business Goal:** A text area labeled "Describe Your Main Business Goal:".
3.  **Action Button:** A main button with the text "Formulate Vision & Mission". While the process is running, the button should be disabled and display the status "Formulating...".
4.  **Output Area:** Divided into two clear sections:
    *   **Vision Section:** Heading (H3) "Vision Statement" followed by a content area to display the draft vision. There should be a "Copy" button next to it.
    *   **Mission Section:** Title (H3) "Mission Statement" followed by a content area to display the mission draft. There should be a "Copy" button next to it.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert the Markdown syntax (if any) into properly formatted HTML elements. Apply this rendering to both parts in the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in the core values ​​and business goals, then click the "Formulate Vision & Mission" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang konsultan strategi bisnis dan branding yang ahli dalam merumuskan identitas perusahaan.

    Berdasarkan informasi berikut:
    - Nilai-Nilai Inti Perusahaan: [Nilai-nilai dari input pengguna]
    - Tujuan Utama Bisnis: [Tujuan dari input pengguna]

    Tugas Anda adalah membuat DUA pernyataan terpisah:

    1.  **Pernyataan Visi:** Sebuah kalimat yang inspiratif, berorientasi ke masa depan, dan menggambarkan dampak besar yang ingin dicapai perusahaan.
    2.  **Pernyataan Misi:** Sebuah kalimat yang ringkas, jelas, dan berorientasi pada tindakan, yang menjelaskan apa yang dilakukan perusahaan, untuk siapa, dan bagaimana caranya untuk mencapai visi tersebut.

    Pastikan kedua pernyataan tersebut selaras dengan nilai dan tujuan yang diberikan. Sajikan hasilnya dengan jelas, dipisahkan oleh judul. Gunakan format Markdown untuk judul.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response, the application parses it to separate Vision and Mission.
5.  The application renders the Markdown content of each section into HTML, then displays it in the appropriate output area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "What Are Your Company's Core Values?..." column with:**
`Innovation, Sustainability, Local Community Empowerment`
*   **Fill in the "Describe the Main Goal of Your Business:" column with:**
`To become the leading e-commerce platform for eco-friendly handicraft products in Southeast Asia and help small craftsmen reach global markets.`
---
