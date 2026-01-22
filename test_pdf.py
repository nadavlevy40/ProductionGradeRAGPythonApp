import pdfplumber

pdf_path = "contract.pdf"  # Make sure this matches your file name

print(f"--- TESTING: {pdf_path} ---")
try:
    with pdfplumber.open(pdf_path) as pdf:
        total_text = ""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            print(f"Page {i+1} extraction result: {'SUCCESS (Text found)' if text else 'FAILED (Empty)'}")
            if text:
                print(f"Snippet: {text[:100]}...") # Print first 100 chars
                total_text += text
                
    if not total_text.strip():
        print("\n❌ RESULT: No text found. This PDF is likely a scanned image.")
    else:
        print(f"\n✅ RESULT: Text found! Total characters: {len(total_text)}")

except Exception as e:
    print(f"\n❌ ERROR: Could not read PDF. Reason: {e}")