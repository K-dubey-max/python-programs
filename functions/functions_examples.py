# functions_examples.py

# A function that greets someone

def greet(name="World"):
    """Return a greeting string for `name`."""
    return f"Hello, {name}!"

# A simple function to add two numbers

def add(a, b):
    return a + b

print(greet("Alice"))
print(greet())
print("2 + 3 =", add(2, 3))
