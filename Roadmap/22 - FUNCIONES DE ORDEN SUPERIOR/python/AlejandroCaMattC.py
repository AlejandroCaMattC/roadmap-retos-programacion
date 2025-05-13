""" Higher Order Functions"""

# Higher Order Functions are functions that can take other functions as arguments
# or return them as results. They are a key concept in functional programming and
# allow for more abstract and flexible code. In Python, functions are first-class
# citizens, meaning they can be passed around as arguments, returned from other
# functions, and assigned to variables. This allows for the creation of higher-
# order functions that can operate on other functions.

from functools import reduce

from datetime import datetime


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

# Renamed the custom 'sum' function to 'add' to avoid conflict with the built-in 'sum'.


def add(x, y):
    return x + y


# Updated the reduce call to use 'add' instead of 'sum'.
print(reduce(add, numbers))

"""Exercise"""

# Students list with names, birthdays and a lists of grades
students = [
    {
        "name": "Alejandro",
        "birthday": "1985-17-06",
        "grades": [10, 9, 8, 3, 6]
    },
    {
        "name": "Matias",
        "birthday": "1995-01-07",
        "grades": [10, 4, 8, 7, 6]
    },
    {
        "name": "Cecilia",
        "birthday": "2001-05-08",
        "grades": [10, 9, 8, 7, 10]
    }
]

# Calculate the average of the grades of each student


def calculate_average(grades):
    return sum(grades) / len(grades)


print(
    list(
        map(
            lambda student: {
                "name": student["name"],
                "average": calculate_average(student["grades"])
            },
            students
        )
    )
)

# Print a list of the students with an average greater than 9


print(
    list(map(lambda student: student["name"], filter(
        lambda student: calculate_average(student["grades"]) > 7,
        students
    )))
)

# Print the list of students sorted by the youngest to the oldest


print(sorted(students, key=lambda student: datetime.strptime(
    student["birthday"], "%Y-%d-%m"), reverse=True
))

# Print the highest average of the students
print(
    {
        "name": max(
            students,
            key=lambda student: calculate_average(student["grades"])
        )["name"],
        "average": calculate_average(
            max(
                students,
                key=lambda student: calculate_average(student["grades"])
            )["grades"]
        )
    }
)
