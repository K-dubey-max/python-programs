"""
01_variables_and_data_types.py

Simple examples of variables and common data types for beginners.
"""

# Integers
age = 20
print("age:", age, "type:", type(age))

# Float
price = 19.99
print("price:", price, "type:", type(price))

# String
name = "Alice"
print("name:", name, "type:", type(name))

# Boolean
is_student = True
print("is_student:", is_student, "type:", type(is_student))

# Multiple assignment
x, y, z = 1, 2.5, "hello"
print("x, y, z:", x, y, z)

# Converting types
num_str = "100"
num_int = int(num_str)
print("Converted:", num_int, type(num_int))

# Using type() and isinstance()
print("is name a str?", isinstance(name, str))
