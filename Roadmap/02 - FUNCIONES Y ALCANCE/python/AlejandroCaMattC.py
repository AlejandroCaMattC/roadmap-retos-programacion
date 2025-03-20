"""Functions and Scope"""
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

"""Functions defined by the user"""

# Simple function
print("\nSimple function")


def greet():
    print("Hello, Python!")


greet()

# Function with return
print("\nFunction with return")


def return_greet():
    return "Hello, Python!"


greeter = return_greet()
print(greeter)
print(return_greet())

# Function with parameters
print("\nFunction with parameters")


def arg_greet(greet, name):
    print(f"{greet}, {name}!")


arg_greet("Hello", "Python")

# Function with default parameters
print("\nFunction with default parameters") \



def default_greet(greet="Hello", name="Python"):
    print(f"{greet}, {name}!")


default_greet("Alejo")
default_greet()
default_greet(name="Alejo", greet="Hi")

# Function with arguments and return
print("\nFunction with arguments and return")


def arg_return_greet(greet, name):
    return f"{greet}, {name}!"


print(arg_return_greet("Hello", "Python"))

# Function with return and multiple values
print("\nFunction with return and multiple values")


def multiple_return_greet():
    return "Hello", "Python"


print(multiple_return_greet())
greet, name = multiple_return_greet()
print(greet)
print(name)
