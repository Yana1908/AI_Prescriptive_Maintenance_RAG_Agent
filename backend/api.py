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
@app.post("/search")
def search(query: Query):

    # Empty input validation
    if not query.question.strip():
        return {
            "query": "",
            "results": [],
            "message": "Please enter a valid question."
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