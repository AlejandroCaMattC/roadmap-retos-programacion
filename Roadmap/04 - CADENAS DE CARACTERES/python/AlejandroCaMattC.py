"""Character Chains
"""
s1 = "Hello"
s2 = "Python"

# Concatenation
print(s1 + " " + s2 + "!")

# Repetition
print(s1 * 3)
print(s2 + " " + s1 * 2)

# Indexing
print(s1[0])
print(s2[1])
print(s1[-1] + s2[-2])

# Length
print(len(s1))
print(len(s2))

# Slicing
print(s1[1:3])
print(s2[2:])
print(s1[:3])
print(s2[:])

# Searching
print("H" in s1)
print("P" not in s2)

# Replace
print(s1.replace("l", "y"))
print(s2.replace("o", "i"))

# Divide
print(s1.split("l"))
print(s2.split("t"))

# Upper, Lower and Capitalize
print(s1.upper())
print(s2.lower())
print("alejandro campos".capitalize())
print("alejandro campos".title())
