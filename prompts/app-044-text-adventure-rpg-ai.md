## Application Name
Text Adventure RPG AI

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build an interactive web application that functions as a text-based adventure game (text-based RPG). The AI ​​will act as Game Master (GM), describing the world and scenarios, while the user types in the actions they want to take. The AI ​​will respond to the action and continue the story.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Text Adventure RPG AI".
2.  **Initial Setup Screen:**
    *   **Scenario Selection:** A dropdown (select) menu with the label "Select Adventure Scenario:" and the options: "Noir Detective in a Rainy City", "Space Explorer on an Abandoned Ship", "Young Witch in the Forbidden Forest".
    *   **Start Button:** A main button with the text "Start the Adventure!".
3.  **Game Screen, after setup:**
    *   **Story Window:** A main content area that displays a narrative history of the AI ​​and actions of the user, such as a conversation log.
    *   **Action Input:** A text input field at the bottom labeled "What do you do?".
    *   **Submit Button:** Button to submit a user action.
    *   **Restart Button:** Button to return to the Initial Setup Screen.
4.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `*italic*` for scene descriptions) into properly formatted HTML elements.

## Workflow & Logic (Workflow & Logic)

1.  The user selects a scenario and clicks "Start the Adventure!".
2.  The app sends an *initial system prompt* to the AI ​​model to start the story.
3.  **Conversation Logic (Very Important):**
    *   Every time a user sends an action, the app must send **the entire conversation history** (previous AI narrative + user actions) back to the AI ​​model. This allows the AI ​​to remember the context and respond coherently.
    *   The app then adds new responses from the AI ​​to the Story Window.

4.  **Initial System Prompt:**
    ```
    Anda adalah seorang Game Master (GM) yang ahli untuk permainan petualangan berbasis teks. Tugas Anda adalah menciptakan cerita yang imersif dan interaktif.

    Aturan Anda:
    1.  Deskripsikan dunia dengan detail yang kaya (pemandangan, suara, bau).
    2.  Hadirkan tantangan, teka-teki, dan karakter non-pemain (NPC).
    3.  Respons secara realistis terhadap tindakan yang ditulis oleh pengguna.
    4.  Selalu akhiri respons Anda dengan pertanyaan "Apa yang kamu lakukan?" untuk memancing input dari pengguna.

    Berdasarkan skenario yang dipilih: "[Skenario dari pilihan pengguna]"

    Mulailah sekarang dengan menulis paragraf pembuka yang menarik untuk memulai petualangan.
    ```
5.  The app displays the first response in the Story Window, and waits for action input from the user.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, set the default options in the dropdown menu when the page first loads:**

*   **Set the "Select Adventure Scenario:" option to:**
`Detective Noir in the Rainy City`
---
