# Importing necessary libraries
import streamlit as st
import cohere
from PyPDF2 import PdfReader
from docx import Document

# Initialize Cohere client (use your API key here)
COHERE_API_KEY = "your-cohere-api-key"  # Replace with your actual API key
cohere_client = cohere.Client(COHERE_API_KEY)

# Streamlit App
def main():
    st.title("Legal Contract Analyzer (Prototype)")
    st.write("Upload your document (PDF or DOCX), and get a summary with detailed explanations.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a legal document", type=["pdf", "docx"])
    if uploaded_file:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        # Text extraction based on file type
        if file_extension == 'pdf':
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif file_extension == 'docx':
            extracted_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format.")
            return

        # Display extracted text
        st.subheader("Extracted Text:")
        st.write(extracted_text)

        # Summarize and explain using Cohere
        if st.button("Analyze with LLM"):
            response = cohere_client.generate(
                model='command-xlarge',
                prompt=f"Summarize and explain this legal document:\n{extracted_text}",
                max_tokens=300
            )
            st.subheader("Analysis:")
            st.write(response.generations[0].text)

# Helper functions for text extraction
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    document = Document(docx_file)
    text = "\n".join([paragraph.text for paragraph in document.paragraphs])
    return text

if __name__ == "__main__":
    main()