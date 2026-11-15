# 📚 Multi-PDF RAG Assistant using LangChain, Streamlit & FAISS

## 🚀 Project Overview

The **Multi-PDF RAG Assistant** is an AI-powered document question-answering application built using Python, LangChain, Streamlit, FAISS, and OpenAI.

It allows users to upload multiple PDF documents simultaneously, extract their content, split the text into smaller chunks, generate embeddings, and store all document vectors in a single FAISS vector database.

Users can then ask questions across all uploaded documents and receive AI-generated answers with source references, including the original PDF filename and page number.

The application uses **Retrieval-Augmented Generation (RAG)** to provide context-aware answers based on the uploaded documents.

## 🎯 Problem Statement

Reading and searching through multiple PDF documents manually can be time-consuming.

This project solves that problem by providing a centralized AI-powered document assistant that:

- Accepts multiple PDF documents in one upload.
- Extracts text from all uploaded PDFs.
- Splits extracted text into manageable chunks.
- Converts chunks into numerical embeddings.
- Stores all embeddings in a single FAISS vector database.
- Retrieves relevant information based on user questions.
- Generates answers using OpenAI GPT-4o-mini.
- Displays source PDF filenames and page numbers for verification.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Programming language |
| Streamlit | Web application interface |
| LangChain | RAG application framework |
| PyPDFLoader | PDF text extraction |
| RecursiveCharacterTextSplitter | Text chunking |
| OpenAI Embeddings | Text-to-vector conversion |
| text-embedding-3-small | Embedding model |
| FAISS | Vector database |
| ChatOpenAI | LLM integration |
| GPT-4o-mini | Answer generation |
| python-dotenv | Environment variable management |

## 🏗️ Application Architecture

The application follows this workflow:

```text
             Multiple PDF Upload
                     |
                     v
              Streamlit UI
                     |
                     v
                PyPDFLoader
                     |
                     v
              Text Extraction
                     |
                     v
             Text Chunking
                     |
                     v
       RecursiveCharacterTextSplitter
                     |
                     v
             OpenAI Embeddings
                     |
                     v
              Vector Creation
                     |
                     v
              FAISS Database
                     |
                     v
              User Question
                     |
                     v
            Similarity Search
                     |
                     v
          Retrieve Relevant Chunks
                     |
                     v
                GPT-4o-mini
                     |
                     v
             Generated Answer
                     |
                     v
            Source File + Page
```

## 📂 Project Structure

```text
MULTI_PDF_RAG_APP/
│
├── venv/
│
├── rag_app.py
│
├── requirements.txt
│
├── .env
│
└── README.md
```

**File Descriptions:**

- `rag_app.py` – Complete application code.
- `requirements.txt` – Required Python dependencies.
- `.env` – Stores the OpenAI API key.
- `README.md` – Project documentation.
- `venv/` – Python virtual environment.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project folder:

```bash
cd MULTI_PDF_RAG_APP
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows CMD:

```cmd
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure OpenAI API Key

Create a `.env` file in the project root directory.

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Note:** Keep your API key private. Never upload the `.env` file to GitHub.

### 6. Run the Application

Execute:

```bash
streamlit run rag_app.py
```

The application will open in your browser.

Default local address:

```text
http://localhost:8501
```

## 📦 Requirements

The `requirements.txt` file contains:

```text
streamlit
langchain
langchain-community
langchain-openai
langchain-text-splitters
faiss-cpu
pypdf
python-dotenv
```

## 🔍 Application Features

### 1. Multiple PDF Upload

- Upload multiple PDF files simultaneously.
- Supports multiple documents in a single session.
- Displays uploaded PDF filenames.

### 2. PDF Text Extraction

- Uses LangChain's PyPDFLoader.
- Extracts PDF content page by page.
- Preserves source filename and page metadata.

### 3. Text Chunking

Uses `RecursiveCharacterTextSplitter`.

Configuration:

```python
chunk_size=1000
chunk_overlap=150
```

This divides large PDF documents into smaller text segments while maintaining contextual overlap.

### 4. Embedding Generation

Uses OpenAI's embedding model:

```python
OpenAIEmbeddings(
    model="text-embedding-3-small"
)
```

Converts text chunks into numerical vector representations.

### 5. FAISS Vector Database

Uses FAISS to store and search document embeddings.

```python
FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)
```

All uploaded PDF chunks are combined into one vector database.

The application also displays the total number of indexed chunks.

### 6. AI-Powered Question Answering

Uses OpenAI GPT-4o-mini:

```python
ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

The application retrieves relevant document chunks using similarity search and passes the retrieved context to the LLM.

### 7. Source Tracking

Every answer is accompanied by source information extracted from chunk metadata.

Source information includes:

- Original PDF filename.
- PDF page number.

This helps users verify the information against the original documents.

## 🧪 Sample Execution

For testing, three wildlife-related PDF documents were uploaded.

**Uploaded Documents:**

1. WILDLIFE ISSUES AND CHALLENGES.pdf
2. AS-302 Wildlife and Conservation Biology.pdf
3. Wildlife-AnIntroduction.pdf

**Processing Results:**

| Processing Stage | Result |
|---|---:|
| PDF Documents Uploaded | 3 |
| Total Pages Extracted | 248 |
| Text Chunks Created | 447 |
| Indexed Chunks | 447 |
| Retrieved Chunks per Question | 4 |

### Sample Question

```text
What are the major threats to wildlife?
```

### Sample Answer

The application generated an answer identifying habitat loss, destruction, fragmentation, and degradation as major threats to wildlife.

It also identified human activities such as:

- Felling of trees.
- Dredging rivers.
- Constructing dams.
- Filling wetlands.
- Using land for agriculture.
- Construction of buildings and infrastructure.

### Source References

The application returned relevant source references from the uploaded documents, including:

- WILDLIFE ISSUES AND CHALLENGES.pdf — Page 1
- AS-302 Wildlife and Conservation Biology.pdf — Page 1
- AS-302 Wildlife and Conservation Biology.pdf — Page 60
- WILDLIFE ISSUES AND CHALLENGES.pdf — Page 2

## 🧠 Key Concepts Learned

Through this project, the following concepts were implemented:

1. Retrieval-Augmented Generation (RAG).
2. Multiple PDF document processing.
3. Document loading using LangChain.
4. Text splitting and chunk overlap.
5. Vector embeddings.
6. FAISS vector database.
7. Semantic similarity search.
8. Prompt engineering.
9. LLM integration using GPT-4o-mini.
10. Source metadata and page tracking.
11. Streamlit session state.
12. Environment variable management.

## 🔐 Security Notes

- Store API keys in environment variables.
- Never commit `.env` to GitHub.
- Add `.env` and `venv/` to `.gitignore`.
- Do not expose API keys in source code or screenshots.

## ⚠️ Current Limitations

- Requires an OpenAI API key and API usage billing.
- Supports text extraction from readable PDFs; scanned PDFs may require OCR.
- FAISS database is maintained in Streamlit session state and is not permanently persisted.
- Large PDF collections may require additional processing time and API usage.
- The current implementation retrieves the top four chunks for each question.

## 🚀 Future Enhancements

Potential improvements include:

- Persistent FAISS database storage.
- Chat history and conversational memory.
- Better source citations directly inside generated answers.
- OCR support for scanned PDFs.
- Advanced document filtering.
- Configurable chunk size and retrieval count.
- Improved document management.
- Downloadable question-answer reports.

## 👨‍💻 Author

**Developed as a hands-on Generative AI and LangChain project.**

### Project Title

**Multi-PDF RAG Assistant using LangChain, Streamlit, FAISS and OpenAI**

---

⭐ If you find this project useful, consider giving the repository a star!
