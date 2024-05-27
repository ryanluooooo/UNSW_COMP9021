# A cross is a pattern of the form
#           *   *
#             *
#           *   *
#
# Given a cross made of 5 digits, the value of the cross is the sum
# of those 5 digits; for instance, the value of
#           6   0
#             8
#           6   7
# is 27.
#
# Note that in a grid of size n by n with n >= 3,
# there are (n-2) * (n-2) many crosses.
#
# In
#    6 6 0 4 8
#    7 6 4 7 5
#    9 3 8 2 4
#    2 1 9 4 8
#    9 2 4 1 1
# there is a unique cross of highest value (31), which is:
#    . . . . .
#    . . . . .
#    9 . 8 . .
#    . 1 . . .
#    9 . 4 . .
# In
#    6 6 0 4 8 7 6 4
#    7 5 9 3 8 2 4 2
#    1 9 4 8 9 2 4 1
#    1 5 7 8 1 5 6 5
#    9 3 8 7 7 8 4 0
#    8 0 1 6 0 9 7 5
#    3 5 1 3 9 3 3 2
#    8 7 1 1 5 8 7 1
# there are 2 crosses of highest value (36), which are:
#    . 6 . 4 . . . .
#    . . 9 . . . . .
#    . 9 . 8 . . . .
#    . . . . . . . .
#    . . . . . . . .
#    . . . . . . . .
#    . . . . . . . .
#    . . . . . . . .
# and
#    . . . . . . . .
#    . . . . . . . .
#    . . 4 . 9 . . .
#    . . . 8 . . . .
#    . . 8 . 7 . . .
#    . . . . . . . .
#    . . . . . . . .
#    . . . . . . . .
#
# The code for the output is completely written already, so
# the task is only to compute the correct values for
# max_value and nb_of_crosses_of_max_value.
#
# You can assume that the function is called with an integer as first
# argument and an integer at least equal to 3 as second argument.


from random import seed, randrange


def cross(for_seed, size):
    '''
    >>> cross(0, 3)
    6 6 0
    4 8 7
    6 4 7
    <BLANKLINE>
    The maximal value for a cross in the grid is: 27
    There is a unique cross of maximal value.
    >>> cross(0, 5)
    6 6 0 4 8
    7 6 4 7 5
    9 3 8 2 4
    2 1 9 4 8
    9 2 4 1 1
    <BLANKLINE>
    The maximal value for a cross in the grid is: 31
    There is a unique cross of maximal value.
    >>> cross(0, 8)
    6 6 0 4 8 7 6 4
    7 5 9 3 8 2 4 2
    1 9 4 8 9 2 4 1
    1 5 7 8 1 5 6 5
    9 3 8 7 7 8 4 0
    8 0 1 6 0 9 7 5
    3 5 1 3 9 3 3 2
    8 7 1 1 5 8 7 1
    <BLANKLINE>
    The maximal value for a cross in the grid is: 36
    There are 2 crosses of maximal value.
    '''
    seed(for_seed)
    grid = [[randrange(10) for _ in range(size)] for _ in range(size)]
    for row in grid:
        print(*row)
    print()
    max_value = 0
    nb_of_crosses_of_max_value = 0
    # INSERT YOUR CODE HERE
    print('The maximal value for a cross in the grid is:', max_value)
    if nb_of_crosses_of_max_value == 1:
        print('There is a unique cross', end=' ')
    else:
        print('There are',  nb_of_crosses_of_max_value, 'crosses', end=' ')
    print('of maximal value.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
