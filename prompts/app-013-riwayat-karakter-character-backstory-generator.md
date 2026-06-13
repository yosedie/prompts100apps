## Application Name
Character History: Character Backstory Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for novel, screenplay or game writers that can create rich and in-depth character backgrounds. Users enter a few basic traits, and the AI ​​will develop them into a complete character profile, including motivations, fears, and hidden secrets.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large title says "Character History".
2.  **User Input Form:**
    *   **Character Name Input:** A text input field labeled "Character Name:".
    *   **Archetype/Role Input:** A text input field labeled "Primary Archetype/Role:".
    *   **Positive Trait Input:** A text input field labeled "Main Positive Trait:".
    *   **Weakness Input:** A text input field labeled "Main Weakness/Conflict:".
3.  **Action Button:** A main button with the text "Create Character History". While the process is running, the button should be disabled and display the status "Writing...".
4.  **Output Area:**
    *   Title (H3): "Character Profile:"
    *   A single content area to display all profiles.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the character details and clicks the “Create Character History” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis fiksi dan master pengembangan karakter (character development).

    Berdasarkan informasi dasar berikut:
    - Nama: [Nama dari input pengguna]
    - Arketipe/Peran: [Arketipe dari input pengguna]
    - Sifat Positif: [Sifat dari input pengguna]
    - Kelemahan/Konflik: [Kelemahan dari input pengguna]

    Tugas Anda adalah menciptakan profil karakter yang mendalam dan kaya. Kembangkan informasi dasar tersebut menjadi sebuah riwayat yang koheren. Profil harus mencakup bagian-bagian berikut:

    - **Ringkasan:** Paragraf singkat yang memperkenalkan karakter.
    - **Motivasi Utama:** Apa yang mendorong karakter ini untuk bertindak? Apa tujuan hidupnya?
    - **Ketakutan Terbesar:** Apa yang paling ia takuti, dan mengapa? Ini harus berhubungan dengan kelemahannya.
    - **Rahasia Terpendam:** Sebuah rahasia penting yang ia sembunyikan dari dunia, yang membentuk kepribadiannya.
    - **Latar Belakang Singkat:** Sebuah narasi singkat tentang masa lalunya yang menjelaskan bagaimana ia menjadi seperti sekarang.

    Gunakan format Markdown untuk judul, sub-judul, dan poin-poin penting agar profil mudah dibaca.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted character profile in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow for live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Character Name:" column with:**
`Kaelan`
*   **Fill in the "Primary Archetype/Role:" column with:**
`A bounty hunter in a cynical cyberpunk city`
*   **Fill in the "Main Positive Trait:" column with:**
`Have a strong personal code of ethics`
*   **Fill in the "Main Weakness/Conflict:" column with:**
`Obsessed with his past failures`
---
