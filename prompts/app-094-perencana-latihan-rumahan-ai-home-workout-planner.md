## Application Name
AI Home Workout Planner: Home Workout Planner

## Configuration & Attribution
*   **Target AI Model:** Gemini 2.5 Pro
*   **Creator:** yosedie

---

## Project Summary
Build a web application that functions as a personal fitness trainer. Users select the areas of the body they want to train, the equipment available, and fitness level, then the AI ​​will put together a simple and effective home workout routine, complete with descriptions of each move.

## User Interface Components (UI Components) (UI Components)

1.  **Header:** The big headline says "AI Home Workout Planner".
2.  **User Input Form:**
    *   **Target Area Selection:** A dropdown menu (select) with the label "Select Target Body Area:" and options: "Full Body", "Abs & Core", "Arms & Chest (Upper Body)", "Legs & Buttocks (Lower Body)".
    *   **Equipment Input:** A text input field labeled "Available Equipment (or 'no tools'):".
    *   **Fitness Level Selection:** A dropdown (select) menu with the label "Your Fitness Level:" and options: "Beginner", "Intermediate", "Advanced".
3.  **Action Button:** A main button with the text "Create a Workout Routine!". While the process is running, the button should be activated and display the status "Composing Workout...".
4.  **Output Area:**
    *   Title (H3): "Your Workout Routine Today:"
    *   A single content area to display the entire routine.
    *   **Copy Button:** There should be a "Copy Text" button next to the output area.
5.  **Footer:** A simple footer containing a link (hyperlink) with the text **'Created by yosedie'**. This link should point to the URL `https://github.com/yosedie` and open in a new tab.

## Content Rendering Requirements

*   **Render Markdown to HTML:** Applications **required** parse text responses from AI before displaying them in the UI. Use a JavaScript library such as `marked.js` or equivalent to convert all Markdown syntax (such as `##`, `**`, and `*`) into properly formatted HTML elements. Apply this rendering to the Output Area.

## Workflow & Logic (Workflow & Logic)

1.  Users select goals, equipment, and fitness level, then click the “Create Workout Routine!” button.
2.  The application creates a structured *prompt* to send to the AI ​​model.
    ```
    Anda adalah seorang pelatih kebugaran pribadi (personal trainer) bersertifikat. Anda ahli dalam merancang program latihan yang efektif dan aman untuk dilakukan di rumah.

    Berdasarkan kriteria pengguna berikut:
    - Target Area: [Target dari pilihan pengguna]
    - Peralatan: [Peralatan dari input pengguna]
    - Tingkat Kebugaran: [Tingkat dari pilihan pengguna]

    Tugas Anda adalah membuat satu rutinitas latihan yang lengkap. Rutinitas harus mencakup:
    1.  **Pemanasan (Warm-up):** 2-3 gerakan pemanasan ringan.
    2.  **Latihan Inti (Main Workout):** 4-6 gerakan latihan yang sesuai dengan target area, peralatan, dan tingkat kebugaran. Untuk setiap gerakan, sebutkan jumlah set dan repetisi yang direkomendasikan.
    3.  **Pendinginan (Cool-down):** 2-3 gerakan peregangan.

    Untuk setiap gerakan, berikan deskripsi singkat tentang cara melakukannya dengan benar. Gunakan format Markdown untuk menyusun rutinitas dengan rapi.
    ```
3.  The application sends this prompt to the **Gemini 2.5 Pro** model API.
4.  After receiving a response, the application renders the Markdown content of the response into HTML.
5.  The app displays workout routines in the Output Area.

---
## Quick Test Scenario (Quick Test Scenario)

**To allow live testing, autofill input fields with the following example data when the page first loads:**

*   **Set the "Select Target Body Area:" option to:**
`Abs & Core`
*   **Fill in the "Available Equipment..." column with:**
`No tools`
*   **Set the "Your Fitness Level:" option to:**
`Beginner`
---
