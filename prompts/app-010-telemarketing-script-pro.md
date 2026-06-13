## Application Name
Telemarketing Script Pro

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a telemarketing script generator. Users enter information about the product, its benefits and the target audience, and AI will create a complete and effective sales call script, from opening lines to how to overcome objections.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "Telemarketing Script Pro".
2.  **User Input Form:**
    *   **Product/Service Input:** A text input field labeled "Name of Product/Service Offered:".
    *   **Input Advantages:** A text area labeled "Main Advantages:".
    *   **Input Target Audience:** A text area with the label "Who is your Target Audience?".
3.  **Action Button:** A main button with the text "Create Sales Copy". While the process is running, the button should be activated and display the status "Compiling Manuscript...".
4.  **Output Area:**
    *   Title (H3): "Sales Call Script:"
    *   A single content area to display the entire manuscript.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users fill in product and audience details, then click the "Create Sales Copy" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang penulis naskah penjualan (sales scriptwriter) dan pelatih telemarketing yang sangat berpengalaman.

    Berdasarkan informasi berikut:
    - Produk/Layanan: [Nama dari input pengguna]
    - Keunggulan Utama: [Poin-poin dari input pengguna]
    - Target Audiens: [Deskripsi dari input pengguna]

    Tugas Anda adalah membuat naskah panggilan penjualan (telemarketing script) yang lengkap dan persuasif. Naskah harus terstruktur dengan jelas dan mencakup bagian-bagian berikut:

    1.  **Pembuka (Opening):** Kalimat pembuka yang menarik perhatian dan membangun rapport dalam beberapa detik.
    2.  **Penyampaian Nilai (Value Proposition):** Jelaskan secara singkat bagaimana produk/layanan ini bisa membantu target audiens, berdasarkan keunggulan yang diberikan.
    3.  **Mengatasi Penolakan Umum (Handling Objections):** Sediakan contoh cara menjawab penolakan umum seperti "Saya tidak tertarik," "Harganya terlalu mahal," atau "Saya sedang sibuk."
    4.  **Panggilan untuk Bertindak (Call to Action):** Kalimat penutup yang jelas untuk mengarahkan prospek ke langkah selanjutnya (misalnya, menjadwalkan demo, mengirim email, dll.).

    Gunakan format Markdown untuk judul, sub-judul, dan poin-poin penting agar naskah mudah dibaca dan diikuti.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays the formatted script in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Name of Product/Service Offered:" column with:**
`SyncUp CRM`
*   **Fill in the "Main Advantages:" column with:**
`- Automate email follow-up to customers.
    - Real-time sales analytics dashboard.
    - Manage all customer data in one place, no more spreadsheets needed.`
*   **Fill in the column "Who is your target audience?" with:**
`Small and medium business (SME) owners who currently still manage customer data manually.`
---
