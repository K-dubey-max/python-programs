# class_and_object.py

# A simple class for beginners
class Dog:
    """A Dog has a name and can speak."""

    def __init__(self, name):
        # `self.name` stores the dog's name
        self.name = name

    def speak(self):
        # A method that returns what the dog says
        return f"{self.name} says woof!"

# Create (instantiate) an object of class Dog
my_dog = Dog("Rex")
print(my_dog.speak())

# Another example showing attributes
another = Dog("Luna")
print(another.name)
