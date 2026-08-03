import os
import json
import numpy as np
import faiss

# -----------------------------
# Paths
# -----------------------------
EMBEDDING_FOLDER = "embeddings"

EMBEDDING_FILE = os.path.join(EMBEDDING_FOLDER, "embeddings.npy")
METADATA_FILE = os.path.join(EMBEDDING_FOLDER, "metadata.json")

VECTOR_FOLDER = "vector_store"
INDEX_FILE = os.path.join(VECTOR_FOLDER, "faiss.index")

os.makedirs(VECTOR_FOLDER, exist_ok=True)

print("=" * 60)
print("VECTOR STORE CREATION STARTED")
print("=" * 60)

# -----------------------------
# Load Embeddings
# -----------------------------
print("\nLoading Embeddings...")

embeddings = np.load(EMBEDDING_FILE)

print("Embeddings Loaded Successfully!")

print(f"Embedding Shape : {embeddings.shape}")

# -----------------------------
# Load Metadata
# -----------------------------
print("\nLoading Metadata...")

with open(METADATA_FILE, "r", encoding="utf-8") as file:
    metadata = json.load(file)

print(f"Metadata Loaded : {len(metadata)}")

# -----------------------------
# Create FAISS Index
# -----------------------------
print("\nCreating FAISS Index...")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("FAISS Index Created!")

# -----------------------------
# Save Index
# -----------------------------
faiss.write_index(index, INDEX_FILE)

print("\nSaving Index...")

print("Index Saved Successfully!")

# -----------------------------
# Verification
# -----------------------------
loaded_index = faiss.read_index(INDEX_FILE)

print("\nVerification Successful!")

# -----------------------------
# Summary
# -----------------------------
print("\n" + "=" * 60)
print("VECTOR STORE CREATED SUCCESSFULLY")
print("=" * 60)

print(f"Embedding Dimension : {dimension}")
print(f"Total Vectors       : {loaded_index.ntotal}")
print(f"Index Type          : IndexFlatL2")
print(f"Saved To            : {INDEX_FILE}")

print("=" * 60)