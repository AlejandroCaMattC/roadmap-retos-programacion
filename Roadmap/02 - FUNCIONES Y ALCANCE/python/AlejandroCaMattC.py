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

# Function with variable number of arguments
print("\nFunction with variable number of arguments")


def var_args_greet(*names):
    for name in names:
        print(f"Hello, {name}!")


var_args_greet("Python", "Java", "C++")

# Function with variable number of keyword arguments
print("\nFunction with variable number of keyword arguments")


def var_kwargs_greet(**names):
    for key, value in names.items():
        print(f"Hello, {value} ({key})!")


var_kwargs_greet(
    language="Python",
    name="Alejo",
    alias="Alejandro",
    age=36
)


"""Functions inside functions"""
print("\nFunctions inside functions")


def outer_function():
    def inner_function():
        print("Inner function")
    inner_function()


outer_function()

"""Built-in functions"""
print("\nBuilt-in functions")


print(len("Alejandro"))
print(type(36))
print(type("Alejandro"))
print(str(36))
print(int("36"))
print("Alejandro".upper())


"""Local and global scope"""
print("\nLocal and global scope")

global_variable = "Python"

print(global_variable)


def hello_python():
    local_variable = "Java"
    print(f"Hello, {local_variable}, {global_variable}!")


print(global_variable)
# print(local_variable)  # Cannot access local variable
hello_python()


"""Exercise"""
print("\nExercise")


def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text_1} {text_2}")
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count


print(print_numbers("Hello", "Python"))
