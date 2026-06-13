## Application Name
WorldForge AI: Fictional World Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for writers and world-builders. Users enter one core theme or concept, and the AI ​​will generate a rich, in-depth description of a new fictional world, complete with its geography, culture, magic/technological systems, and political factions.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "WorldForge AI".
2.  **User Input Form:**
    *   A large text area labeled "Enter Your Main Theme or Core World Concept:".
3.  **Action Button:** A main button with the text "Create the World!". While the process is running, the button should be disabled and display the status "Building Reality...".
4.  **Output Area:**
    *   Title (H3): "Description of Your Fictional World:"
    *   A single content area to display the entire description.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a theme and clicks the "Create a World!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang world-builder veteran, sejarawan fiksi, dan penulis fantasi epik.

    Berdasarkan tema inti berikut:
    """
    [Tema dari input pengguna]
    """

    Tugas Anda adalah menciptakan deskripsi yang kaya dan mendalam untuk sebuah dunia fiksi baru. Deskripsi harus mencakup empat pilar utama:

    1.  **Geografi Unik:** Jelaskan lanskap, iklim, dan ciri khas geografis dunia ini.
    2.  **Budaya & Masyarakat:** Deskripsikan penduduknya, tradisi mereka, dan bagaimana mereka beradaptasi dengan lingkungannya.
    3.  **Sistem Sihir atau Teknologi Khas:** Jelaskan sumber kekuatan di dunia ini. Apakah itu sihir, teknologi uap, psionik, atau lainnya? Bagaimana cara kerjanya?
    4.  **Faksi & Politik:** Sebutkan 2-3 faksi atau kerajaan utama yang ada, dan jelaskan hubungan atau konflik di antara mereka.

    Gunakan format Markdown untuk menyusun deskripsi dengan rapi (judul, sub-judul, daftar poin).
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays a formatted world description in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Enter the Main Theme or Core Concept of Your World:" field with:**
`A world where cities float on a sea of ​​poisonous clouds, and travel between cities is by airship.`
---
