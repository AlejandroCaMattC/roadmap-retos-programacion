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

# Find occurrences
s3 = "Jose Alejandro Campos"
print(s1.count("l"))
print(s2.count("o"))
print(s3.count("a"))
print(s3.lower().count("a"))


# Format
print("Saludo: {}, Lenguaje: {}!".format(s1, s2))

# Interpolation
print(f"Saludo: {s1}, Lenguaje: {s2}!")

# Character list transformation
print(list(s3))

l1 = [s1, " ", s2, "!"]

print("".join(l1))
print("-".join(l1))

# Numeric transformation

s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Various checks
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


"""Extra"""


def check(word1: str, word2: str):
    # Palindromes
    print(f"Is {word1} a palindrome?: {word1 == word1[::-1]}")
    print(f"Is {word2} a palindrome?: {word2 == word2[::-1]}")

    # Anagrams
    print(f"Is {word1} an anagram of {word2}?: {sorted(word1) == sorted(word2)}")

    # Isograms
    print(len(word1))
    print(len(set(word1)))
    print(f"Is {word1} an isogram?: {len(word1) == len(set(word1))}")
    print(f"Is {word2} an isogram?: {len(word2) == len(set(word2))}")

    def isogram(word: str) -> bool:

        word_dict = dict()

        for letter in word:
            word_dict[letter] = word_dict.get(letter, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]

        for letter_count in values:
            if letter_count != isogram_len:
                isogram = False
                break
        return isogram

    print(f"Is {word1} an isogram?: {isogram(word1)}")
    print(f"Is {word2} an isogram?: {isogram(word2)}")


check("radar", "pythonpythonpython")
