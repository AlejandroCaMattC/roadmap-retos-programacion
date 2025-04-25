""" Higher Order Functions"""

# Higher Order Functions are functions that can take
# other functions as arguments or return them as results.
# They are a key concept in functional programming and allow for more abstract
# and flexible code.
# In Python, functions are first-class citizens, meaning they can be passed
# around as arguments, returned from other functions, and assigned to variables.
# This allows for the creation of higher-order functions that can operate on other functions.


def apply_func(func, x):
    return func(x)


print(apply_func(len, "Hello World"))  # 11


# Higher-order functions can also return other functions.

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


multiplier = apply_multiplier(2)
print(multiplier(5))  # 10
print(apply_multiplier(3)(5))  # 15
