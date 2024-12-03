# 📝 Legal Contract Analyzer

An AI-powered application to help users analyze, summarize, and interact with legal documents such as NDAs, contracts, employment letters, land leases, and rent agreements. Built using **Cohere's LLM API** and **Streamlit** for a quick, responsive, and interactive user experience.

## 🚀 Features
- **Document Upload**: Upload PDF or DOCX legal documents for analysis.
- **Initial Analysis**: Automatically generates a detailed summary and analysis of the uploaded document.
- **Conversational Chat Interface**: Users can engage in a back-and-forth conversation with the app to clarify, explore, or ask questions about the document.
- **Grounded Responses**: All responses are grounded in the content of the uploaded document, ensuring accuracy and relevance.
- **General Conversations**: Handles conversations outside the document's scope while referencing the uploaded document for clarification when needed.
- **User-Friendly Design**: Simple and intuitive interface built with Streamlit, including loading indicators for better user experience.

## 📂 Project Structure
```
.
├── main.py  # Main application file
├── README.md                              # Project documentation
├── requirements.txt                       # List of dependencies
```

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/legal-contract-analyzer.git
   cd legal-contract-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run main.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

## 🔑 Setup Cohere API Key
To use the app, you need a **Cohere API Key**:
1. Sign up at [Cohere](https://cohere.com/) and get your API key.
2. Replace the placeholder in the script (`your-cohere-api-key`) with your actual API key.

## 🎥 How It Works
1. **Upload a Document**: Upload a PDF or DOCX legal document.
2. **Get an Initial Analysis**: The app processes the document and provides a detailed summary.
3. **Start a Conversation**: Use the chat interface to ask questions, clarify details, or discuss the document.

## 📋 Dependencies
- `streamlit`: For building the web interface.
- `cohere`: For natural language processing.
- `PyPDF2`: For extracting text from PDF documents.
- `python-docx`: For extracting text from DOCX files.

Install them using:
```bash
pip install -r requirements.txt
```

## 📦 Example Use Cases
- **Reviewing NDAs**: Get a detailed analysis of non-disclosure agreements.
- **Exploring Employment Contracts**: Understand key clauses and terms.
- **Analyzing Rent Agreements**: Clarify rights, obligations, and legal terms.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork.
4. Create a pull request.

## 🛡️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments
- **Cohere**: For the language model powering the app.
- **Streamlit**: For the rapid web app development framework.
