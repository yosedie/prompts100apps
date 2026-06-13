import csv
import os

# Paths configuration
csv_file_path = "dataset_apps.csv"
readme_file_path = "README.md"

# Beautiful README Header Template
readme_header = """# 🚀 100+ AI-Powered Web Applications Portfolio

Welcome to my portfolio! This repository showcases a comprehensive collection of **101 web-based applications** systematically designed, prompted, and evaluated using **Google AI Studio**. 

This project demonstrates proficiency in:
- ✍️ **Advanced Prompt Engineering**: Multi-turn prompts, system instructions, and structured output formatting.
- ⚙️ **LLM Orchestration**: Designing applications powered by Gemini models (specifically Gemini 2.5 Pro and Flash).
- 🛠️ **Rapid Prototyping & Product Design**: Transforming raw ideas into interactive, functional web apps.

---

## 📊 Application Index

Below is the complete list of the 101 generated applications, along with descriptions and direct launch links.

| No | Application Name | Description | Direct Link |
|:---:|:---|:---|:---:|
"""

readme_footer = """
---

## 🚀 How to Launch an App

1. Find an application you are interested in from the index table above.
2. Click the **[Launch App 🌐]** link in the "Direct Link" column.
3. The application will open directly in Google AI Studio, allowing you to test, review, and fork it.

*Created as part of the Prompt Engineering Portfolio.*
"""

try:
    readme_content = readme_header
    
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for index, row in enumerate(reader, start=1):
            name = row.get('Nama_Aplikasi', f'AI App {index}')
            description = row.get('Deskripsi', 'No description provided.')
            link = row.get('Link_Drive', '#')
            
            # Escape pipes (|) in name and description to prevent breaking markdown tables
            description = description.replace('|', '\\|')
            name = name.replace('|', '\\|')
            
            readme_content += f"| {index} | **{name}** | {description} | [Launch App 🌐]({link}) |\n"

    readme_content += readme_footer

    with open(readme_file_path, mode='w', encoding='utf-8') as file:
        file.write(readme_content)
        
    print("🔥 BOOM! README.md has been successfully generated with 101 applications!")

except Exception as e:
    print(f"Error: {e}. Please ensure dataset_apps.csv exists and contains columns: Nama_Aplikasi, Deskripsi, Link_Drive.")
