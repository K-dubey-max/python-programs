"""
08_oop_class_and_object.py

Basic Object-Oriented Programming: a simple class (Person) with attributes and methods.
"""

class Person:
    """Simple Person class to demonstrate __init__ and instance methods."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age}."

# Create objects
alice = Person("Alice", 30)
print(alice.introduce())
print(alice.have_birthday())

bob = Person("Bob", 25)
print(bob.introduce())
