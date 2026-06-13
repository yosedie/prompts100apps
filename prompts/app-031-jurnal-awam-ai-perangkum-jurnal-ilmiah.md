## Application Name
AI Public Journal: Summarize Scientific Journals

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a science translator. Users paste in the abstract or full text of a dense and technical scientific journal, and AI will summarize it into an explanation that is easy for laypeople to understand, without losing the essence of the main findings.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "AI Lay Journal".
2.  **User Input Form:**
    *   A large text area with the label "Paste Abstract or Scientific Journal Text Here:".
3.  **Action Button:** A main button with the text "Summarize for Laymen". While the process is running, the button should be activated and display the status "Translating Science...".
4.  **Output Area:**
    *   Title (H3): "Simple Summary:"
    *   A single content area to display summaries.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user pastes the journal text and clicks the "Summary for Laymen" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang komunikator sains (science communicator) yang sangat berbakat. Anda mampu memahami penelitian ilmiah yang kompleks dan menjelaskannya kepada audiens non-ahli dengan cara yang menarik dan mudah dimengerti.

    Berikut adalah teks dari sebuah jurnal ilmiah:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah merangkum teks ini untuk orang awam. Ringkasan Anda harus:
    - Menghindari jargon teknis. Jika terpaksa digunakan, jelaskan dengan analogi sederhana.
    - Fokus pada "gambaran besar": Apa pertanyaan utama penelitian ini? Apa temuan utamanya? Mengapa ini penting?
    - Disajikan dalam bentuk narasi yang mengalir, bukan poin-poin teknis.

    Gunakan format Markdown untuk penekanan pada istilah-istilah kunci yang telah Anda sederhanakan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted summary in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste Abstract or Scientific Journal Text Here:" column with:**
`Abstract: This study investigated the neuroprotective effects of curcumin against glutamate-induced oxidative stress in cultured hippocampal cells. The results showed that pretreatment with curcumin significantly suppressed the production of reactive oxygen species (ROS) and cellular apoptosis. Our data indicate that curcumin may be a potential therapeutic agent for neurodegenerative disorders mediated by excitotoxicity.`
---
