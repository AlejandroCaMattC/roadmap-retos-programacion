"""Recursion in Python"""
# A function that calls itself is known as a recursive function.
# The process of defining a function that calls itself is called recursion.


def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)


# countdown(100)


def factorial(number: int) -> int:
    """Factorial of a number"""
    if number < 0:
        print("The number must be positive")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(15))


def fibonacci(number: int) -> int:
    """Fibonacci series"""
    if number < 0:
        print("The number must be positive")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(5))
