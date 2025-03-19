# https://www.python.org/

# This is a comment
# Comments are used to explain code when the Python interpreter ignores them.
"""This is another way to write a comment in Python for multiple lines."""
'''This is another way to write a comment in Python for multiple lines.'''

# Variables
# Variables are containers for storing data values.
name = "Alejandro"  # This is a string
age = 20  # This is an integer
height = 1.75  # This is a float (decimal)
is_student = True  # This is a boolean


# Constants
# Constants are fixed values that a program may not alter during its execution.
FIRST_CONSTANT = "Hello, Python!"  # This is how a constant is declared in Python

print(FIRST_CONSTANT)  # Output: Hello, Python!
print("Hola, Python!")

print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>
print(type(FIRST_CONSTANT))  # Output: <class 'str'>
print(type("Hola, Python!"))  # Output: <class 'str'>
print(type(10))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
