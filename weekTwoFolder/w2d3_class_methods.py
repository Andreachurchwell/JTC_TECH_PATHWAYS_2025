#  Class Method Basics
# Defined with: @classmethod decorator.
# First parameter: cls (refers to the class, not the instance).
# Use case: Access or modify class state that applies across all instances.

# class MyClass:
#     class_variable = 0

#     @classmethod
#     def my_class_method(cls, value):
#         cls.class_variable = value

# # Test it
# print(MyClass.class_variable)  # Output: 0
# MyClass.my_class_method(10)
# print(MyClass.class_variable)  # Output: 10


# ✅ When to Use a Class Method
# You need to access or modify class-level data.
# You want an alternative constructor (e.g., from a dictionary or JSON).

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, string):
#         name, age = string.split(',')
#         return cls(name, int(age))

# # Using the class method
# person1 = Person.from_string("Andrea,43")
# print(person1.name)  # Andrea
# print(person1.age)   # 43
    
# 🔁 Difference from Static Method
# @classmethod has access to cls (class).

# @staticmethod does not take self or cls as parameters; acts like a regular function inside the class.

# Class Attribute: An attribute that is defined at the class level and shared by all instances

# Instance Attribute: An attribute that is unique to each instance of a class

# Class Method: A method that is bound to the class rather than an instance

# Instance Method: A method that is bound to an instance and can access instance data

# Static Method: A method that doesn't operate on instance or class data

# Method Overriding: Redefining a method in a subclass that exists in the parent class

# Decorator: A special syntax to modify a function or method's behavior

# Factory Method: A method that creates and returns objects, often using class methods

# Namespace: The place where variables are stored and how they are located

# Attribute Lookup: The process Python uses to find an attribute reference



# class Student:
#     # Class attribute - shared by all instances
#     school_name = "Python Academy"
#     total_students = 0
    
#     def __init__(self, name, grade):
#         # Instance attributes - unique to each instance
#         self.name = name
#         self.grade = grade
        
#         # Updating a class attribute from instance method
#         Student.total_students += 1
    
#     def display_info(self):
#         print(f"Name: {self.name}, Grade: {self.grade}, School: {self.school_name}")

# # Create some students
# alice = Student("Alice", 95)
# bob = Student("Bob", 87)

# # Accessing instance attributes
# print(f"Alice's grade: {alice.grade}")  # Output: Alice's grade: 95
# print(f"Bob's grade: {bob.grade}")      # Output: Bob's grade: 87

# # Accessing class attributes
# print(f"School name (from class): {Student.school_name}")  # Output: School name (from class): Python Academy
# print(f"School name (from instance): {alice.school_name}") # Output: School name (from instance): Python Academy
# print(f"Total students: {Student.total_students}")         # Output: Total students: 2

# # Changing class attribute through the class
# Student.school_name = "Code Academy"
# print(f"Alice's school after change: {alice.school_name}")  # Output: Alice's school after change: Code Academy
# print(f"Bob's school after change: {bob.school_name}")      # Output: Bob's school after change: Code Academy

# # What happens if we change it through an instance?
# alice.school_name = "Alice's Private School"
# print(f"Alice's school: {alice.school_name}")               # Output: Alice's school: Alice's Private School
# print(f"Bob's school: {bob.school_name}")                   # Output: Bob's school: Code Academy
# print(f"Class school name: {Student.school_name}")          # Output: Class school name: Code Academy







