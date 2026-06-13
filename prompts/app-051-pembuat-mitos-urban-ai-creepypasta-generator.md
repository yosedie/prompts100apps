## Application Name
AI Urban Myth Generator: Creepypasta Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that creates a new, scary urban legend or creepypasta story. Users enter a common location or object, and the AI ​​will write a short horror story that feels like a myth that can spread by word of mouth.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Urban AI Mythmaker".
2.  **User Input Form:**
    *   A text input field labeled "What Locations or Objects Hold Scary Stories?".
3.  **Action Button:** A main button with the text "Create a Myth". While the process is running, the button should be disabled and display the status "Whispering Stories...".
4.  **Output Area:**
    *   Title (H3): "A New Urban Legend:"
    *   A single content area to display the entire story.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*` for emphasis) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a location/object and clicks the "Create Myth" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pencerita horor ulung dan penulis creepypasta. Anda ahli dalam mengambil hal-hal biasa dan membuatnya terasa sangat menyeramkan.

    Berdasarkan lokasi/objek berikut:
    """
    [Input dari pengguna]
    """

    Tugas Anda adalah menulis sebuah cerita legenda urban atau creepypasta pendek yang baru dan orisinal. Cerita harus:
    - Dimulai dengan suasana yang normal dan familiar.
    - Memperkenalkan elemen yang aneh atau tidak pada tempatnya secara perlahan.
    - Membangun ketegangan dan rasa takut.
    - Berakhir dengan kesimpulan yang mengerikan atau pertanyaan yang menghantui.

    Gaya tulisan harus terasa personal, seolah-olah ini adalah cerita yang "benar-benar terjadi" dan diceritakan kembali. Gunakan format Markdown untuk penekanan.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted story in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "What Locations or Objects Tell Scary Stories?" with:**
`People crossing bridge at night`
---
