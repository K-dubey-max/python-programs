"""
02_if_else.py

Beginner example of if / elif / else statements with comments.
"""

try:
    score = int(input("Enter your score (0-100): "))
except ValueError:
    print("Please enter a valid integer number.")
    raise SystemExit(1)

if score < 0 or score > 100:
    print("Score should be between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
