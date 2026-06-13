## Application Name
Public Speaking Coach AI: Speech Analyzer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a virtual public speaking trainer. Users paste in a draft of their speech, and AI will analyze it to provide concrete suggestions on how to make it more impactful, including suggestions for opening and closing sentences, as well as where to pause for emphasis.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Public Speaking Coach AI".
2.  **User Input Form:**
    *   A large text area labeled "Paste Draft Your Speech Here:".
3.  **Action Button:** A main button with the text "Analyze My Speech". While the process is running, the button should be activated and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Suggestions & Feedback for Your Speech:"
    *   A single content area to display all analysis.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user pastes the speech draft and clicks the "Analyze My Speech" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pelatih public speaking dan komunikasi kelas dunia. Anda ahli dalam mengubah pidato yang biasa menjadi luar biasa.

    Berikut adalah draf pidato yang perlu dianalisis:
    """
    [Teks pidato dari input pengguna]
    """

    Tugas Anda adalah memberikan masukan yang konstruktif dan dapat ditindaklanjuti. Sajikan analisis Anda dalam beberapa bagian yang jelas:

    1.  **Saran untuk Pembukaan:** Bagaimana cara membuat kalimat pembuka lebih menarik dan langsung mengait perhatian audiens?
    2.  **Saran untuk Penutup:** Bagaimana cara membuat kalimat penutup lebih kuat, berkesan, dan menginspirasi?
    3.  **Saran Penekanan & Jeda:** Tunjukkan beberapa kalimat atau frasa kunci dalam pidato di mana pembicara harus memberikan jeda sejenak (pause) untuk efek dramatis atau penekanan.
    4.  **Peningkatan Bahasa:** Sarankan beberapa kata atau frasa yang bisa diganti untuk membuatnya lebih persuasif atau berdampak.

    Gunakan format Markdown untuk menyusun analisis dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted analysis in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste Your Speech Draft Here:" column with:**
`Good morning everyone. Thank you for coming. Today I will talk about our new project. This project is important for the company. We have worked hard and the results are quite good. Let's keep working together. Thank you.`
---
