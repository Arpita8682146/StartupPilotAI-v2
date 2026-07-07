import fitz
def load_pdf(uploaded_file):
    """
    Loads text page-by-page from an uploaded PDF file object.
    Returns:
        List of dicts: [{'text': str, 'page': int, 'source': str}]
    """
    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )
    pages_data = []
    filename = getattr(uploaded_file, "name", "uploaded_document.pdf")
    
    for page_num, page in enumerate(pdf, start=1):
        text = page.get_text()
        if text.strip():
            pages_data.append({
                "text": text,
                "page": page_num,
                "source": filename
            })
            
    pdf.close()
    return pages_data