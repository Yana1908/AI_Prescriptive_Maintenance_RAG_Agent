import os
import re

# Folder containing extracted text files
INPUT_FOLDER = "outputs"

# Folder to save cleaned text
OUTPUT_FOLDER = "outputs/cleaned"

# Create cleaned folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 60)
print("TEXT CLEANING STARTED")
print("=" * 60)

# Read every txt file
for file_name in os.listdir(INPUT_FOLDER):

    if file_name.endswith(".txt"):

        input_path = os.path.join(INPUT_FOLDER, file_name)

        with open(input_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove multiple blank lines
        text = re.sub(r"\n\s*\n", "\n", text)

        # Remove strange characters
        text = text.replace("\x00", "")

        # Remove leading and trailing spaces
        text = text.strip()

        # Save cleaned file
        output_path = os.path.join(OUTPUT_FOLDER, file_name)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Cleaned: {file_name}")

print("\n")
print("=" * 60)
print("TEXT CLEANING COMPLETED")
print("=" * 60)