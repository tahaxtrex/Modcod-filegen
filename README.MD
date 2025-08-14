# 📄 Article Document Generator

This tool automatically generates Word documents for a list of articles provided in an Excel file.  
It uses a Word template to format each article and saves the results in an output folder.

---

## 🧠 What It Does

- Reads article data from: `input/articles.xlsx`
- Loads a Word template: `input/document_template.docx`
- For each article:
  - Creates a formatted `.docx` file
  - Includes the article number and designation
- Saves all generated files into a folder named `output/`

---

## 🖥️ How to Use

1. **Make sure the folder contains:**

   main.exe

   input/

   ├── articles.xlsx

   └── document_template.docx

2. **Double-click `main.exe` to run the tool.**

- A console window will appear showing the progress.
- Generated documents will be saved in the `output/` folder.

---

## 📦 Files & Folders

| Name                     | Description                                |
| ------------------------ | ------------------------------------------ |
| `main.exe`               | Executable file (double-click to run)      |
| `input/`                 | Folder containing required input files     |
| `articles.xlsx`          | Excel sheet with article data              |
| `document_template.docx` | Word template used for formatting          |
| `output/` (auto)         | Folder created for the generated documents |

---

## 🛡️ Antivirus Warning (If Any)

This file was generated using [PyInstaller](https://www.pyinstaller.org/), a tool that bundles Python code into a Windows executable.

> ⚠️ Some antivirus programs may mistakenly flag this `.exe` as suspicious because it is unsigned and self-contained.  
> It contains no malicious code and is safe to use.

If you're unsure:

- Scan it with your antivirus manually
- Or upload it to [https://www.virustotal.com](https://www.virustotal.com) to verify

---

## 📞 Need Help?

If you run into problems or need help:

- Contact: **[hbirritaha@gmail.com]**
- Or report issues via [linkedin](https://www.linkedin.com/in/tahahbirri/)

---

## ✅ Example Output

All generated documents will look like:

output/

├── 001 - Widget A.docx

├── 002 - Widget B.docx

├── ...

---

## 🧩 Requirements (for developers only)

This tool was built using:

- Python 3.x
- `pandas`, `openpyxl`, `docxtpl`

To modify the script or rebuild the `.exe`, install the dependencies:

```bash
pip install pandas openpyxl docxtpl
pyinstaller --onefile --add-data "input;input" main.py
```
