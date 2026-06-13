## Application Name
AI Negotiation Simulator: Negotiation Coach

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an interactive web application that functions as a simulator to practice negotiation skills. Users define a scenario and their roles, and then the AI ​​takes on the role of negotiating opponent, providing offers and counter-arguments dynamically in a conversational format.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Negotiation Simulator".
2.  **Initial Setup Screen:**
    *   **Scenario Input:** A text input field labeled "Describe Your Negotiation Scenario:".
    *   **Input Your Role:** A text input field labeled "What is Your Role?".
    *   **AI Role Input:** A text input field labeled "What is the Role of AI as a Negotiator?".
    *   **Opening Input:** A text area labeled "Write Your Offer or Opening Sentence:".
    *   **Start Button:** A main button with the text "Start Negotiations!".
3.  **Negotiation Screen (After Setup):**
    *   **Conversation Window:** The main area that displays negotiation history (such as chat).
    *   **Input Reply:** The text input field below is labeled "Your Reply:".
    *   **Send Button:** Button to send a reply.
    *   **Restart Button:** Button to return to the Initial Setup Screen.
4.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax into properly formatted HTML elements.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the scenario details in the Setup Screen and clicks "Start Negotiation!".
2.  The application creates an *initial system prompt* which will become the basis for the AI's role.
3.  **Conversation Logic (Important):**
    *   The app must store the entire conversation history.
    *   Every time a user sends a reply, the app must send **the entire conversation history** plus the *initial system prompt* to the AI ​​model to maintain context.
    *   New responses from the AI ​​are then added to the Conversation Window.

4.  **Initial System Prompt:**
    ```
    Anda adalah seorang negosiator ahli yang berperan sebagai [Peran AI dari input pengguna]. Tujuan Anda adalah untuk mendapatkan hasil terbaik bagi pihak Anda, namun tetap bersikap realistis dan profesional.

    Skenario negosiasinya adalah tentang [Skenario dari input pengguna]. Lawan negosiasi Anda (pengguna) berperan sebagai [Peran Pengguna dari input pengguna].

    Respons setiap argumen atau tawaran dari pengguna dengan argumen balasan yang logis. Jangan terlalu cepat menyerah. Berikan penawaran balasan jika perlu. Mulai sekarang, respons pesan pertama dari pengguna.
    ```
5.  The app displays the user's opening sentence and the AI's first response in the Conversation Window, then waits for the user's next reply.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow for live testing, autofill the input fields in the Initial Setup Screen with the following example data when the page first loads:**

*   **Fill in the "Describe Your Negotiation Scenario:" column with:**
`Negotiating the price of a used car.`
*   **Fill in the "What is Your Role?" with:**
`Careful buyers and want the lowest possible price.`
*   **Fill in the column "What is the Role of AI as a Negotiator?" with:**
`Experienced used car salesman who wants the highest possible price.`
*   **Fill in the "Write Your Offer or Opening Sentence:" column with:**
`I saw this car advertised for 150 million. It's in good condition, but I noticed a few small scratches on the door. I bid 135 million.`
---
