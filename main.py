# Importing necessary libraries
import streamlit as st
import cohere
from PyPDF2 import PdfReader
from docx import Document
from dotenv import load_dotenv
import time
import os

load_dotenv()

# Initialize Cohere client (use your API key here)
cohere_client = cohere.Client(os.environ["COHERE_API_KEY"])

# Streamlit App with Enhanced Chat Interface
def main():
    st.title("Legal Contract Analyzer (Enhanced Chat Interface)")
    st.write("Upload your document (PDF or DOCX) and interact with it conversationally.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a legal document", type=["pdf", "docx"])
    if uploaded_file:
        file_extension = uploaded_file.name.split('.')[-1].lower()

        # Text extraction based on file type with a loading indicator
        with st.spinner("Extracting text from document..."):
            time.sleep(1)  # Simulate processing time
            if file_extension == 'pdf':
                extracted_text = extract_text_from_pdf(uploaded_file)
            elif file_extension == 'docx':
                extracted_text = extract_text_from_docx(uploaded_file)
            else:
                st.error("Unsupported file format.")
                return

        # Store extracted text in session state
        if "document_text" not in st.session_state:
            st.session_state["document_text"] = extracted_text

        st.success("Document uploaded successfully! Generating the initial analysis...")

        # Initial analysis generation
        if "initial_analysis" not in st.session_state:
            with st.spinner("Generating initial analysis..."):
                time.sleep(1)  # Simulate processing time
                initial_response = cohere_client.generate(
                    model='command-xlarge',
                    prompt=(
                        f"You are a legal assistant. A user has uploaded a legal document. "
                        f"Please summarize and analyze the key points of the document:\n{st.session_state['document_text']}\n\n"
                        f"Provide a detailed initial analysis of the document."
                    ),
                    max_tokens=500,  # Increased max tokens for richer responses
                )
                initial_answer = initial_response.generations[0].text.strip()
                st.session_state["initial_analysis"] = initial_answer

        st.text_area("Initial Analysis:", value=st.session_state["initial_analysis"], disabled=True, height=300)

        # Chat interface
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = [("app", st.session_state["initial_analysis"])]

        # Display chat history
        for message in st.session_state["chat_history"]:
            role, content = message
            if role == "user":
                st.text_input("You:", value=content, disabled=True, key=f"user_{content}")
            else:
                st.text_area("App:", value=content, disabled=True, key=f"app_{content}")

        # User input
        user_input = st.text_input("Type your question or message here:")
        if st.button("Send"):
            if user_input.strip():
                # Append user input to chat history
                st.session_state["chat_history"].append(("user", user_input))

                # Generate response with a loading indicator
                with st.spinner("Generating response..."):
                    time.sleep(1)  # Simulate processing time
                    response = cohere_client.generate(
                        model='command-xlarge',
                        prompt=(
                            f"You are a legal assistant. A user has uploaded a document. "
                            f"Here's the document content:\n{st.session_state['document_text']}\n\n"
                            f"User's question: {user_input}\nAssistant's response:"
                        ),
                        max_tokens=500,  # Increased max tokens for richer responses
                    )
                    answer = response.generations[0].text.strip()

                # Append assistant response to chat history
                st.session_state["chat_history"].append(("app", answer))

                # Display the assistant's response
                st.text_area("App:", value=answer, disabled=True, key=f"app_response_{user_input}")

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