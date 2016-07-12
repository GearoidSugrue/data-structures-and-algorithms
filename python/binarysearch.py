"""Binary search in Python.
Efficiency is O(log(n))"""
#coded with the help of Udacity :D

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
            high = middle -1
        else:
            return middle
    return -1
