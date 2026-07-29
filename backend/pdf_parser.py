import os
from pypdf import PdfReader

# Folder containing PDF manuals
MANUALS_FOLDER = "manuals"

# Folder where extracted text will be saved
OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Get all PDF files
pdf_files = [file for file in os.listdir(MANUALS_FOLDER) if file.endswith(".pdf")]

# Statistics
total_pdfs = len(pdf_files)
total_pages = 0

print("=" * 60)
print("PDF PARSING STARTED")
print("=" * 60)

# Process each PDF
for pdf in pdf_files:

    pdf_path = os.path.join(MANUALS_FOLDER, pdf)

    print(f"\nReading: {pdf}")

    reader = PdfReader(pdf_path)

    pages = len(reader.pages)
    total_pages += pages

    print(f"Pages: {pages}")

    extracted_text = ""

    # Read every page
    for page in reader.pages:
        text = page.extract_text()

        if text:
            extracted_text += text + "\n"

    # Save text file
    txt_name = pdf.replace(".pdf", ".txt")
    txt_path = os.path.join(OUTPUT_FOLDER, txt_name)

    with open(txt_path, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print(f"Saved: {txt_name}")
    print(f"Characters Extracted: {len(extracted_text)}")
    print("-" * 60)

print("\n" + "=" * 60)
print("PDF PARSING COMPLETED")
print("=" * 60)
print(f"Total PDFs Processed : {total_pdfs}")
print(f"Total Pages Read     : {total_pages}")
print(f"Output Folder        : {OUTPUT_FOLDER}")
print("=" * 60)