## Application Name
AI Harmony Design: Palette & Mood Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for designers and creators. Users enter a theme or visual keywords, and the AI ​​will generate a harmonious color palette (complete with HEX codes) as well as a brief description of the mood created by the palette.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Harmonious Design".
2.  **User Input Form:**
    *   A text input field labeled "Enter Theme or Visual Keywords:".
3.  **Action Button:** A main button with the text "Create Design Palette". While the process is running, the button should be activated and display the status "Searching for Harmony...".
4.  **Output Area:** Divided into two clear sections:
    *   **Color Palette Section:**
        *   Title (H3): "Resulting Color Palette:"
        *   This area should display 5 colored squares (swatches) horizontally. The background of each box must be filled with the color according to the resulting HEX code. Inside each box, display the HEX code of that color with contrasting text for easy reading.
    *   **Mood Description Section:**
        *   Title (H3): "Visual Mood Description:"
        *   Content area to display a brief description of the AI.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert the Markdown syntax (if any) into formatted HTML elements. Apply this rendering to the Mood Description section.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a theme and clicks the “Create Design Palette” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang desainer grafis senior dan ahli teori warna (color theorist).

    Berdasarkan tema berikut:
    """
    [Tema dari input pengguna]
    """

    Tugas Anda adalah menghasilkan DUA hal:

    1.  **Palet Warna:** Buat palet berisi 5 warna yang harmonis. Sajikan dalam format daftar, di mana setiap item adalah kode HEX warna (contoh: `#FFFFFF`).
    2.  **Deskripsi Mood Visual:** Tulis deskripsi singkat (2-3 kalimat) yang menjelaskan suasana atau mood yang diciptakan oleh palet warna ini.

    Pisahkan kedua bagian dengan jelas menggunakan penanda unik: `---MOOD---`.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application parses the text. The text before `---MOOD---` is a list of HEX codes. The text that follows is a mood description.
5.  The application uses a list of HEX codes to dynamically create 5 colored squares.
6.  The app renders a mood description (with Markdown) and displays it in the appropriate area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Enter Theme or Visual Keywords:" column with:**
`Tropical twilight`
---
