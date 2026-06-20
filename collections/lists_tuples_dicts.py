# lists_tuples_dicts.py

# List (mutable)
fruits = ["apple", "banana", "cherry"]
print("fruits:", fruits)
fruits.append("date")
print("after append:", fruits)

# Tuple (immutable)
coords = (10, 20)
print("coords:", coords)

# Dictionary (key -> value)
person = {"name": "Bob", "age": 30}
print("person name:", person["name"])  # access by key
# Add or change a value
person["city"] = "New York"
print("person:", person)
