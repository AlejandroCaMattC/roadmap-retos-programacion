"""python assemblies"""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Initial structure: {data}")  # Print the list

data.append(11)  # Add an element to the end of the list
print(f"Adding data at the end: {data}")

data.insert(0, 0)  # Add an element to the beginning of the list
print(f"Adding data at the beginning: {data}")

data.extend([12, 13, 14])  # Add multiple elements to the end of the list
print(f"Adding multiple data at the end: {data}")

data[3:3] = [-1, -2, -3]  # Add multiple elements at a specific position
print(f"Adding multiple data at a specific position: {data}")

del data[3]  # Remove an element at a specific position
print(f"Removing data at a specific position: {data}")

data[4] = 20  # Replace an element at a specific position
print(f"Replacing data at a specific position: {data}")

# Check if an element is in the list
print(f"Validate if element 5 is in the list: {5 in data}")

print(f"Clear the list: {data.clear()}")  # Clear the list
print(f"List after clear: {data}")  # Print the list after clearing


print("\n")

"""Exercise"""

# Show examples of the following operations:
# Joining two sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)  # Union of two sets
print(f"Joining two sets: {set3}")  # Print the union of the sets

# Intersection of two sets
set4 = set1.intersection(set2)  # Intersection of two sets
# Print the intersection of the sets
print(f"Intersection of two sets: {set4}")

# Difference of two sets
set5 = set1.difference(set2)  # Difference of two sets
# Print the difference of the sets
print(f"Difference of two sets: {set5}")  # Print the difference of the sets

# Symmetric difference of two sets
set6 = set1.symmetric_difference(set2)  # Symmetric difference of two sets
# Print the symmetric difference of the sets
# Print the symmetric difference of the sets
print(f"Symmetric difference of two sets: {set6}")
