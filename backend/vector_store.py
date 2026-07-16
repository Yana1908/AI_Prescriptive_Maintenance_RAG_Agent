import os
import pickle
import numpy as np
import faiss

embedding_file = "embeddings/vectors/manual_embeddings.pkl"

index_folder = "embeddings/faiss"
os.makedirs(index_folder, exist_ok=True)

index_file = os.path.join(index_folder, "manual_index.faiss")

with open(embedding_file, "rb") as file:
    embeddings = pickle.load(file)

embedding_matrix = np.array(
    [item["embedding"] for item in embeddings],
    dtype="float32"
)

dimension = embedding_matrix.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embedding_matrix)

faiss.write_index(index, index_file)

print("=" * 60)
print("FAISS Index Created Successfully")
print(index_file)
print("Total Embeddings:", index.ntotal)
print("=" * 60)