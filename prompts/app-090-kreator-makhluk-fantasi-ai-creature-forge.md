## Application Name
AI Fantasy Creature Creator: Creature Forge

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for world-builders that automatically designs unique fantasy creatures. Users describe an environment or habitat, and the AI ​​will create creatures that make sense to live there, complete with physical descriptions, behavior, and their role in the fictional ecosystem.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "AI Fantasy Creature Creator".
2.  **User Input Form:**
    *   A large text area labeled "Describe Your Fictitious Environment or Habitat:".
3.  **Action Button:** A main button with the text "Create Creature!". While the process is running, the button should be activated and display the status "Creating...".
4.  **Output Area:**
    *   Title (H3): "Resulting Creature:"
    *   A single content area to display all creature descriptions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user enters a description of the habitat and clicks the "Create Creature!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli ekologi fiksi dan xenobiologist. Anda ahli dalam merancang makhluk hidup yang beradaptasi secara logis dengan lingkungan mereka yang fantastis.

    Berdasarkan deskripsi habitat berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah merancang SATU makhluk unik yang hidup di habitat ini. Deskripsi makhluk harus mencakup:

    1.  **Nama Makhluk:** Berikan nama yang terdengar pas untuk makhluk tersebut.
    2.  **Deskripsi Fisik:** Jelaskan penampilan, ukuran, dan fitur-fitur uniknya. Jelaskan bagaimana fisiknya merupakan adaptasi terhadap habitatnya.
    3.  **Perilaku & Makanan:** Jelaskan bagaimana perilakunya (nokturnal, soliter, dll.) dan apa yang dimakannya.
    4.  **Peran dalam Ekosistem:** Jelaskan posisinya dalam rantai makanan atau perannya dalam ekosistem (misalnya, penyerbuk, dekomposer, predator puncak).

    Gunakan format Markdown untuk menyusun deskripsi dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays creature descriptions in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Describe Your Fictitious Environment or Habitat:" column with:**
`A swamp whose water glows with a strange mineral, filled with giant mushrooms that emit shimmering spores.`
---
