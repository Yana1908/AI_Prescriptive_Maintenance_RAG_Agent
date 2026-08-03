from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI(title="AI Prescriptive Maintenance RAG API")

INDEX_FILE = "vector_store/faiss.index"
METADATA_FILE = "embeddings/metadata.json"

index = faiss.read_index(INDEX_FILE)

with open(METADATA_FILE, "r", encoding="utf-8") as f:
    metadata = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Prescriptive Maintenance RAG API Running"}


@app.post("/search")
def search(query: Query):

    query_embedding = model.encode([query.question])

    distances, indices = index.search(
        np.array(query_embedding, dtype=np.float32),
        k=3
    )

    results = []

    for score, idx in zip(distances[0], indices[0]):

        results.append({
            "document": metadata[idx]["document"],
            "chunk_id": metadata[idx]["chunk_id"],
            "score": float(score),
            "text": metadata[idx]["text"]
        })

    return {
        "query": query.question,
        "results": results
    }