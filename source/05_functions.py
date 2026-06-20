"""
05_functions.py

Functions: definition, parameters, return values, docstring, and default arguments.
"""

def greet(name="World"):
    """Return a greeting for name."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of a and b."""
    return a + b

# Using the functions
print(greet("Sam"))
print(greet())
print("3 + 4 =", add(3, 4))

# A function that returns multiple values

def divide_remainder(a, b):
    """Return quotient and remainder of a // b and a % b."""
    return a // b, a % b

q, r = divide_remainder(10, 3)
print("quotient:", q, "remainder:", r)
