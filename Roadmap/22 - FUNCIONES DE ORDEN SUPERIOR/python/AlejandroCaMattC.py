""" Higher Order Functions"""

# Higher Order Functions are functions that can take
# other functions as arguments or return them as results.
# They are a key concept in functional programming and allow for more abstract
# and flexible code.
# In Python, functions are first-class citizens, meaning they can be passed
# around as arguments, returned from other functions, and assigned to variables.
# This allows for the creation of higher-order functions that can operate on other functions.


from functools import reduce


def apply_func(func, x):
    return func(x)


print(apply_func(len, "Hello World"))  # 11


# Higher-order functions can also return other functions.

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


multiplier = apply_multiplier(3)
print(multiplier(5))  # 10
print(apply_multiplier(3)(5))  # 15

# System

# Higher-order functions are often used in functional programming to create
# more abstract and reusable code. They can be used to create decorators,
# which are functions that modify the behavior of other functions.

numbers = [3, 4, 2, 5, 1]

# map()


def apply_double(n):
    return n * 2


print(list(map(apply_double, numbers)))  # [6, 8, 4, 10, 2]

# filter()


def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, numbers)))  # [2]


# sorted()

print(sorted(numbers))  # [1, 2, 3, 4, 5]
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
print(sorted(numbers, key=lambda x: -x))  # [5, 4, 3, 2, 1]

# reduce()


def sum(x, y):
    return x + y


print(reduce(sum, numbers))
