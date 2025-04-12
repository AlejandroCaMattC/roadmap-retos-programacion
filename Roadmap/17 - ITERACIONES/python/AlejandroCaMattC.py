"""Iterations"""
# Iterations are used to repeat a block of code multiple times.
# There are three types of iterations in Python: for, while, and recursion.

# For
for i in range(10):
    print(i + 1, end=" ")

# While
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

# Recursion


def countdown(i=1):
    if i <= 10:
        print(i, end=" ")
        countdown(i + 1)


countdown()

print("\n")

"""Exercise"""

for e in [1, 2, 3, 4, 5]:
    print(e, end=" ")

for e in {"1", "2", "3", "4", "5"}:
    print(e, end=" ")

for e in ("1", "2", "3", "4", "5"):
    print(e, end=" ")

for e in {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}:
    print(e, end=" ")

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c, end=" ")
print("\n")

for e in reversed([1, 2, 3, 4, 5]):
    print(e, end=" ")
print("\n")

for e in reversed(["Py", "th", "on"]):
    print(e, end=" ")
print("\n")

for i, e in enumerate(sorted(["A", "l", "e", "j", "a", "n", "d", "r", "o"])):
    print(f"Index: {i}, Value: {e}")
print("\n")
