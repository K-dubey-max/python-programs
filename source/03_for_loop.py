"""
03_for_loop.py

Examples of using for loops with range and lists.
"""

# Loop with range
for i in range(1, 6):
    print("Number:", i)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

# Using enumerate to get index and value
for index, fruit in enumerate(fruits, start=1):
    print(index, "->", fruit)
