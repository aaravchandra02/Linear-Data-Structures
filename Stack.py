"""
We can implement Stack - with push(),pop() and peek() using array or list.
Due to operations that need to be performed in case the initial memory runs out,
Linked List is a better suited implementation technique.
"""

import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_element = None
        self.size = 0
        self.limit = limit

    def peek(self):
        if(size > 0):
            return self.top_element.get_value()
        else:
            print("Sorry the Stack is empty\n")

    def push(self, val):
        if self.has_space():
            item = Node(val)
            item.set_next_node(self.top_element)
            self.top_element = item
            self.size += 1
        else:
            print("Sorry Stack is Full\n")

    def pop(self):
        if not self.is_empty():
            remove_item = self.top_element
            self.top_element = self.top_element.get_next_node()
            self.size -= 1
            return remove_item.get_value()
        else:
            print("Sorry the Stack is empty\n")

    def has_space(self):
        if self.size < self.limit:
            return True
        else:
            return False

    def is_empty(self):
        if self.size > 0:
            return False
        else:
            return True
