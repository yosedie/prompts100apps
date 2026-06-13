## Application Name
AI Virtual Tour Guide

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a personal tour guide. Users enter the name of a famous city or museum, and the AI ​​will write an immersive and informative tour narrative, as if the user were walking through that location.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Virtual Tour Guide".
2.  **User Input Form:**
    *   A text input field labeled "Enter Tour Location (City or Museum):".
3.  **Action Button:** A main button with the text "Start Virtual Tour!". While the process is running, the button should be activated and display the status "Exploring Locations...".
4.  **Output Area:**
    *   Title (H3): "Your Virtual Tour Narrative:"
    *   A single content area to display the entire tour narrative.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a location and clicks the "Start Virtual Tour!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pemandu wisata (tour guide) yang sangat berpengetahuan, karismatik, dan pandai bercerita.

    Berdasarkan lokasi berikut:
    """
    [Lokasi dari input pengguna]
    """

    Tugas Anda adalah menulis sebuah naskah tur virtual yang imersif. Tulis narasi dari sudut pandang orang pertama jamak ("Kita sekarang berada di...", "Di sebelah kanan kita, kita bisa melihat...").

    Narasi harus mencakup:
    - **Deskripsi Visual:** Lukiskan gambaran yang jelas tentang pemandangan di sekitar.
    - **Fakta Sejarah:** Sisipkan fakta-fakta sejarah yang menarik dan relevan.
    - **Anekdot & Cerita Menarik:** Bagikan cerita atau detail kecil yang tidak banyak diketahui orang.
    - **Arahan Virtual:** Berikan arahan seolah-olah kita sedang berjalan ("Mari kita berjalan sedikit ke depan...").

    Gunakan format Markdown untuk penekanan pada nama tempat atau detail penting.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted tour narrative in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Tour Location (City or Museum):" field with:**
`Tokyo`
---
