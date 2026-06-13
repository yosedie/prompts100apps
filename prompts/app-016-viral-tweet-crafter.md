## Application Name
Viral Tweet Crafter

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a content generator for platform X (Twitter). Users enter an idea, topic, or article link, and the AI ​​will generate 3 draft tweets or threads designed for virality, complete with relevant hashtags and calls-to-action.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Viral Tweet Crafter".
2.  **User Input Form:**
    *   A large text area labeled "Enter Your Article Idea, Topic, or Link:".
3.  **Action Button:** A main button with the text "Draft Tweet". While the process is running, the button should be activated and display the status "Compiling...".
4.  **Output Area:**
    *   Title (H3): "3 Draft Tweets/Threads for You:"
    *   A single content area to display 3 drafts. Each draft should be clearly separated.
    *   **Copy Button:** Each draft should have an individual "Copy" button next to it.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters an idea/link and clicks the "Draft Tweet" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang Social Media Manager dan ahli growth hacking yang sangat berpengalaman dalam menciptakan konten viral di platform X (Twitter).

    Berdasarkan input berikut:
    """
    [Input dari pengguna]
    """

    Tugas Anda adalah membuat **3 draf tweet atau thread yang berbeda** untuk memaksimalkan engagement (likes, retweets, replies). Setiap draf harus memiliki pendekatan yang unik.

    Untuk setiap draf, sertakan:
    - **Hook yang Kuat:** Kalimat pertama yang provokatif atau membuat penasaran.
    - **Isi yang Padat:** Sajikan informasi utama dengan ringkas.
    - **Hashtag Relevan:** 2-3 hashtag yang relevan.
    - **Call-to-Action (CTA):** Sebuah pertanyaan atau ajakan untuk memancing interaksi.

    Gunakan format Markdown untuk memisahkan setiap draf dengan jelas (misalnya, menggunakan garis horizontal `---`).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 3 draft tweets that have been formatted in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Enter your idea, topic or article link:" column with:**
`Idea: Bad sleeping habits can actually reduce work productivity by more than 50%.`
---
