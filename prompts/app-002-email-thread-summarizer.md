## Application Name
Email Thread Summarizer

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that serves to summarize long email threads. Users paste the entire email content into the input area, and the application will analyze it to produce a main summary in 3 points as well as a list of tasks (action items) complete with the person responsible in table format.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large header says "Email Thread Summarizer".
2.  **Input Area:**
    *   A large, tall textarea labeled "Paste entire email thread here:".
3.  **Action Button:** A main button with the text "Compact Now!". While the process is running, the button should be disabled and display the status "Analyzing...".
4.  **Output Area:** Divided into two clear sections:
    *   **Summary Section:**
        *   Title (H3): "Main Summary"
        *   Content area to display 3 summary points in a numbered list format.
    *   **Action Items section:**
        *   Title (H3): "Action Items"
        *   Content area to display a table of tasks and people in charge.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (especially numbered lists and tables) into properly formatted HTML elements. Apply this rendering to both parts in the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  The user pastes the text of the email thread and clicks the "Summarize Now!" button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang asisten eksekutif AI yang sangat efisien, berspesialisasi dalam menganalisis utas email yang panjang dan mengekstrak informasi paling penting.

    Berikut adalah utas email untuk dianalisis:
    """
    [Utas email dari input pengguna]
    """

    Tugas Anda adalah:
    1.  **Ringkasan Utama:** Sajikan 3 poin ringkasan utama dari keseluruhan diskusi.
    2.  **Action Items:** Identifikasi semua tugas spesifik (action items), siapa yang bertanggung jawab (penanggung jawab), dan sajikan dalam format tabel yang jelas.

    Gunakan Markdown untuk format. Untuk tabel, gunakan format Markdown table dengan header "Tugas (Action Item)" dan "Penanggung Jawab (PIC)".
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving the response, the application parses the text, separating the summary section and the action items table section.
5.  The application renders the Markdown content of each section into HTML, then displays it in the appropriate output area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill the input area with the following example data when the page first loads:**

*   **Fill in the "Paste entire email thread here:" field with:**
    ```
    From: Andi (Project Manager)
    To: Tim Proyek Phoenix
    Subject: Status Terkini Proyek Phoenix

    Halo tim,

    Saya ingin mengecek status terkini untuk Proyek Phoenix yang deadline-nya semakin dekat. Kita sepertinya sedikit tertinggal dari jadwal. Mohon update dari masing-masing penanggung jawab.

    Terima kasih,
    Andi

    ---
    From: Budi (Developer)
    To: Tim Proyek Phoenix
    Subject: Re: Status Terkini Proyek Phoenix

    Hai Andi,

    Untuk bagian backend, API utama sudah selesai 100%. Saya sekarang sedang menunggu aset desain final dari Citra untuk bisa melanjutkan integrasi ke antarmuka pengguna.

    Salam,
    Budi

    ---
    From: Citra (Designer)
    To: Tim Proyek Phoenix
    Subject: Re: Status Terkini Proyek Phoenix

    Mohon maaf atas keterlambatannya. Ada beberapa revisi minor dari klien. Mockup final sudah siap dan akan saya unggah ke folder Google Drive bersama semua asetnya paling lambat sore ini.

    Terima kasih,
    Citra

    ---
    From: Andi (Project Manager)
    To: Tim Proyek Phoenix
    Subject: Re: Status Terkini Proyek Phoenix

    Baik, terima kasih atas updatenya Budi dan Citra.

    Kalau begitu, Budi, tolong segera mulai proses integrasi setelah aset dari Citra tersedia. Saya sendiri akan memperbarui timeline proyek di Asana dan melaporkannya ke manajemen.

    Kerja bagus semua!
    Andi
    ```
---
