## Application Name
Author of Eulogy AI: In Loving Memory

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that helps users compose memorial eulogies during difficult times. Users enter memories, good qualities, and their relationship with the deceased, then AI will help assemble them into a sincere, moving, and respectful eulogy.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Eulogy Writer".
2.  **User Input Form:**
    *   **Relationship Input:** A text input field with the label "What was your relationship with the deceased/deceased?".
    *   **Input Traits:** A text area with the label "Name the 3 best traits you remember most about him:".
    *   **Input Memories:** A text area with the label "Tell me one short, most memorable memory with him:".
3.  **Action Button:** A main button with the text "Draft Eulogy". While the process is running, the button should be activated and display the status "Recalling...".
4.  **Output Area:**
    *   Title (H3): "Draft Your Eulogy:"
    *   A single content area to display the entire manuscript.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the memorial details and clicks the “Draft Eulogy” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis yang sangat empatik dan bijaksana. Anda mampu merangkai kata-kata untuk menghormati kenangan seseorang dengan cara yang tulus dan mengharukan.

    Berdasarkan informasi berikut:
    - Hubungan Penulis: [Hubungan dari input pengguna]
    - Sifat Terbaik Almarhum/ah: """[Sifat dari input pengguna]"""
    - Kenangan Berkesan: """[Kenangan dari input pengguna]"""

    Tugas Anda adalah menulis sebuah draf eulogi yang singkat dan penuh hormat. Naskah harus:
    - Memiliki pembukaan yang memperkenalkan hubungan Anda dengan almarhum/ah.
    - Mengintegrasikan cerita tentang sifat-sifat baik dan kenangan yang diberikan.
    - Memiliki penutup yang merefleksikan warisan atau dampak positif yang ditinggalkan.
    - Menggunakan nada yang tulus, hangat, dan menghibur.

    Gunakan placeholder `[Nama Almarhum/ah]` agar mudah disesuaikan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the draft eulogy in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What was your relationship with the deceased/deceased?" with:**
`I am his grandson.`
*   **Fill in the column "Name the 3 best qualities that you remember most about him:" with:**
`Always patient, has a great sense of humor and is really good at baking.`
*   **Fill in the column "Tell me one short, most memorable memory with him:" with:**
`I remember when he taught me how to make his first chocolate cake, even though the kitchen was a mess, he just laughed and said that the mess was part of the adventure.'
---
