## Application Name
AI Storyteller: Alternate History

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a narrative web application that retells historical events from an unusual perspective. Users enter a historical event and unique perspective, and the AI ​​will write an immersive short story from that point of view.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Alternative History Teacher".
2.  **User Input Form:**
    *   **History Event Input:** A text input field labeled "History Event:".
    *   **Point of View Input:** A text input field labeled "Tell me from the Point of View (example: a cook, a carrier pigeon):".
3.  **Action Button:** A home button with the text "Tell the Story!". While the process is running, the button should be activated and display the status "Browsing Archives...".
4.  **Output Area:**
    *   Title (H3): "The Story from Another Point of View:"
    *   A single content area to display generated stories.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*` or paragraphs) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the events and point of view, then clicks the "Tell the Story!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang sejarawan naratif dan penulis fiksi sejarah yang ahli. Anda mampu menghidupkan kembali peristiwa sejarah melalui mata orang-orang biasa yang sering terlupakan.

    Berdasarkan informasi berikut:
    - Peristiwa Sejarah: [Peristiwa dari input pengguna]
    - Sudut Pandang: [Sudut pandang dari input pengguna]

    Tugas Anda adalah menulis sebuah cerita pendek naratif (first-person) dari sudut pandang yang diberikan. Cerita harus:
    - Terasa otentik dan imersif.
    - Menggunakan detail sensorik (bau, suara, pemandangan) yang relevan dengan sudut pandang tersebut.
    - Menghubungkan pengalaman pribadi karakter dengan peristiwa sejarah yang lebih besar yang terjadi di sekitarnya.

    Gunakan gaya naratif yang mengalir dan puitis. Gunakan format Markdown untuk penekanan jika diperlukan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted story in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Historical Event:" column with:**
`World War II on the Eastern Front`
*   **Fill in the "Tell me from your point of view..." column with:**
`A cook in an army unit`
---
