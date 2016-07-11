"""Stack using a LinkedList in Python"""
#based on code provided from Udacity

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None #the next element in the list, if there is one

class LinkedList(object):
    def __init__(self, head=None): #head (the 1st element) defaults to None if nothing passed in
        self.head = head

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """Puts an the new element at the top of the stack"""
        self.ll.insert_first(new_element)

    def pop(self):
        """Removes the element at the top of the stack and returns it"""
        return self.ll.delete_first()
