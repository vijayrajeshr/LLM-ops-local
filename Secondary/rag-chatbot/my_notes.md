
# 📄 Local RAG Chatbot with Llama 3.2

This is a private, local **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **LangChain**, and **Ollama**. It allows you to upload PDF documents and have a conversation with them. Since it runs entirely on your local machine, your data never leaves your system.

## 🌟 Key Features

- **Privacy-First:** Powered by Llama 3.2 via Ollama; no cloud APIs required.
    
- **PDF Intelligence:** Analyzes uploaded documents and provides context-aware answers.
    
- **Session Memory:** Remembers your questions within the same session using Streamlit Session State.
    
- **Fast Retrieval:** Uses `nomic-embed-text` for highly efficient mathematical indexing.
    

## 🛠️ Tech Stack

- **UI:** Streamlit
    
- **LLM:** Llama 3.2 (Local via Ollama)
    
- **Orchestration:** LangChain
    
- **Vector Database:** ChromaDB
    
- **Embeddings:** Nomic Embed Text
    

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have [Ollama](https://ollama.com/) installed and running. Pull the required models:

Bash

```
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 2. Installation

Clone the repository and install the dependencies:

Bash

```
pip install -r requirements.txt
```

### 3. Run the App

Bash

```
streamlit run app.py
```

## 🧠 How It Works (The RAG Pipeline)

1. **Ingest:** Reads the PDF using `PyPDFLoader`.
    
2. **Chunk:** Chops text into 1000-character segments with `RecursiveCharacterTextSplitter` to fit the LLM's memory.
    
3. **Embed:** Converts chunks into numerical vectors using `OllamaEmbeddings`.
    
4. **Store:** Saves vectors in `ChromaDB` for instant searching.
    
5. **Retrieve:** When you ask a question, the system finds the most relevant chunks.
    
6. **Generate:** Sends the context and question to Llama 3.2 to produce a grounded answer.
    

## ☁️ Deployment Note

This project includes a `pysqlite3` fix in `app.py` to ensure compatibility with **Streamlit Community Cloud**. However, as the LLM is local, a cloud-based API (like Groq) is recommended for public showcases.