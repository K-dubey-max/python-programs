"""
06_lists_tuples_dictionaries.py

Examples of lists, tuples, and dictionaries with common operations.
"""

# List (mutable)
colors = ["red", "green", "blue"]
print("colors:", colors)
colors.append("yellow")
print("after append:", colors)
colors.remove("green")
print("after remove:", colors)

# Tuple (immutable)
point = (10, 20)
print("point:", point)
# You cannot change a tuple item: point[0] = 5 -> Error

# Dictionary (key -> value)
student = {"name": "Amy", "age": 21}
print("student name:", student["name"])  # access by key
student["grade"] = "A"  # add new key
print("student:", student)

# Looping through a dictionary
for key, value in student.items():
    print(key, "=>", value)
