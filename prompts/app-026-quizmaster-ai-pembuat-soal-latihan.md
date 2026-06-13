## Application Name
QuizMaster AI: Practice Question Generator

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that automatically creates practice questions from a text or course material. Users paste in material, select the type and number of questions, and AI will generate relevant quizzes to test understanding.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The large headline says "QuizMaster AI".
2.  **User Input Form:**
    *   **Input Material:** A large text area labeled "Paste Text or Study Material Here:".
    *   **Question Type Selection:** A dropdown (select) menu with the label "Select Question Type:" and options: "Multiple Choice", "Essay", "Mixed (5 PG, 5 Essays)".
    *   **Input Number of Questions:** A number input field (type="number") with the label "Number of Questions:" and a default value of 10.
3.  **Action Button:** A main button with the text "Create Practice Questions". While the process is running, the button should be activated and display the status "Compiling Questions...".
4.  **Output Area:**
    *   Title (H3): "Generated Practice Questions:"
    *   A single content area to display all questions.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `**bold**` and numbered lists) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users enter material, select the type and number of questions, then click a button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang ahli perancang kurikulum dan pembuat soal ujian yang sangat teliti.

    Berdasarkan materi pelajaran berikut:
    """
    [Teks dari input pengguna]
    """

    Tugas Anda adalah membuat [Jumlah dari input pengguna] soal latihan dengan tipe [Tipe dari pilihan pengguna]. Semua pertanyaan dan jawaban HARUS didasarkan HANYA pada informasi yang ada di dalam teks yang diberikan.

    Gunakan format Markdown yang ketat sebagai berikut:
    - **Untuk Pilihan Ganda:**
      1. Pertanyaan...
         A. Opsi A
         B. Opsi B
         C. Opsi C
         D. Opsi D
      **Jawaban: [Huruf Jawaban]**

    - **Untuk Esai:**
      1. Pertanyaan esai...

    - **Untuk Campuran:** Buat 5 soal Pilihan Ganda terlebih dahulu, diikuti oleh 5 soal Esai.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The application displays questions that have been formatted in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Fill in the "Paste Text or Study Material Here:" column with:**
`Photosynthesis is the process by which green plants and some other organisms convert light energy into chemical energy. During photosynthesis, plants use solar energy to convert carbon dioxide (CO2) and water (H2O) into glucose (sugar as food) and oxygen (O2) as byproducts. This process occurs in chloroplasts and relies heavily on chlorophyll, a green pigment that captures light energy.`
*   **Set the "Select Question Type:" option to:**
`Mixed (5 PG, 5 Essays)`
*   **Set "Number of Questions:" to:**
`10`
---
