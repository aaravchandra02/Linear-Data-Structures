"""
We can implement Stack - with push(),pop() and peek() using array or list.
Due to operations that need to be performed in case the initial memory of array runs out,
Linked List is a better suited implementation technique.
"""

from node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_element = None
        self.size = 0
        self.limit = limit

    def peek(self):
        if not self.is_empty():
            return self.top_element.get_value()
        else:
            print("Sorry the Stack is empty\n")

    def push(self, val):
        if self.has_space():
            item = Node(val)
            item.set_next_node(self.top_element)
            self.top_element = item
            self.size += 1
            print(f"\nAdding {val} to the Stack!\n")
        else:
            print("Sorry Stack is Full\n")

    def pop(self):
        if not self.is_empty():
            remove_item = self.top_element
            self.top_element = self.top_element.get_next_node()
            self.size -= 1
            print(f"deleted '{remove_item.get_value()}' from the stack!\n")
            return remove_item.get_value()
        else:
            print("Sorry the Stack is empty\n")

    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True


# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print(f"The first pizza to be delivered is {pizza_stack.peek()}\n")
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()
