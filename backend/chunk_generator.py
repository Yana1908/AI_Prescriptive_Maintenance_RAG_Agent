import os
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Folder containing cleaned text files
INPUT_FOLDER = "outputs/cleaned"

# Output file
OUTPUT_FILE = "outputs/chunks.json"

# Create splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

all_chunks = []
document_count = 0
chunk_count = 0

print("=" * 60)
print("CHUNK GENERATION STARTED")
print("=" * 60)

# Read all txt files
for file in os.listdir(INPUT_FOLDER):
    print(file)

    if file.endswith(".txt"):

        document_count += 1

        file_path = os.path.join(INPUT_FOLDER, file)

        print(f"\nReading: {file}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = text_splitter.split_text(text)

        print(f"Chunks Created: {len(chunks)}")

        for i, chunk in enumerate(chunks):

            all_chunks.append({
                "document": file,
                "chunk_id": i + 1,
                "text": chunk
            })

        chunk_count += len(chunks)

# Save chunks
os.makedirs("outputs", exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=4)

print("\n" + "=" * 60)
print("CHUNK GENERATION COMPLETED")
print("=" * 60)
print(f"Documents Processed : {document_count}")
print(f"Total Chunks        : {chunk_count}")
print(f"Chunks Saved To     : {OUTPUT_FILE}")
print("=" * 60)