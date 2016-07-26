"""BinaryTree.
- Search is linear, O(n).
- Insert Worst case is height of tree, which is O(log(n)).
- Deleting is linear, O(n).
Code based on practice excercise on Udacity."""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root, "")[:-1]  #slices all elements except the last as its a "-" symbol

    def preorder_search(self, start, find_val):
        """Helper method - used to create a
        recursive search solution."""
        if start is None:   #base case
            return False
        if start.value == find_val:
            return True
        else:
            return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

    def preorder_print(self, start, traversal):
        """Helper method - used to create a
        recursive print solution."""
        if start is None:
            return traversal
        traversal += (str(start.value) + "-")
        traversal = self.preorder_print(start.left, traversal)
        traversal = self.preorder_print(start.right, traversal)
        return traversal
