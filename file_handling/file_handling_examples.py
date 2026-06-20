# file_handling_examples.py

# Write to a file
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello file\n")

print("Wrote 'Hello file' to example.txt")

# Read the file back
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("Content of example.txt:\n", content)
