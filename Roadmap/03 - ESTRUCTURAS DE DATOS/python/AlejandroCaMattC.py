"""Data structures in Python"""
print("\nData structures in Python\n")
# Lists
print("\nLists\n")
my_list = [1, 2, 3, 4, 5]
my_friends = ["Alejandro", "Carmen", "Matias"]
print(my_list)
print(my_friends)

# Add values to the list
my_list.append(6)
print(my_list)
my_friends.append("Carlos")
print(my_friends)

# Remove values from the list
my_list.remove(6)
print(my_list)
my_friends.remove("Carlos")
print(my_friends)

# Update values in the list
my_list[2] = 10
print(my_list)
my_friends[1] = "Mirian"
print(my_friends)

# Order values in the list
my_list.sort()
print(my_list)
my_friends.sort()
print(my_friends)

# Tuples
print("\nTuples\n")
print("\nTuples\n")
my_tuple = (1, 5, 3, 2, 4)
my_friends = ("Alejandro", "Carmen", "Matias")
print(my_tuple)
print(my_friends)
# Tuples cannot be modified

new_tuple = ("Alejo", "Jose", 36, 4.5)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[2])
print(new_tuple[3])

my_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(type(my_tuple))

# Sets - the set is a collection of unordered and unindexed elements
# With no duplicate elements
print("\nSets\n")
my_set = {"Alejandro", "Carmen", "Matias", "29"}
print(my_set)
my_set.add("Carlos")
print(my_set)
my_set.remove("Carlos")
print(my_set)
my_set = set(sorted(my_set))
print(my_set)
my_set.add("Jose")
my_set.add("Jose")
print(my_set)
my_set.remove("Jose")
print(my_set)
print(type(my_set))
my_set.update(["Alejo", "Mirian"])
print(sorted(my_set))
my_set.clear()
print(my_set)

# Dictionaries
print("\nDictionaries\n")
my_dict = {
    "name": "Alejandro",
    "surname": "Campos",
    "age": 29,
    "city": "Bogota"
}

print(my_dict)
my_dict["age"] = 30
print(my_dict)
my_dict["city"] = "Medellin"
print(my_dict)
print(my_dict["name"])

my_dict["email"] = "alejo@gmail.com"
print(my_dict)
my_dict.pop("email")
print(my_dict)
del my_dict["city"]
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)

print(type(my_dict))

"""Exercise"""


def search_contact(agenda, name):
    if name in agenda:
        print(f"The phone number of {name} is {agenda[name]}")
    else:
        print(f"{name} is not in the agenda.")


def add_contact(agenda, name, phone):
    if phone.isdigit() and len(phone) <= 11:
        agenda[name] = phone
        print("Contact added successfully.")
    else:
        print("Invalid phone number.")


def update_contact(agenda, name):
    if name in agenda:
        phone = input("Enter the new phone number: ")
        add_contact(agenda, name, phone)
    else:
        print(f"{name} is not in the agenda.")


def delete_contact(agenda, name):
    if name in agenda:
        del agenda[name]
        print("Contact deleted successfully.")
    else:
        print(f"{name} is not in the agenda.")


def display_agenda(agenda):
    if agenda:
        print("\nAll Contacts:")
        for name, phone in agenda.items():
            print(f"{name}: {phone}")
    else:
        print("\nThe agenda is empty.")


def my_agenda():
    agenda = {}

    while True:
        print("\nAgenda")
        print("1. Search contact")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")

        option = input("\nChoose an option: ")

        try:
            option_num = int(option)
            match option_num:
                case 1:
                    name = input("Enter the name you are looking for: ")
                    search_contact(agenda, name)
                case 2:
                    name = input("Enter the name: ")
                    phone = input("Enter the phone: ")
                    add_contact(agenda, name, phone)
                case 3:
                    name = input("Enter the name your want to update: ")
                    update_contact(agenda, name)
                case 4:
                    name = input("Enter the name you want to delete: ")
                    delete_contact(agenda, name)
                case 5:
                    display_agenda(agenda)
                case 6:
                    print("You are going to exit the agenda.")
                    print(agenda)
                    break
                case _:
                    print("Invalid option. Please choose a valid option from 1 to 6")
        except ValueError:
            print("Invalid input. Please enter a number.")


my_agenda()
