"""Exception handling in Python"""


try:
    print(10/1)  # This will raise a ZeroDivisionError
    my_list = [1, 2, 3]
    print(my_list[5])  # This will raise an IndexError
except Exception as e:
    print("An error has occurred:", e)

print("Hello, what's your name?")

"""Exercise"""


class StrTypeError(Exception):
    """Custom exception for string type errors."""
    pass


def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError("The list must have at least 3 elements.")
    elif parameters[1] == 0:
        raise ZeroDivisionError("The second element cannot be zero.")
    elif type(parameters[2]) == str:
        raise StrTypeError("The third element must be a number.")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)


try:
    process_params([1, 2, 3, 4])  # This will raise an IndexError
except IndexError as e:
    print("An error occurred in the process_params function:", e)
except ZeroDivisionError as e:
    print("An error occurred in the process_params function:", e)
except StrTypeError as e:
    print("", e)
except Exception as e:
    print("A type error occurred:", e)
else:
    print("No errors occurred in the process_params function.")
    print("The process_params function executed successfully.")
    print("You can continue with the rest of the program.")
finally:
    print("End of the program")
