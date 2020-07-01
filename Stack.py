"""
We can implement Stack - with push(),pop() and peek() using array or list.
Due to operations that need to be performed in case the initial memory runs out,
Linked List is a better suited implementation technique.
"""

import Node


class Stack:
    def __init__(self):
        self.top_element = None

    def peek(self):
        return self.top_element.get_value()

    def push(self, val):
        item = Node(val)
        item.set_next_node(self.top_element)
        self.top_element = item

    def pop(self):
        remove_item = self.top_element.get_value()
        self.top_element = self.top_element.get_next_node()
        return remove_item
