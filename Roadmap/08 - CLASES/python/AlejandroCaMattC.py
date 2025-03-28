"""Classes"""


class Programmer:
    """Class to create a programmer object."""

    surname: str = None

    def __init__(self, name: str, age: int, language: list):
        self.name = name
        self.age = age
        self.language = language

    def print(self):
        print(
            f"Name: {self.name} | Surname: {self.surname} | Age: {self.age} | Language: {self.language}")


my_programmer = Programmer("Alejandro", 39, ["Python", "JavaScript", "C++"])
my_programmer.print()
my_programmer.surname = "Campos"
my_programmer.print()
my_programmer.age = 40
my_programmer.print()


"""Exercise"""

# LIFO (Last In First Out) - Stack


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.print()


# FIFO (First In First Out) - Queue

class Queue:
    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)

    def deequeue(self):
        return self.queue.pop(0) if self.count() > 0 else None

    def count(self):
        return len(self.queue)

    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
print(my_queue.count())
my_queue.print()
