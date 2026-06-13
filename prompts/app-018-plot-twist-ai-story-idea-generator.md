## Application Name
Plot Twist AI: Story Idea Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a creative web application for writers. Users enter a synopsis or summary of their story, and the AI ​​will provide 3 unexpected plot twist ideas that have the potential to drastically change the direction of the narrative.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Plot Twist".
2.  **User Input Form:**
    *   A large text area labeled "Paste Your Story Synopsis Here:".
3.  **Action Buttons:** A main button with the text "Look for the Plot Twist!". While the process is running, the button should be disabled and display the "Thinking Out Loud..." status.
4.  **Output Area:**
    *   Title (H3): "3 Unexpected Twist Plot Ideas:"
    *   A single content area to showcase 3 plot twist ideas.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `###` for title and `**` for bold) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a synopsis and clicks the "Search for Plot Twist!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis novel misteri dan skenario film thriller yang ahli dalam menciptakan plot twist yang mengejutkan dan cerdas.

    Berikut adalah sinopsis sebuah cerita:
    """
    [Sinopsis dari input pengguna]
    """

    Tugas Anda adalah membaca sinopsis ini dan memberikan **3 ide plot twist yang benar-benar tak terduga**. Untuk setiap ide, jelaskan secara singkat twist-nya dan bagaimana hal itu bisa mengubah arah cerita secara drastis.

    Gunakan format Markdown untuk memisahkan setiap ide dengan jelas, misalnya dengan sub-judul.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays 3 plot twist ideas that have been formatted in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste Your Story Synopsis Here:" column with:**
`A veteran detective haunted by the past must hunt down a serial killer who leaves puzzles at every crime scene. The detective slowly realizes that all the victims have a connection to an old case that he failed to solve.`
---
