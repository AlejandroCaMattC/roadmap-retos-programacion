"""
Operators
"""

# Arithmetic operators
print("Arithmetic operators")
a = 5
b = 2
print(a + b)  # 7
print(f"Sum: 5 + 2 = {a + b}")
print(f"Subtraction: 5 - 2 = {a - b}")
print(f"Multiplication: 5 * 2 = {a * b}")
print(f"Division: 5 / 2 = {a / b}")
print(f"Module: 5 % 2 = {a % b}")
print(f"Exponent: 5 ** 2 = {a ** b}")
print(f"Floor division: 5 // 2 = {a // b}")

# Comparison operators
print("\nComparison operators")
print(f"Equal: 5 == 2 = {a == b}")
print(f"Different: 5 != 2 = {a != b}")
print(f"Greater than: 5 > 2 = {a > b}")
print(f"Less than: 5 < 2 = {a < b}")
print(f"Greater than or equal: 5 >= 2 = {a >= b}")
print(f"Less than or equal: 5 <= 2 = {a <= b}")

# Logical operators
print("\nLogical operators")
print(f"a= {a}, b= {b}")
print(f"AND &&: a + b == 7 and a - b == 3 = {a + b == 7 and a - b == 3}")
print(f"OR ||: a + b == 7 or a - b == 3 = {a + b == 7 or a - b == 3}")
print(f"NOT !: not a + b == 7 = {not a + b == 7}")

# Assignment operators
print("\nAssignment operators")
my_number = 11
print(f"my_number = {my_number}")
my_number += 3
print(f"my_number += 3: {my_number}")
my_number -= 3
print(f"my_number -= 3: {my_number}")
my_number *= 3
print(f"my_number *= 3: {my_number}")
my_number /= 3
print(f"my_number /= 3: {my_number}")
my_number %= 3
print(f"my_number %= 3: {my_number}")
my_number **= 3
print(f"my_number **= 3: {my_number}")
my_number //= 3
print(f"my_number //= 3: {my_number}")

# Identity operators
print("\nIdentity operators")
my_new_number = 1.0
# Identify the memory value
print(f"my_number is my_new_number: {my_number is my_new_number}")
# Identify the memory value
print(f"my_number is not my_new_number: {my_number is not my_new_number}")
