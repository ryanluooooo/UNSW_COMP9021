# Will be tested only with positive integers for for_seed and upper_bound,
# and a strictly positive integer for size.
#
# Exploration can follow up to 8 directions
# (two horizontally, two vertically, and four diagonally).
#
# Travelling from m to n means starting from a cell that stores m,
# moving to a (horizontally, vertically or diagonally) neighbouring
# cell that stores m + 1, then moving to a (horizontally, vertically
# or diagonally) neighbouring cell hat stores m + 2... and eventually
# reaching a cell that stores n.
#
# Most of the code is written already, and there are not many statements
# left for you to write...

from random import seed, randrange


def travel(for_seed, size, upper_bound):
    '''
    >>> travel(0, 2, 0)
    The grid is:
    * * * *
    * 0 0 *
    * 0 0 *
    * * * *
    It is possible to travel from 0 to 0.
    >>> travel(0, 3, 1)
    The grid is:
    * * * * *
    * 1 1 0 *
    * 1 1 1 *
    * 1 1 1 *
    * * * * *
    It is possible to travel from 0 to 1.
    It is possible to travel from 1 to 1.
    >>> travel(0, 4, 4)
    The grid is:
    * * * * * *
    * 3 3 0 2 *
    * 4 3 3 2 *
    * 3 2 4 1 *
    * 4 1 2 1 *
    * * * * * *
    It is possible to travel from 0 to 0, but not from 0 to 1.
    It is possible to travel from 1 to 4.
    It is possible to travel from 2 to 4.
    It is possible to travel from 3 to 4.
    It is possible to travel from 4 to 4.
    >>> travel(0, 6, 8)
    The grid is:
    * * * * * * * *
    * 6 6 0 4 8 7 *
    * 6 4 7 5 3 8 *
    * 2 4 2 1 4 8 *
    * 2 4 1 1 5 7 *
    * 8 1 5 6 5 3 *
    * 8 7 7 8 4 0 *
    * * * * * * * *
    It is possible to travel from 0 to 0, but not from 0 to 1.
    It is possible to travel from 1 to 2, but not from 1 to 3.
    It is possible to travel from 2 to 2, but not from 2 to 3.
    It is possible to travel from 3 to 8.
    It is possible to travel from 4 to 8.
    It is possible to travel from 5 to 8.
    It is possible to travel from 6 to 8.
    It is possible to travel from 7 to 8.
    It is possible to travel from 8 to 8.
    >>> travel(2, 5, 4)
    The grid is:
    * * * * * * *
    * 0 0 0 2 1 *
    * 2 2 4 1 4 *
    * 0 4 1 3 3 *
    * 4 2 4 3 4 *
    * 2 0 0 2 3 *
    * * * * * * *
    It is possible to travel from 0 to 2, but not from 0 to 3.
    It is possible to travel from 1 to 2, but not from 1 to 3.
    It is possible to travel from 2 to 4.
    It is possible to travel from 3 to 4.
    It is possible to travel from 4 to 4.
    '''
    seed(for_seed)
    values = set()
    grid = [['*' for _ in range(size + 2)] for _ in range(size + 2)]
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            value = randrange(upper_bound + 1)
            values.add(value)
            grid[i][j] = value
    print('The grid is:')
    for row in grid:
        print(*row)
    upper_bound = max(values)
    from_to = {_from: _from for _from in values}
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            from_to[grid[i][j]] = max(from_to[grid[i][j]],
                                      explore_from(grid, upper_bound, i, j)
                                     )
    for _from in from_to:
        _to = from_to[_from]
        print(f'It is possible to travel from {_from} to {_to}', end='')
        if _to != upper_bound:
            print(f', but not from {_from} to {_to + 1}', end='')
        print('.')
    
def explore_from(grid, upper_bound, i, j):
    return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
