"""Binary search in Python.
Efficiency is O(log(n))"""
#coded with the help of Udacity :D

import sys
import ast

def binary_search(input_array, value):
    """Returns the index of value, or -1 if the value
    doesn't exist in the list."""
    if not input_array:
        return -1

    low = 0
    high = len(input_array) - 1
    while low <= high:
        middle = (low + high) / 2
        if input_array[middle] < value:
            low = middle + 1
        elif input_array[middle] > value:
            high = middle - 1
        else:
            return middle
    return -1

if __name__ == '__main__':
    if len(sys.argv) > 2:
        #ast.literal_eval() only considers a small subset of syntax to be valid
        inputList = ast.literal_eval(sys.argv[1])#parses input to type list
        inputValue = ast.literal_eval(sys.argv[2])#parses input to int
        print binary_search(inputList, inputValue)
