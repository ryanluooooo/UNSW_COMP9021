#  You can assume that i and j are both between 0 and 9 included.
#  i is the row number (indexed from top to bottom),
#  j is the column number (indexed from left to right)
#  of the displayed grid.
    

from random import seed, randrange


def area(for_seed, sparsity, i, j):
    '''
    >>> area(0, 1, 5, 5)
    The grid is:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    The area of the largest empty region of the grid
    containing the point (5, 5) is: 0
    >>> area(0, 1000, 5, 5)
    The grid is:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    The area of the largest empty region of the grid
    containing the point (5, 5) is: 100
    >>> area(0, 3, 6, 2)
    The grid is:
    0 0 1 0 0 0 0 0 0 0
    0 1 0 1 0 1 1 0 0 0
    0 0 1 0 1 0 1 0 0 0
    0 1 0 0 0 0 0 1 0 0
    0 0 0 1 0 1 1 0 0 0
    0 0 1 0 0 0 1 0 0 0
    1 1 0 1 1 1 0 0 1 1
    0 0 0 1 0 0 0 0 1 0
    0 0 1 0 0 0 0 0 1 0
    0 0 0 1 0 1 1 1 1 0
    The area of the largest empty region of the grid
    containing the point (6, 2) is: 9
    >>> area(0, 2, 9, 5)
    The grid is:
    0 0 1 0 0 0 0 0 0 1
    1 0 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 0 0 0 1
    1 1 0 1 0 0 1 0 1 1
    1 1 1 0 1 1 0 0 1 0
    0 1 0 1 0 0 1 0 0 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 0 0 0
    0 0 1 0 1 0 0 1 1 1
    0 1 1 0 1 0 0 1 1 1
    The area of the largest empty region of the grid
    containing the point (9, 5) is: 4
    >>> area(0, 2, 2, 7)
    The grid is:
    0 0 1 0 0 0 0 0 0 1
    1 0 1 1 0 1 0 1 1 0
    0 1 0 0 0 1 0 0 0 1
    1 1 0 1 0 0 1 0 1 1
    1 1 1 0 1 1 0 0 1 0
    0 1 0 1 0 0 1 0 0 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 0 0 0
    0 0 1 0 1 0 0 1 1 1
    0 1 1 0 1 0 0 1 1 1
    The area of the largest empty region of the grid
    containing the point (2, 7) is: 22
    >>> area(0, 4, 2, 7)
    The grid is:
    0 0 1 0 0 0 0 0 0 0
    0 0 0 1 0 0 0 1 1 0
    0 1 0 0 0 0 0 0 0 1
    1 1 0 1 0 0 0 0 1 0
    0 0 0 0 1 1 0 0 1 0
    0 1 0 0 0 0 1 0 0 0
    0 0 0 0 1 0 0 1 1 0
    0 1 1 0 0 0 0 0 0 0
    0 0 1 0 1 0 0 0 0 1
    0 1 0 0 0 0 0 1 1 0
    The area of the largest empty region of the grid
    containing the point (2, 7) is: 73
    '''
    seed(for_seed)
    grid = [[int(randrange(sparsity) == 0) for _ in range(10)]
                for _ in range(10)
           ]
    print('The grid is:')
    for row in grid:
        print(*row)
    print('The area of the largest empty region of the grid')
    print(f'containing the point ({i}, {j}) is: ', end='')
    # INSERT YOUR CODE HERE

# POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest
    doctest.testmod()
