# if_else_examples.py

# Simple age checker
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a valid number. Please enter an integer.")
    raise SystemExit(1)

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
