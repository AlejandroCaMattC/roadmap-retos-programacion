import os

"""File handling in Python"""

file_name = "AlejandroCaMattC.txt"  # File name

with open(file_name, "w") as file:  # Open a file in write mode
    file.write("Alejandro Campos\n")  # Write to the file
    file.write("36\n")
    file.write("Python\n")


with open(file_name, "r") as file:  # Open a file in read mode
    print(file.read())  # Read the file


os.remove(file_name)  # Remove the file

"""Exercise"""

file_name = "venta.txt"  # File name

open(file_name, "a")  # Open a file in write mode

while True:
    print("1. Add product")
    print("2. Search product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Show all products")
    print("6. Calculate total sale")
    print("7. Calculate sale by product")
    print("8. Exit")

    option = input("Select an option: ")

    if option == "1":
        name = input("Enter product name: ")
        units = input("Enter product units: ")
        price = input("Enter product price: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {units}, {price}\n")
    elif option == "2":
        name = input("Enter product name to search: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif option == "3":
        name = input("Enter product name to update: ")
        units = input("Enter new product units: ")
        price = input("Enter new product price: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        # Open the file in write mode to update it
        with open(file_name, "w") as file:
            for line in lines:
                # Check if the line contains the product name
                # If it does, update it with the new values
                # Otherwise, write the original line to the file
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {units}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input("Enter product name to update: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())

    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                units = int(components[1])
                price = float(components[2])
                total += units * price
        print(f"Total sale: {total}")
    elif option == "7":
        name = input("Enter product name to search: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    units = int(components[1])
                    price = float(components[2])
                    total += units * price
                    break
        print(f"Total sale for {name}: {total}")
    elif option == "8":
        # os.remove(file_name)  # Remove the file
        # print("File removed")
        break
    else:
        print("Invalid option, please select again.")
