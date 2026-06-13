## Application Name
Radio Ad Pro: Advertising Copywriter

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a radio ad copywriter. Users enter a product description and select a duration, then AI will create a complete ad script, including directions for sound effects (SFX), music, and dialogue for a duration of 30 or 60 seconds.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Radio Ad Pro".
2.  **User Input Form:**
    *   **Input Product Description:** A text area labeled "Your Product/Service Description:".
    *   **Duration Selection:** A dropdown (select) menu with the label "Select Ad Duration:" and options: "30 Seconds" and "60 Seconds".
3.  **Action Button:** A main button with the text "Create Ad Script". While the process is running, the button should be activated and display the status "On Air...".
4.  **Output Area:**
    *   Title (H3): "Radio Advertising Script:"
    *   A single content area to display the entire manuscript.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and `*italic*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in the product description, select a duration, and click the “Create Ad Script” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang copywriter iklan dan produser audio yang ahli dalam membuat naskah iklan radio yang menarik dan efektif.

    Berdasarkan informasi berikut:
    - Deskripsi Produk: [Deskripsi dari input pengguna]
    - Durasi Iklan: [Durasi dari pilihan pengguna]

    Tugas Anda adalah membuat naskah iklan radio yang lengkap dan siap produksi. Naskah harus diformat secara profesional dan mencakup:

    1.  **Arahan Musik:** Petunjuk tentang jenis musik yang harus diputar (contoh: [MUSIK: Upbeat dan ceria masuk lalu fade out]).
    2.  **Arahan Efek Suara (SFX):** Petunjuk untuk suara-suara yang relevan (contoh: [SFX: Suara mesin kopi espresso, cangkir beradu]).
    3.  **Dialog (NARATOR/SUARA):** Dialog yang diucapkan oleh narator atau karakter.

    Pastikan total durasi naskah sesuai dengan yang diminta. Naskah harus memiliki pembuka yang menarik, isi yang menjelaskan keunggulan produk, dan penutup dengan call-to-action yang jelas. Gunakan format Markdown untuk memisahkan arahan (SFX/Musik) dari dialog agar mudah dibaca.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted script in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Description of Your Product/Service:" column with:**
`Coffee Express: A 'grab-and-go' coffee shop that serves premium coffee quickly to busy professionals in the morning.`
*   **Set the "Select Ad Duration:" option to:**
`30 Seconds`
---
