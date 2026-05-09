# 📄 Chat with PDFs using Groq + FAISS

A Retrieval-Augmented Generation (RAG) based PDF Question Answering system built using Streamlit, FAISS, Sentence Transformers, and Groq LLM.

The application allows users to upload PDF documents, extract text, generate embeddings, perform semantic search using FAISS, and get intelligent answers from the uploaded documents.

---

# 🚀 Features

* Upload multiple PDF files
* Extract text from PDFs
* Automatic text chunking
* Semantic search using FAISS
* Local embeddings using Sentence Transformers
* AI-powered answers using Groq LLM
* Streamlit-based interactive UI

---

# 🛠️ Tech Stack

* Python
* Streamlit
* FAISS
* Sentence Transformers
* Groq API
* PyPDF2
* NumPy
* dotenv

---

# 📂 Project Structure

```bash
chat-with-pdfs/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/anuj-chendake/chat-with-pdfs.git
```

## 2️⃣ Move into Project Folder

```bash
cd chat-with-pdfs
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Environment Variables

Create a `.env` file in the root folder.

```env
GROQ_API_KEY=your_api_key_here
```

Get API Key from:

[https://console.groq.com/keys](https://console.groq.com/keys)

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

# 🧠 Working Flow

1. Upload PDF documents
2. Extract text from PDFs
3. Split text into chunks
4. Generate embeddings using Sentence Transformers
5. Store embeddings in FAISS vector database
6. Retrieve relevant chunks based on user query
7. Send retrieved context to Groq LLM
8. Generate intelligent answer

---

# 📸 Screenshots

Add screenshots of:

* PDF Upload UI
* Question Input
* Generated Answers
* Working Chat Interface

---

# 🔮 Future Improvements

* Chat history memory
* Conversational RAG
* Multi-user support
* Database integration
* Authentication system
* Deploy on Streamlit Cloud or Render
* Support for DOCX and TXT files

---

# 👨‍💻 Author

Anuj Chendake

GitHub:
[https://github.com/anuj-chendake](https://github.com/anuj-chendake)

---

# ⭐ If you like this project

Give this repository a star on GitHub.
