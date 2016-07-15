"""Quick sort - Divide and Conquer!
Worst Case: O(n^2)
Average and Best: O(nlog(n))
Space: O(1)"""

import sys
import ast
import random

def quick_sort(arr):#lists in Python are passed by reference
    if len(arr) < 2:#base case
        return arr
    pivot = len(arr) - 1
    i = 0
    while i < pivot:
        if  arr[i] > arr[pivot]:
            arr[i], arr[pivot - 1] = arr[pivot - 1], arr[i]
            arr[pivot - 1], arr[pivot] = arr[pivot], arr[pivot - 1]
            pivot -= 1
        else:
            i += 1
    #Using list[x:y], i.e. slicing, does not create new list.
    #Slicing uses references from the original list.
    return quick_sort(arr[:pivot]) + \
            arr[pivot:pivot + 1] + \
            quick_sort(arr[pivot + 1:])


if __name__ == '__main__':
    """Simplifies calling from command line.
    __name__ stores the name of the module calling script.
    __name__ is equal to '__main__' if called from command line."""
    if len(sys.argv) > 1:
        #ast.literal_eval() only considers a small subset of syntax to be valid
        inputList = ast.literal_eval(sys.argv[1])#parses input to type list
        print "Unsorted list"
    else:
        #if no list is provided as an argument, it generates a random list
        inputList = random.sample(xrange(1, 101), 20)
        print "Random unsorted list"
    print inputList
    print "Sorted list"
    print quick_sort(inputList)
