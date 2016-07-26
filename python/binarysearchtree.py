"""Binary Search Tree.
- Every node has max 2 children.
- Sorted so every element on left is smaller while every element on right is greater.
- Average Search and Insert is the height of the tree. Therefore average is O(log(n)).
- Deleting is linear.
Code based on practice excercise on Udacity."""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bst_insert(self.root, new_val)

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_insert(self, start, new_val):
        if start is None:   #base case
            start = Node(new_val)
        if new_val < start.value:
            self.bst_insert(start.left, new_val)
        elif new_val > start.value:
            self.bst_insert(start.right, new_val)

    def bst_search(self, start, find_val):
        if start is None:   #base case
            return False
        if find_val < start.value:
            return self.bst_search(start.left, find_val)
        elif find_val > start.value:
            return self.bst_search(start.right, find_val)
        else:
            return True
