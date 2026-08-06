import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# ==========================================
# Paths
# ==========================================

INDEX_PATH = "vector_store/faiss.index"
METADATA_PATH = "embeddings/metadata.json"

# ==========================================
# Load Model
# ==========================================

print("Loading Sentence Transformer Model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ==========================================
# Load FAISS Index
# ==========================================

print("Loading FAISS Index...")
index = faiss.read_index(INDEX_PATH)

# ==========================================
# Load Metadata
# ==========================================

print("Loading Metadata...")

with open(METADATA_PATH, "r", encoding="utf-8") as file:
    metadata = json.load(file)

print("RAG Pipeline Ready!")

# ==========================================
# Retrieve Function
# ==========================================

def retrieve(query, top_k=3):

    try:

        # Empty input validation
        if not query.strip():
            return []

        # Convert query into embedding
        query_embedding = model.encode([query])

        # Convert to numpy float32
        query_embedding = np.array(query_embedding).astype("float32")

        # Search FAISS
        distances, indices = index.search(query_embedding, top_k)

        results = []

        # Prepare Results
        for score, idx in zip(distances[0], indices[0]):

            if idx == -1:
                continue

            results.append({
                "document": metadata[idx]["document"],
                "chunk_id": metadata[idx]["chunk_id"],
                "score": round(float(score), 4),
                "text": metadata[idx]["text"]
            })

        return results

    except Exception as e:

        print(f"Error : {e}")

        return []