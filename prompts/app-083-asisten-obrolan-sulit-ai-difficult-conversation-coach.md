## Application Name
AI "Difficult Conversation" Assistant: Difficult Conversation Coach

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a communication coach. Users describe a difficult conversation they had to face, and the AI ​​will provide a structured guide that includes several opening line options, key points to cover, and tips for keeping the conversation productive and non-escalative.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI 'Difficult Chat' Assistant".
2.  **User Input Form:**
    *   A large text area labeled "Describe a difficult conversation you had to have:". Provide a placeholder such as "Example 1: I need to tell a coworker that the quality of their work is declining. Example 2: I want to ask my boss for a raise."
3.  **Action Button:** A main button with the text "Set Up a Conversation Strategy". While the process is running, the button should be activated and display the status "Making a Strategy...".
4.  **Output Area:**
    *   Title (H3): "Your Conversation Strategy:"
    *   A single content area to display the entire guide.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a conversation description and clicks the "Prepare Conversation Strategy" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pelatih komunikasi (communication coach) dan ahli resolusi konflik yang empatik dan strategis.

    Berdasarkan deskripsi percakapan sulit berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah membuat panduan yang jelas dan dapat ditindaklanjuti. Panduan harus mencakup tiga bagian utama:

    1.  **Opsi Kalimat Pembuka:** Berikan 2-3 opsi kalimat pembuka yang berbeda (misalnya, satu langsung, satu lebih lembut) untuk memulai percakapan dengan cara yang tidak konfrontatif.
    2.  **Poin-Poin Kunci untuk Dibahas:** Buat daftar poin-poin utama yang harus disampaikan oleh pengguna untuk memastikan pesannya jelas dan didukung oleh fakta atau perasaan (menggunakan metode "I-message").
    3.  **Tips Menjaga Percakapan Tetap Produktif:** Berikan beberapa saran tentang cara menjaga nada bicara, mendengarkan secara aktif, dan menghindari eskalasi konflik.

    Gunakan format Markdown untuk menyusun panduan dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a strategy guide in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Describe a difficult conversation you had to have:" column with:**
`I had to tell my teammate, Budi, that he was often late turning in his work, which had an impact on the whole team. I don't want to ruin our working relationship.`
---
