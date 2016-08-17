"""Max Heap - where max value is always at the top of the tree (array).
Both Max value delete and peek are constant time O(1).
Insert is ...
Worst case Searching is linear O(n).
Average case Searching is O(n/2) which approx. is O(n).

Notes:
Using an array saves space as only value and index are stored.
Array needs to be sorted in order to use an array instead of tree.
"""


class Heap(object):
    def __init__(self):
        # The dummy element at index 0 ensures our parent-child aritmithic works
        # e.g. parent_index = child_index / 2
        self.tree_arr = [0]
        self.cur_size = 0

    def insert(self, new_value):
        """Adds a value to the tree"""
        self.tree_arr.append(new_value)
        self.cur_size += 1
        self.perc_up(self.cur_size) # Quicker to add to end and then move it up

    def delete_max(self):
        """Deletes the largest element from the tree."""
        if self.cur_size > 1:
            # The last element becomes the root element
            self.tree_arr[1] = self.tree_arr.pop()
            self.cur_size -= 1
            self.perc_down(1)  # Move down the tree to keep it balanced
        elif self.cur_size == 1:
            self.tree_arr.pop()
            self.cur_size -= 1

    def peek_max(self):
        """Return the maximum element in the tree."""
        if self.cur_size >= 1:
            return self.tree_arr[1]  # The root, ie max, of the tree is index 1

    def heap_pop_max(self):
        """Returns and removes the largest value"""
        if self.cur_size < 1:
            return
        max = self.tree_arr[1]
        self.delete_max()
        return max

    def perc_up(self, child):
        """Move the specified node up the tree until it has a larger parent."""
        if child <= 1:
            return
        parent = child // 2
        if self.tree_arr[child] > self.tree_arr[parent]:
            self.tree_arr[child], self.tree_arr[parent] \
            = self.tree_arr[parent], self.tree_arr[child]
            self.perc_up(parent)
        else:
            return

    def perc_down(self, parent):
        """"Move the node down the tree until it is larger than both of its
        children.
        """
        if parent * 2 > self.cur_size:  # Check that there is at least 1 child
            return
        max_child = self.max_child(parent)
        if self.tree_arr[parent] < self.tree_arr[max_child]:
            self.tree_arr[parent], self.tree_arr[max_child] \
            = self.tree_arr[max_child], self.tree_arr[parent]
            self.perc_down(max_child)

    def max_child(self, parent):
        """Return a parent's largest child."""
        left_child = parent * 2
        right_child = parent*2 + 1
        # There is no right_child if it is greater than current tree size
        if right_child > self.cur_size:
            return left_child
        else:
            if self.tree_arr[left_child] > self.tree_arr[right_child]:
                return left_child
            else:
                return right_child

    def search_heap(self, value):
        """Return the index of an value if it is in the heap.
        Returns -1 if the value is not in the heap.
        """
        if self.tree_arr is None:  # Sanity check!
            return -1
        i = 1
        while i < self.cur_size:
            # Not possible for value be any lower in the tree so return -1
            if value > self.tree_arr[i]:
                return -1
            elif value == self.tree_arr[i]:
                return i
            i += 1
        return -1  # Only reached if value was not found in the tree_arr

    def build_heap(self, alist):
        """Creates a max heap from a list.

        Height of tree is nlogn. The heap can be built in linear O(n)."""
        i = len(alist) // 2 #the '//' is used for truncating division
        self.cur_size = len(alist)
        self.tree_arr = [0] + alist[:]
        while i > 0: # Start in the middle of the tree and work up to the root
            # Ensures the smallest node is pushed down the tree as far as it can
            self.perc_down(i)
            i -= 1

rand_list = [9, 4, 6, 3, 7, 2, 1, 5, 12, 8] #[9,5,6,2,3]#[9, 4, 6, 3, 7, 2, 1, 5, 12, 8]
print("Unsorted list")
print(rand_list)

heap = Heap()
heap.build_heap(rand_list)
print("Sorted heap - the first element (0) is a dummy element)")
print(heap.tree_arr)

print("Max value")
print(heap.peek_max())

heap.delete_max()
print("Max value after delete")
print(heap.peek_max())

print("Search for 4")
print(heap.search_heap(4))
print("Search for 20 - should be -1")
print(heap.search_heap(20))

print("Heap after adding values: 20, 10, 11")
heap.insert(20)
heap.insert(10)
heap.insert(11)
print(heap.tree_arr)

print("All values popped off the top of heap")
max = heap.heap_pop_max()
while max is not None:
    print(max)
    max = heap.heap_pop_max()
