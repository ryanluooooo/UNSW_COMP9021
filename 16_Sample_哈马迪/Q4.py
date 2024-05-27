
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here

# Possibly define other functions

    
if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    is_heterosquare([[1, 2, 3, 4], \
                     [5, 6, 7, 8], \
                     [9, 10, 11, 12], \
                     [13, 14, 15, 16]])
