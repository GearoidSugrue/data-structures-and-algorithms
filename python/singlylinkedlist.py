"""Singly-linked list in Python"""

#should have a structure for elements which contains a value and the next element
#should have a head to refer to the first element in the list
#Methods: append, insert, get and delete

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None #the next element in the list, if there is one

class SinglyLinkedList(object):
    def __init__(self, head=None): #head (the 1st element) defaults to None if nothing passed in
        self.head = head

    def append(self, new_element):
        """Adds the element to the end of the LinkedList"""
        current = self.head
        if self.head:   #if there is a head element
            while current.next: #iterate through each element until you find one with no next element. ie find the last element
                current = current.next
                current.next = new_element #when the last element is reached, set its next element to new_element
        else:
            self.head = new_element #if no head, set new_element as head.

    def get_position(self, position):
        """Gets an element from a particular position.
        Returns "None" if position is not in the list."""
        if not self.head or position < 1:
            return None
        current = self.head
        i = 1
        while i < position and current:
            current = current.next
            i += 1
        return current

    def insert(self, new_element, position):
        """Inserts the new element into the position specified"""
        if not self.head or position < 1:
            return
        if position == 1:
            new_element == self.head
            self.head = new_element
        elif position > 1:
            i = 1
            current = self.head
            while i < position and current:
                if i == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                i += 1

    def delete(self, value):
        """Deletes the first node with a given value."""
        current = self.head
        preceding = None
        while current.value != value and current.next:
            preceding = current
            current = current.next
        if current.value == value:
            if preceding:
                preceding.next = current.next
            else:   #no preceding node means the value was in the head
                self.head = current.next
