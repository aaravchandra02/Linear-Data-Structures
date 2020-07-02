"""
We can implement Queue - with enqueue(),dequeue() and peek() using array or list.
Due to operations that need to be performed in case the initial memory of array runs out,
Linked List is a better suited implementation technique.
"""

from node import Node


class Queue:

    # only for bounded queues a limit is set, no limit is set for other ype of queues.
    def __init__(self, limit=None):
        self.front_element = None
        self.back_element = None
        self.limit = limit
        self.size = 0

    def get_size(self):
        return self.size

    def has_space(self):
        if self.limit == None:
            return True
        return self.get_size() >= self.limit

    def is_empty(self):
        return self.get_size() == 0

    def peek(self):
        if not self.is_empty():
            return self.front_element.get_value()
        print("\nSorry the Queue is empty\n")

    def enqueue(self, val):
        if self.has_space():
            to_enqueue = Node(val)
            print(f"Adding {to_enqueue.get_value()} to the queue!")

            # If the queue is empty before adding, make first and last element both as first element. If not then Node class fn wont work.
            if self.is_empty():
                self.front_element = to_enqueue
                self.back_element = to_enqueue
            else:  # When queue already has other elements
                self.back_element.set_next_node(to_enqueue)
                self.back_element = to_enqueue
            self.size += 1
        else:
            print("\nSorry the Queue is Full\n")

    def dequeue(self):
        if not self.is_empty():
            to_dequeue = self.peek()  # getting the front element
            print(f"Deleting {to_dequeue} from the queue!")

            # Check if the element to be removed is the last element in the Queue
            if self.get_size() == 1:  # set front and back of the queue as 'None'
                self.back_element = None
                self.front_element = None
            else:
                self.front_element = self.front_element.get_next_node()
            self.size -= 1
            return to_dequeue
        else:
            print("\nSorry the Queue is empty\n")

    def print_it(self):
        s = ""
        curr = self.front_element
        while(curr):
            s = str(curr.get_value()) + " " + s
            curr = curr.get_next_node()
        if s:
            print(f"The queue is as follow:\n{s}\n")
        else:
            print(f"\nQueue is empty right now\n")


a = Queue()
a.print_it()

a.enqueue(2)
a.print_it()

a.enqueue(5)
print(f"Size = {a.get_size()}\nOn Top = {a.peek()}\n")
a.print_it()

print(f"Dequeued element = {a.dequeue()}\nSize = {a.get_size()}\n")
a.print_it()

print(f"Dequeued element = {a.dequeue()}\nSize = {a.get_size()}\n")

print(f"Dequeued element = {a.dequeue()}\nSize = {a.get_size()}\n")
