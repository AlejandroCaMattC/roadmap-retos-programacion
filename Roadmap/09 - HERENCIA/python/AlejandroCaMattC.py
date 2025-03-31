"""Inheritance in Python"""
# Inheritance allows us to define a class that inherits all the methods
# and properties from another class.


class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

# Subclass Dog inherits from Animal
# Dog is a subclass of Animal


class Dog(Animal):

    def sound(self):
        print("Woof! Woof!")


class Cat(Animal):

    def sound(self):
        print("Meow! Meow!")


def print_sound(animal: Animal):
    animal.sound()
    # This function takes an Animal object and calls its sound method


my_animal = Animal("Generic Animal")
print_sound(my_animal)  # Output: This animal makes a sound
my_dog = Dog("Buddy")
print_sound(my_dog)  # Output: Woof! Woof!
my_cat = Cat("Whiskers")
print_sound(my_cat)  # Output: Meow! Meow!


"""Exercise"""


class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} is coordinating projects of the company.")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        # Call the constructor of the parent class (Employee)
        self.project = project

    def coordinate_projects(self):
        print(f"{self.name} is coordinating one project of the company.")


class Developer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        # Call the constructor of the parent class (Employee)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

    def add(self, employee: Employee):
        print(
            f"A developer cannot add employees. {employee.name} will not be added")
        # Overriding the add method to prevent adding employees


my_manager = Manager(1, "Alice")
my_project_manager = ProjectManager(2, "Bob", "Project A")
my_project_manager2 = ProjectManager(3, "Charlie", "Project B")
my_developer = Developer(4, "Dave", "Python")
my_developer2 = Developer(5, "Eve", "Java")
my_developer3 = Developer(6, "Frank", "JavaScript")
my_developer4 = Developer(7, "Grace", "C++")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_developer)
my_project_manager.add(my_developer2)
my_project_manager2.add(my_developer3)
my_project_manager2.add(my_developer4)

my_developer.add(my_project_manager2)  # This will not add the developer

my_developer.code()  # Output: Dave is coding in Python
# Output: Bob is coordinating one project of the company.
my_project_manager.coordinate_projects()
# Output: Alice is coordinating projects of the company.
my_manager.coordinate_projects()
my_manager.print_employees()  # Output: Bob, Charlie
my_project_manager.print_employees()  # Output: Dave, Eve
# Output: (no output, as the developer cannot add employees)
my_developer.print_employees()
# Output: (no output, as the developer cannot add employees)
