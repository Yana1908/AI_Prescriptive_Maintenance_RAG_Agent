import json
import pickle
from sentence_transformers import SentenceTransformer

# Load chunks from chunks.json
with open("outputs/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

embedding_only = []

for chunk in chunks:
    embedding = model.encode(chunk["text"]).tolist()
    embedding_only.append(embedding)

# Save embeddings
with open("embeddings/vectors/manual_embeddings.pkl", "wb") as file:
    pickle.dump(embedding_only, file)

print("Embeddings generated successfully!")