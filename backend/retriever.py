import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_FILE = "vector_store/faiss.index"
METADATA_FILE = "embeddings/metadata.json"

print("="*60)
print("RAG RETRIEVER")
print("="*60)

print("\nLoading FAISS Index...")
index = faiss.read_index(INDEX_FILE)

print("Loading Metadata...")
with open(METADATA_FILE, "r", encoding="utf-8") as f:
    metadata = json.load(f)

print("Loading Embedding Model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

while True:

    query = input("\nEnter your question (type exit to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding, dtype=np.float32),
        k=3
    )

    print("\nTop Results\n")

    for i, idx in enumerate(indices[0], start=1):

        print("="*60)
        print(f"Result {i}")
        print(f"Document : {metadata[idx]['document']}")
        print(f"Chunk ID : {metadata[idx]['chunk_id']}")
        print(f"Distance : {distances[0][i-1]:.4f}")
        print()
        print(metadata[idx]["text"][:600])
        print("="*60)