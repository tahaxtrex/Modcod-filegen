import os
import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime
import sys

# === CONFIGURATION ===
EXCEL_FILE = "./input/articles.xlsx"
TEMPLATE_FILE = "./input/document_template.docx"
OUTPUT_FOLDER = "output"


def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


def validate_files():
    missing = []
    if not os.path.isfile(EXCEL_FILE):
        missing.append(EXCEL_FILE)
    if not os.path.isfile(TEMPLATE_FILE):
        missing.append(TEMPLATE_FILE)
    if missing:
        log(f"❌ Missing required file(s): {', '.join(missing)}")
        sys.exit(1)


def load_data():
    try:
        df = pd.read_excel(EXCEL_FILE, header=None)
        df = df.iloc[2:]  # Skip headers
        df.columns = ['Article', 'Designation', 'Unite', 'Qte', 'P_Unit', 'P_Total']
        df = df[df['Article'].notna()]
        df = df[df['Article'].astype(str).str.strip().apply(lambda x: x[0].isdigit())]
        return df
    except Exception as e:
        log(f"❌ Failed to load Excel: {e}")
        sys.exit(1)


def sanitize_filename(name: str) -> str:
    return name.replace("/", "-").replace("\\", "-").strip()


def generate_documents(df):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    count = 0

    for _, row in df.iterrows():
        article_no = str(row['Article']).strip()
        designation = str(row['Designation']).strip()
        context = {
            'article_number': f"Prix n° : {article_no} — {designation}"
        }

        try:
            tpl = DocxTemplate(TEMPLATE_FILE)
            tpl.render(context)

            safe_name = sanitize_filename(f"{article_no} - {designation[:50]}")
            output_path = os.path.join(OUTPUT_FOLDER, f"{safe_name}.docx")
            tpl.save(output_path)
            log(f"✅ Generated: {output_path}")
            count += 1
        except Exception as e:
            log(f"⚠️ Failed to generate doc for article {article_no}: {e}")

    return count


def main():
    log("📄 Starting Document Generator...")
    validate_files()
    df = load_data()
    total = generate_documents(df)
    log(f"🏁 Done! {total} documents generated in /{OUTPUT_FOLDER}")


if __name__ == "__main__":
    main()
