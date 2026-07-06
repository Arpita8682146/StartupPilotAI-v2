import streamlit as st
import fitz

st.title("StartupPilotAI")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text=""

    for page in pdf:

        text += page.get_text()

    st.success(
        "PDF processed successfully"
    )

    st.text_area(
        "Extracted Text",
        text,
        height=400
    )