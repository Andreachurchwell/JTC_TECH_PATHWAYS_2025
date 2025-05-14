# A class is like a blueprint for creating objects. Think of it as a mold for making things like dogs,
#  cats, or cars, each with their own properties and actions.
# It bundles data (variables) and functions (called methods) that operate on that data together.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"
# 🧱 The __init__ Method (Constructor)
# This is a special method that runs automatically when you create an object.

# Term	                   Meaning
# class	                   Keyword used to define a class
# __init__	               A special method called a constructor; runs automatically when you create an object
# self	                   Refers to the current instance of the class; must be the first parameter in methods
# Attributes	               Variables stored in an object (e.g., name, breed)
# Methods	                   Functions inside a class that use or modify object data

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1

#     def reset(self):
#         self.count = 0

#     def get_count(self):
#         return self.count
# c = Counter()
# c.increment()
# c.increment()
# print(c.get_count())  # Output: 2
# c.reset()
# print(c.get_count()) 