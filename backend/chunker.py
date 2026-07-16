import os
import json

# Folder containing cleaned text
INPUT_FOLDER = "outputs/cleaned"

# Output file
OUTPUT_FILE = "embeddings/chunks.json"

# Chunk settings
CHUNK_SIZE = 500
OVERLAP = 50

all_chunks = []

print("=" * 60)
print("TEXT CHUNKING STARTED")
print("=" * 60)

# Read every cleaned txt file
for file_name in os.listdir(INPUT_FOLDER):

    if file_name.endswith(".txt"):

        file_path = os.path.join(INPUT_FOLDER, file_name)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        start = 0
        chunk_number = 1

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            all_chunks.append({
                "source": file_name,
                "chunk_id": chunk_number,
                "text": chunk
            })

            chunk_number += 1

            start += CHUNK_SIZE - OVERLAP

        print(f"{file_name} → {chunk_number - 1} chunks created")

# Save JSON
os.makedirs("embeddings", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(all_chunks, file, indent=4)

print("\nTotal Chunks:", len(all_chunks))

print("\nSaved Successfully:")
print(OUTPUT_FILE)

print("=" * 60)
print("TEXT CHUNKING COMPLETED")
print("=" * 60)