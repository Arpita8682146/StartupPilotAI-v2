import streamlit as st
from upload_handler import process_pdf
from gemini_client import ask_gemini

st.image(
    "c:\\Users\\Arpita Singh\\Downloads\\logo.png",width=200
    
)
st.title("StartupPilotAI")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file is not None:

    text = process_pdf(uploaded_file)

    # Debugging
    st.write("Characters extracted:", len(text))
    st.text(text[:500])

    st.success("PDF processed successfully")

    question = st.text_input("Ask a question")

    if question:

        prompt = f"""
You are a helpful assistant.

Answer only from the information present in the PDF.

PDF Content:
{text}

Question:
{question}

Answer:
"""

        try:
            response = ask_gemini(prompt)

            st.subheader("Answer")
            st.write(response)

        except Exception as e:
            st.error(str(e))