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

# Membership operators
print("\nMembership operators")
print(f"'a' in 'Alejandro' = {'a' in 'Alejandro'}")
print(f"'b' not in 'Alejandro' = {'b' not in 'Alejandro'}")

# Bit operators
print("\nBit operators")
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {a & b}")  # 2 = 0010
print(f"OR: 10 | 3 = {a | b}")  # 11 = 1011
print(f"XOR: 10 ^ 3 = {a ^ b}")  # 9 = 1001
print(f"NOT: ~10 = {~a}")  # -11 = 1011
print(f"Shift left: 10 << 3 = {a << 3}")  # 80 = 1010000
print(f"Shift right: 10 >> 3 = {a >> 3}")  # 1 = 0001

"""Control structures"""

# Conditional structure
print("\nConditional structure")
my_string = "Alejandro"
if my_string == "Alejandro":
    print(f"Hello {my_string}")
elif my_string == "Ale":
    print(f"Hello {my_string}")
else:
    print("Is not Alejandro")

# Iterative structure
print("\nIterative structure")
for i in range(11):
    print(i)

i = 0
while i <= 5:
    print(i)
    i += 1

# Exception handling structure
print("\nException handling structure")
try:
    print(10 / 1)
except ZeroDivisionError as error:
    print(f"Error: {error}")
finally:
    print("Finally block")

"""Exercise: create a program that prints all even numbers from 10 to 56
and are not 16 and multiple of 3"""
print("\nExercise")

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
