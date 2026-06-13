## Application Name
Alibi Weaver AI: Fictional Alibi Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application for writers and role players. Users describe a fictional crime and a character who needs an alibi, then the AI ​​will construct a detailed, logical, and (almost) unbreakable alibi, complete with fictional witnesses and supporting evidence.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Alibi Weaver AI".
2.  **User Input Form:**
    *   **Crime Input:** A text area labeled "Describe a Fictitious Crime (Time, Place, Type):".
    *   **Character Input:** A text input field labeled "Characters Requiring Alibi:".
3.  **Action Button:** A main button with the text "Create an Alibi!". While the process is running, the button should be activated and display the status "Looking for Gaps...".
4.  **Output Area:**
    *   Headline (H3): "Resulting Alibi:"
    *   A single content area to display all alibis.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user fills in the crime and character details, then clicks the "Create Alibi!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang perencana kriminal jenius dan ahli strategi yang sangat teliti. Anda mampu menciptakan alibi yang nyaris sempurna.

    Berdasarkan skenario fiktif berikut:
    - Kejahatan: """[Deskripsi kejahatan dari input pengguna]"""
    - Karakter yang Membutuhkan Alibi: [Nama karakter dari input pengguna]

    Tugas Anda adalah membuat alibi yang detail dan meyakinkan untuk karakter tersebut. Alibi harus mencakup:

    1.  **Linimasa (Timeline):** Rincian aktivitas karakter, menit demi menit, selama waktu kejahatan terjadi.
    2.  **Saksi Fiktif:** Sebutkan setidaknya satu orang atau tempat (misal: pelayan restoran, rekaman CCTV) yang bisa "memverifikasi" keberadaan karakter.
    3.  **Bukti Pendukung Fiktif:** Sebutkan bukti fisik atau digital yang mendukung alibi (misal: struk pembayaran, postingan media sosial, riwayat panggilan).
    4.  **Sikap Saat Diinterogasi:** Berikan saran singkat tentang bagaimana karakter harus bersikap jika ditanyai oleh detektif.

    Gunakan format Markdown untuk menyusun alibi dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted alibi in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the column "Describe a Fictitious Crime (Time, Place, Type):" with:**
`A safe break-in at the Municipal Museum of Art on Tuesday, between 10pm and 11pm.`
*   **Fill in the "Characters Who Require an Alibi:" column with:**
`Victor "The Ghost" Sterling, a master thief known for his intelligence.`
---
