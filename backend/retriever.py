import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("embeddings/faiss/manual_index.faiss")

# Load chunks
with open("embeddings/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

def retrieve(query, top_k=5):
    # Convert query into embedding
    query_embedding = model.encode([query]).astype("float32")

    # Search
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results

if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (type exit to quit): ")

        if question.lower() == "exit":
            break

        answers = retrieve(question)

        print("\nTop Results:\n")

        for i, ans in enumerate(answers, 1):
            print("=" * 60)
            print(f"Result {i}")
            print("Source:", ans["source"])
            print("Chunk:", ans["chunk_id"])
            print(ans["text"][:600])
            print("=" * 60)