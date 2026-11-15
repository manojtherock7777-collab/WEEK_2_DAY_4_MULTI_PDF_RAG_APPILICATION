
# ============================================================
# MULTI-PDF RAG APPLICATION
# Using LangChain + Streamlit + FAISS + OpenAI
# ============================================================


# ------------------------------------------------------------
# STEP 1: IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import os
import tempfile
import streamlit as st

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate


# ------------------------------------------------------------
# STEP 2: LOAD ENVIRONMENT VARIABLES
# ------------------------------------------------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# ------------------------------------------------------------
# STEP 3: STREAMLIT PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Multi-PDF RAG Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Multi-PDF RAG Assistant")

st.write(
    "Upload multiple PDF documents and ask questions "
    "across all documents using Retrieval Augmented Generation."
)


# ------------------------------------------------------------
# STEP 4: INITIALIZE SESSION STATE
# ------------------------------------------------------------

if "vector_store" not in st.session_state:

    st.session_state.vector_store = None


if "chunk_count" not in st.session_state:

    st.session_state.chunk_count = 0


# ------------------------------------------------------------
# STEP 5: CHECK OPENAI API KEY
# ------------------------------------------------------------

if not OPENAI_API_KEY:

    st.error(
        "OpenAI API key not found. "
        "Please check your .env file."
    )

    st.stop()


# ------------------------------------------------------------
# STEP 6: INITIALIZE OPENAI MODELS
# ------------------------------------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY
)


# ------------------------------------------------------------
# STEP 7: INITIAL SUCCESS MESSAGE
# ------------------------------------------------------------

st.success("RAG application initialized successfully!")

# STEP 10: MULTIPLE PDF UPLOAD

st.subheader("1. Upload PDF Documents")

uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.write("Uploaded PDF Documents:")

    for file in uploaded_files:

        st.write("📄", file.name)

  # STEP 10.5: EXTRACT TEXT FROM ALL PDFS

if uploaded_files:

    all_documents = []

    for uploaded_file in uploaded_files:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(uploaded_file.getvalue())

            temp_path = temp_file.name

        try:

            loader = PyPDFLoader(temp_path)

            documents = loader.load()

            for document in documents:

                document.metadata["source"] = uploaded_file.name

            all_documents.extend(documents)

        finally:

            os.remove(temp_path)

    st.success(
        f"Successfully extracted {len(all_documents)} pages "
        f"from {len(uploaded_files)} PDF files."
    )
    # STEP 11: TEXT CHUNKING

st.subheader("2. Split Documents into Chunks")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(all_documents)

st.success(
    f"Successfully created {len(chunks)} text chunks "
    f"from {len(all_documents)} pages."
)
# STEP 12: CREATE FAISS VECTOR DATABASE

st.subheader("3. Create Vector Database")

if st.button("Build Vector Database"):

    with st.spinner("Generating embeddings and creating FAISS database..."):

        vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings
        )

        st.session_state.vector_store = vector_store

        st.session_state.chunk_count = len(chunks)

    st.success("FAISS Vector Database created successfully!")

    st.metric(
        "Total Indexed Chunks",
        st.session_state.chunk_count
    )
    
# ------------------------------------------------------------
# STEP 13: QUESTION ANSWERING
# ------------------------------------------------------------

if st.session_state.vector_store is not None:

    st.divider()

    st.subheader("4. Ask Questions Across PDFs")

    question = st.text_input(
        "Enter your question:",
        placeholder="What are the major threats to wildlife?"
    )

    if st.button("Get Answer"):

        if not question.strip():

            st.warning("Please enter a question.")

        else:

            with st.spinner("Searching documents..."):

                # Retrieve relevant chunks from FAISS
                retrieved_docs = (
                    st.session_state.vector_store
                    .similarity_search(
                        question,
                        k=4
                    )
                )

                # Prepare retrieved context
                context = "\n\n".join(
                    [
                        doc.page_content
                        for doc in retrieved_docs
                    ]
                )

                # Create RAG prompt
                prompt = ChatPromptTemplate.from_messages([

                    (
                        "system",
                        """
                        You are a helpful PDF question-answering assistant.

                        Answer the user's question using ONLY
                        the retrieved document context.

                        Rules:
                        1. Do not invent information.
                        2. If the answer is not available,
                           say you cannot find it in the documents.
                        3. Explain in simple language.
                        """
                    ),

                    (
                        "human",
                        """
                        Context:
                        {context}

                        Question:
                        {question}

                        Answer:
                        """
                    )

                ])

                # Connect prompt with GPT-4o-mini
                chain = prompt | llm

                response = chain.invoke({

                    "context": context,

                    "question": question

                })

                # Display answer
                st.subheader("Answer")

                st.write(response.content)

                # ------------------------------------------------
                # STEP 14: DISPLAY SOURCE FILE AND PAGE NUMBER
                # ------------------------------------------------

                st.subheader("Sources")

                sources = []

                for doc in retrieved_docs:

                    filename = doc.metadata.get(
                        "source",
                        "Unknown file"
                    )

                    page_number = int(
                        doc.metadata.get("page", 0)
                    ) + 1

                    source = {
                        "filename": filename,
                        "page": page_number
                    }

                    if source not in sources:

                        sources.append(source)

                for source in sources:

                    st.info(
                        f"📄 File: {source['filename']} "
                        f"| Page: {source['page']}"
                    )

# ============================================================
# END OF CURRENT DEVELOPMENT STAGE
# ============================================================
