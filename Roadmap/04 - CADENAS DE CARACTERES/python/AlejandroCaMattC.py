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

# Delete spaces at the beginning an the end - Strip
print("  Hello  ".strip())
print("  Hello  ".lstrip())
print("  Hello  ".rstrip())

# Startswith and endswith
print(s1.startswith("H"))
print(s2.endswith("n"))
print(s1.startswith("e"))
print(s2.endswith("o"))

# Find position
print(s1.find("l"))
print(s2.find("o"))
print(s1.find("z"))
print("Jose Alejandro".find("Ale"))

# Find ocurrences
s3 = "Jose Alejandro Campos"
print(s1.count("l"))
print(s2.count("o"))
print(s3.count("a"))
print(s3.lower().count("a"))
