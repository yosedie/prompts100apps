## Application Name
The Pro AI Debate: Counter-Arguments

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an interactive web application that serves as a virtual debater. Users enter a topic, choose a position (Pro or Con), and write their argument. AI will automatically take the opposing position and provide logical and structured counter-arguments to train the user's debating skills.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "Pro AI Debate".
2.  **User Input Form:**
    *   **Debate Topic Input:** A text input field labeled "Debate Topic:".
    *   **Position Selection:** A dropdown (select) menu with the label "Your Position:" and options: "Pros" and "Cons".
    *   **Input Argument:** A large text area labeled "Your Argument:".
3.  **Action Button:** A main button with the text "Give a Counter-Argument!". While the process is running, the button should be disabled and display the status "Contemplating Rebuttal...".
4.  **Output Area:**
    *   Title (H3): "Arguments from Opponents of the Debate:"
    *   A single content area to display AI's counterarguments.
    *   **Advanced Instructions:** Below the AI ​​argument, display the instruction text: "*To continue the debate, write your rebuttal in the 'Your Argument' column above and click the button again.*"
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and bullet lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the topic, position, and initial argument, then clicks the button.
2.  The application determines the position the AI ​​should take (if the user is 'Pro', the AI ​​is 'Con', and vice versa).
3.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli debat yang logis, kritis, dan terstruktur. Anda sangat pandai dalam menemukan kelemahan dalam argumen lawan dan memberikan sanggahan yang kuat.

    Konteks Debat:
    - Topik: [Topik dari input pengguna]
    - Posisi Lawan (Pengguna): [Posisi dari pilihan pengguna]
    - Argumen Lawan (Pengguna): """[Argumen dari input pengguna]"""

    Tugas Anda adalah:
    1.  Ambil posisi yang **BERLAWANAN** dari lawan Anda.
    2.  Berikan argumen tandingan yang kuat dan terstruktur.
    3.  Serang kelemahan, asumsi, atau celah logika dalam argumen lawan.
    4.  Gunakan data, logika, atau contoh untuk mendukung poin Anda.

    PENTING: Hanya berikan argumen tandingan Anda, tanpa kalimat pembuka seperti "Baik, saya akan mengambil posisi kontra...". Langsung saja ke argumennya.
    ```
4.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
5.  After receiving a response, the application renders the Markdown content of the response into HTML.
6.  The application displays AI counterarguments in the Output Area. This flow repeats every time the user submits a new argument.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow for live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Debate Topic:" column with:**
`Remote work (WFH) is better than working in the office.`
*   **Set the "Your Position:" option to:**
`Pro`
*   **Fill in the "Your argument:" column with:**
`Remote work provides time flexibility and saves transportation costs, thereby improving work-life balance for employees.'
---
