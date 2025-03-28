"""Stacks and queues"""

# Stacks (LIFO)

stack = []
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")
print(stack)

stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

# Pop
print(stack.pop())
print(stack)

# Queues (FIFO)

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue)

# Pop
print(queue.pop())
print(queue)


"""Exercises"""


def web_navigation():

    stack = []

    while True:

        action = input("Add a URL of your choice: ")

        if action == "exit":
            print("Exiting the web browser...")
            break
        elif action == "forward":
            pass
        elif action == "back":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"You are currently on the web: {stack[len(stack) - 1]}")
        else:
            print("You are not on any web page.")


# web_navigation()

def shared_printer():
    queue = []

    while True:
        action = input("Add a document to the queue (or 'exit' to quit): ")

        if action == "exit":
            print("Exiting the printer...")
            break
        elif action == "print":
            if len(queue) > 0:
                print(f"Printing document: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Printing document: {queue}")


shared_printer()
