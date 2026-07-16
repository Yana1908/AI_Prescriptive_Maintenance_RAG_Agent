import json
import os
import pickle

from sentence_transformers import SentenceTransformer

# Load embedding model
print("=" * 60)
print("LOADING EMBEDDING MODEL...")
print("=" * 60)

model = SentenceTransformer("all-MiniLM-L6-v2")

# Read chunk file
with open("embeddings/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"\nTotal Chunks Found: {len(chunks)}")

embeddings = []

print("\nGenerating Embeddings...\n")

for chunk in chunks:

    vector = model.encode(chunk["text"]).tolist()

    embeddings.append({
        "source": chunk["source"],
        "chunk_id": chunk["chunk_id"],
        "text": chunk["text"],
        "embedding": vector
    })

print("\nEmbeddings Generated Successfully!")

# Create folder if not exists
os.makedirs("embeddings/vectors", exist_ok=True)

# Save embeddings
output_file = "embeddings/vectors/manual_embeddings.pkl"

with open(output_file, "wb") as file:
    pickle.dump(embeddings, file)

print("\nSaved Successfully:")
print(output_file)

print("=" * 60)
print("DAY 5 COMPLETED")
print("=" * 60)