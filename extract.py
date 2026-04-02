import os
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path, txt_path):
    print(f"Extracting {pdf_path} to {txt_path}...")
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n\n"
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extraction successful for {pdf_path}")
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")

pdfs = [
    r"c:\Users\w196818\work\Office\parsec-x-rules\parsecX_rules.pdf",
    r"c:\Users\w196818\work\Office\parsec-x-rules\parsecX_cards.pdf",
    r"c:\Users\w196818\work\Office\twilight-empire-rules\TwilightImperium4thEd_v1.pdf",
    r"c:\Users\w196818\work\Office\twilight-empire-rules\ti-k0289_rules_referencecompressed.pdf",
    r"c:\Users\w196818\work\Office\twilight-empire-rules\TI4_Factions_Overview_&_Strategy_Guide_(display).pdf",
    r"c:\Users\w196818\work\Office\twilight-empire-rules\TI_Objective_Cards.pdf"
]

for pdf in pdfs:
    txt = pdf.replace(".pdf", ".txt")
    extract_text_from_pdf(pdf, txt)
