## Application Name
Auto Generator FAQ

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that intelligently generates a list of Frequently Asked Questions (FAQ) from a text description. Users simply paste in a product, service, or project description, and the app will generate a list of relevant questions along with clear and concise answers.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Automatic FAQ Generator".
2.  **User Input Form:**
    *   A large text area labeled "Paste Your Product or Service Description Here:".
3.  **Action Button:** A main button with the text "Create FAQ List". While the process is running, the button should be disabled and display the status "Analyzing...".
4.  **Output Area:**
    *   Title (H3): "Generated FAQ List:"
    *   A single content area to display a list of questions and answers.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `###` for questions and `**` for bold) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user pastes the description text and clicks the "Create FAQ List" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang spesialis customer support dan copywriter yang berpengalaman. Tugas Anda adalah membaca deskripsi sebuah produk atau layanan dan mengantisipasi pertanyaan yang paling mungkin ditanyakan oleh calon pengguna.

    Berikut adalah deskripsi yang perlu dianalisis:
    """
    [Teks deskripsi dari input pengguna]
    """

    Berdasarkan deskripsi di atas, buatlah daftar Pertanyaan yang Sering Diajukan (FAQ) yang komprehensif. Untuk setiap pertanyaan, berikan jawaban yang jelas dan ringkas langsung dari informasi yang tersedia.

    Gunakan format Markdown berikut untuk setiap item FAQ:
    ### Pertanyaan?
    Jawaban.

    Pastikan pertanyaan mencakup aspek-aspek penting seperti fitur utama, harga, keamanan, dan cara penggunaan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted list of FAQs in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste Your Product or Service Description Here:" field with:**
`AwanAman is a premium cloud storage service that offers end-to-end encryption security. Users get 10GB free when signing up and can upgrade to a paid plan for more capacity. Our features include automatic file sync across devices, file sharing with secure links, and 30-day file version history.`
---
