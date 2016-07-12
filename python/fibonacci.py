"""Fibonacci sequence implemented both iteratively and recursively"""
#coded with help from Udacity

def get_fib_iteritive(pos):
    """Gets the Fibonacci number at the specified position using iteration"""
    first = 0
    second = 1
    for fib_pos in range(pos - 1):
        second = first + second #set second as the sum of the previous two
        first = second - first  #set first equal the previous second
        print second
    return second

def get_fib_recursive(pos):
    """Gets the Fibonacci number at the specified position using recursion"""
    if position == 0 or position == 1:   #base case
        return position

    return get_fib(position - 2) + get_fib(position - 1)
