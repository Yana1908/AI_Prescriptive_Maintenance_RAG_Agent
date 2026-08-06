from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag_pipeline import retrieve

# ------------------------------------
# FastAPI App
# ------------------------------------
app = FastAPI(
    title="AI Prescriptive Maintenance RAG API",
    description="API for Semantic Search using FAISS and Sentence Transformers",
    version="1.0"
)

# ------------------------------------
# Request Model
# ------------------------------------
class Query(BaseModel):
    question: str
    top_k: int = 5

# ------------------------------------
# Home Route
# ------------------------------------
@app.get("/")
def home():
    return {
        "message": "AI Prescriptive Maintenance RAG API is Running Successfully!"
    }

# ------------------------------------
# Search Route
# ------------------------------------
from time import time

@app.post("/search")
def search(query: Query):

    if not query.question.strip():
        return {
            "query": "",
            "results": [],
            "message": "Question cannot be empty."
        }

    start = time()

    results = retrieve(query.question, query.top_k)

    end = time()

    return {
        "query": query.question,
        "total_results": len(results),
        "search_time": round(end - start, 3),
        "results": results
    }
    # Retrieve relevant chunks
    results = retrieve(query.question)

    return {
        "query": query.question,
        "total_results": len(results),
        "results": results
    }

# ------------------------------------
# Health Check
# ------------------------------------
@app.get("/health")
def health():
    return {
        "status": "Running",
        "service": "AI Prescriptive Maintenance RAG API"
    }