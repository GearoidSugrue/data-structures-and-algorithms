"""A FIFO queue implementd in Python"""
#based on code provided from Udacity

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        """Adds the new element to the end of the queue"""
        self.storage.append(new_element)

    def peek(self):
        """Returns the oldest element without removing it from the queue"""
        return self.storage[0]


    def dequeue(self):
        """Removes and returns the oldest element from the queue"""
        return self.storage.pop(0)
