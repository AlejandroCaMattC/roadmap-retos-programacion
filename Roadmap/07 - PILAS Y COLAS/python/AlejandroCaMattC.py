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