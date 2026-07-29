import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# ----------------------------
# Paths
# ----------------------------
CHUNK_FILE = "outputs/chunks.json"

EMBEDDING_FOLDER = "embeddings"

EMBEDDING_FILE = os.path.join(EMBEDDING_FOLDER, "embeddings.npy")

METADATA_FILE = os.path.join(EMBEDDING_FOLDER, "metadata.json")

# ----------------------------
# Create folder
# ----------------------------
os.makedirs(EMBEDDING_FOLDER, exist_ok=True)

print("=" * 60)
print("EMBEDDING GENERATION STARTED")
print("=" * 60)

# ----------------------------
# Load Model
# ----------------------------
print("\nLoading Sentence Transformer Model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!")

# ----------------------------
# Read Chunks
# ----------------------------
print("\nReading chunks.json...")

with open(CHUNK_FILE, "r", encoding="utf-8") as file:
    chunks = json.load(file)

print(f"Total Chunks Found : {len(chunks)}")

# ----------------------------
# Generate Embeddings
# ----------------------------
embeddings = []

metadata = []

print("\nGenerating Embeddings...\n")

for index, chunk in enumerate(chunks, start=1):

    embedding = model.encode(chunk["text"])

    embeddings.append(embedding)

    metadata.append({
        "document": chunk["document"],
        "chunk_id": chunk["chunk_id"],
        "text": chunk["text"]
    })

    print(f"Processed Chunk {index}/{len(chunks)}")

# ----------------------------
# Save Embeddings
# ----------------------------
np.save(EMBEDDING_FILE, np.array(embeddings))

with open(METADATA_FILE, "w", encoding="utf-8") as file:
    json.dump(metadata, file, indent=4)

# ----------------------------
# Final Summary
# ----------------------------
print("\n" + "=" * 60)
print("EMBEDDINGS GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"Total Embeddings : {len(embeddings)}")

print(f"Embedding Dimension : {len(embeddings[0])}")

print(f"Embeddings Saved : {EMBEDDING_FILE}")

print(f"Metadata Saved : {METADATA_FILE}")

print("=" * 60)