import re

"""Regular expressions in Python
   - Regular expressions are a powerful tool 
   for searching and manipulating strings."""

# Regular expressions are defined using the re module in Python.
# The re module provides functions for searching, matching, and
# manipulating strings using regular expressions.


def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)


print(find_numbers("This is the exercise 16 published in 15/04/2025"))


"""Exercise"""


def validate_email(email: str) -> bool:
    """Validates if the given email address is valid."""
    # Regular expression pattern for validating an email address
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


print(validate_email("alejandro@gmail.com"))


def validate_phone(phone: str) -> bool:
    """Validates if the given phone number is valid."""
    # Regular expression pattern for validating a phone number
    pattern = r"^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    return re.match(pattern, phone) is not None


print(validate_phone("+503 7853-9586"))


def validate_url(url: str) -> bool:
    """Validates if the given URL is valid."""
    # Regular expression pattern for validating a URL
    pattern = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
    return re.match(pattern, url) is not None


print(validate_url("https://alejandro.com"))
