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
| text-embedding-3-small | Embedding