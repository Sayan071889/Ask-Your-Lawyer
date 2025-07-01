# Ask-Your-Lawyer

An intelligent legal assistant powered by Retrieval-Augmented Generation (RAG) that helps answer legal questions based on uploaded PDF documents. Built with LangChain, Streamlit, and powered by DeepSeek R1 via Groq API.

## 🚀 Features

- **PDF Document Processing**: Upload and process legal documents (PDFs) for analysis
- **Intelligent Q&A**: Ask natural language questions about legal documents
- **RAG Pipeline**: Uses vector embeddings and similarity search for accurate context retrieval
- **Web Interface**: Clean, user-friendly Streamlit interface
- **Advanced LLM**: Powered by DeepSeek R1 Distill Llama 70B model via Groq API

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **LLM**: DeepSeek R1 Distill Llama 70B (via Groq API)
- **Embeddings**: HuggingFace all-MiniLM-L6-v2
- **Vector Database**: FAISS
- **Document Processing**: PDFPlumber, PyMuPDF
- **Framework**: LangChain

## 📋 Prerequisites

- Python 3.7+
- Groq API Key ([Get one here](https://console.groq.com/))
- Google Colab (recommended) or local Python environment

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-lawyer.git
   cd ai-lawyer
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pymupdf langchain langchain-community langchain-core langchain-groq faiss-cpu pdfplumber langchain-huggingface
   ```

3. **Set up environment variables**
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   ```
   Or add it directly in the code where indicated.

4. **Create necessary directories**
   ```bash
   mkdir pdfs vectorstore
   ```

## 🚀 Usage

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Access the application**
   - Open your browser and go to `http://localhost:8501`
   - Upload a PDF document (legal document, contract, etc.)
   - Ask questions about the document content

### Example Questions

- "What are the key clauses in this contract?"
- "If a government forbids the right to assemble peacefully, which articles are violated and why?"
- "What are the penalties mentioned for breach of contract?"
- "Summarize the main points of this legal document"

## 📁 Project Structure

```
ai-lawyer/
├── ai_lawyer_code.py    # Main logic and RAG pipeline
├── app.py              # Streamlit frontend
├── pdfs/               # Directory for uploaded PDFs
├── vectorstore/        # FAISS vector database storage
└── README.md          # This file
```

## 🔍 How It Works

1. **Document Processing**: PDFs are loaded and split into chunks for better processing
2. **Embedding Creation**: Text chunks are converted to vector embeddings using HuggingFace models
3. **Vector Storage**: Embeddings are stored in FAISS vector database for fast similarity search
4. **Query Processing**: User questions are embedded and matched against document chunks
5. **Answer Generation**: Retrieved context is sent to DeepSeek R1 model for intelligent response generation

## ⚙️ Configuration

### Customizing Chunk Size
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,      # Adjust based on your needs
    chunk_overlap = 200,    # Overlap between chunks
    add_start_index = True
)
```

### Changing Embedding Model
```python
huggingface_model_name = "all-MiniLM-L6-v2"  # Or use other HuggingFace models
```

## 🔒 Security & Privacy

- Documents are processed locally and not stored permanently
- API calls to Groq are made securely with your API key
- No document content is shared beyond the processing pipeline

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This tool is for informational purposes only and should not be considered as professional legal advice. Always consult with qualified legal professionals for important legal matters.

## 🐛 Known Issues

- Large PDF files may take longer to process
- Context window limitations may affect very long documents
- Requires stable internet connection for Groq API calls

## 🔮 Future Enhancements

- [ ] Support for multiple document formats (DOCX, TXT)
- [ ] Conversation history and memory
- [ ] Document comparison features
- [ ] Export functionality for Q&A sessions
- [ ] Batch processing for multiple documents
- [ ] Enhanced UI with document preview

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/yourusername/ai-lawyer/issues) section
2. Create a new issue with detailed description
3. Contact the maintainer

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the RAG framework
- [Streamlit](https://streamlit.io/) for the web interface
- [Groq](https://groq.com/) for high-speed LLM inference
- [HuggingFace](https://huggingface.co/) for embedding models
- [FAISS](https://github.com/facebookresearch/faiss) for vector similarity search

---
