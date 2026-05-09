import streamlit as st
import numpy as np
import faiss
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
import os

# ================= LOAD ENV =================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# ================= LOAD EMBEDDING MODEL =================

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ================= PDF TEXT EXTRACTION =================

def get_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:

            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text

    return text


# ================= TEXT CHUNKING =================

def get_text_chunks(text, chunk_size=1000, overlap=200):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ================= CREATE EMBEDDINGS =================

def get_embeddings(text_chunks):

    embeddings = embedding_model.encode(text_chunks)

    return np.array(embeddings).astype("float32")


# ================= CREATE FAISS INDEX =================

def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


# ================= RETRIEVE CONTEXT =================

def retrieve_context(question, index, text_chunks):

    question_embedding = embedding_model.encode([question])

    question_embedding = np.array(question_embedding).astype("float32")

    distances, indices = index.search(question_embedding, k=3)

    retrieved_chunks = []

    for idx in indices[0]:

        retrieved_chunks.append(text_chunks[idx])

    return "\n".join(retrieved_chunks)


# ================= GENERATE ANSWER =================

def generate_answer(question, context):

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful PDF assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# ================= STREAMLIT UI =================

st.set_page_config(page_title="Chat with PDFs")

st.title("📄 Chat with PDFs using Groq + FAISS")

pdf_docs = st.file_uploader(
    "Upload PDF Files",
    accept_multiple_files=True
)

if pdf_docs:

    with st.spinner("Processing PDFs..."):

        raw_text = get_pdf_text(pdf_docs)

        text_chunks = get_text_chunks(raw_text)

        embeddings = get_embeddings(text_chunks)

        index = create_faiss_index(embeddings)

    st.success("PDFs Processed Successfully!")

    question = st.text_input("Ask a question from PDFs")

    if question:

        with st.spinner("Generating Answer..."):

            context = retrieve_context(
                question,
                index,
                text_chunks
            )

            answer = generate_answer(
                question,
                context
            )

        st.write("### Answer")
        st.write(answer)


        #streamlit run app.py