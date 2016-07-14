"""Merge sort - Divide and Conquer!
Efficiency: O(nlog(n))
Space efficiency: O(n)"""
import sys
import ast
import random

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    midpoint = len(arr) / 2
    return merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))

def merge(arrLeft, arrRight):
    mergedArr = []
    while len(arrLeft) > 0 and len(arrRight) > 0:
        if arrLeft[0] < arrRight[0]:
            mergedArr.append(arrLeft.pop(0))
        else:
            mergedArr.append(arrRight.pop(0))
    if len(arrLeft) > 0:    #remaining elements are sorted so add them the end
        mergedArr.extend(arrLeft)
    else:
        mergedArr.extend(arrRight)
    return mergedArr

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
    print merge_sort(inputList)
