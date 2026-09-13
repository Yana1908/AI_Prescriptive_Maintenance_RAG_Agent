# 🤖 AI Prescriptive Maintenance Assistant

An AI-powered **Retrieval-Augmented Generation (RAG)** based application designed to help users quickly retrieve relevant information from industrial maintenance manuals using **semantic search, Sentence Transformers, and FAISS**.

---

## 📌 Project Overview

The **AI Prescriptive Maintenance Assistant** is an intelligent maintenance-support system that reduces the effort required to manually search through large industrial maintenance manuals.

Users can enter a maintenance-related question, and the system converts the query into a vector representation and performs semantic similarity search against information extracted from industrial PDF manuals.

The most relevant manual sections are retrieved and displayed through an interactive **Streamlit dashboard**.

### Example Query

> **How to troubleshoot ABB ACS550 drive?**

The system searches the available industrial maintenance knowledge base and retrieves the most relevant manual sections.

---

## 🎯 Objectives

The main objectives of this project are:

- Extract information from industrial maintenance PDF manuals.
- Clean and preprocess extracted text.
- Divide large documents into smaller chunks.
- Generate vector embeddings for document chunks.
- Store embeddings in a FAISS vector index.
- Convert user queries into vector embeddings.
- Perform semantic similarity search.
- Retrieve the most relevant Top-K results.
- Display retrieved information through an interactive dashboard.
- Provide similarity scores and confidence indicators.
- Provide a FastAPI backend for search operations.

---

# 🏗️ System Architecture

```text
                 INDUSTRIAL PDF MANUALS
                           │
                           ▼
                  PDF TEXT EXTRACTION
                           │
                           ▼
                    TEXT CLEANING
                           │
                           ▼
                     TEXT CHUNKING
                           │
                           ▼
               SENTENCE TRANSFORMER
                           │
                           ▼
                  VECTOR EMBEDDINGS
                           │
                           ▼
                    FAISS INDEX
                           │
                           │
                           │
                    USER QUERY
                           │
                           ▼
                   QUERY EMBEDDING
                           │
                           ▼
                   SEMANTIC SEARCH
                           │
                           ▼
                  TOP-K RESULTS
                           │
                           ▼
                    FASTAPI API
                           │
                           ▼
                  STREAMLIT DASHBOARD
