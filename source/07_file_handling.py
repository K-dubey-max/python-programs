"""
07_file_handling.py

Basic file handling: write and read a text file using 'with' context manager.
"""

filename = "sample.txt"

# Write to a file
with open(filename, "w", encoding="utf-8") as f:
    f.write("Hello from file handling example!\n")
    f.write("Line 2\n")
print(f"Wrote to {filename}")

# Read the entire file
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
print("Content read from file:\n", content)

# Read line by line
print("Reading line by line:")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
