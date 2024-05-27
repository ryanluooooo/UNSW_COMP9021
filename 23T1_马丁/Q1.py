# Consider a strictly positive integer. Omit all occurrences of 0,
# if any, and write what is left as d_1d_2...d_k.
# Returns the integer consisting of d_2 copies of d_1, followed
# by d_3 copies of d_2, ... followed by d_k copies of d_{k-1},
# followed by d_1 copies of d_k (note that when k = 1, that is
# d_1 copies of d_1).
#
# For instance, if the integer is 40025000170 then removing
# all occurrences of 0, it becomes 42517, and what is returned
# is the integer consisting of
# - 2 copies of 4,
# - followed by 5 copies of 2,
# - followed by 1 copy of 5,
# - followed by 7 copies of 1,
# - followed 4 copies of 7,
# so the integer 4422222511111117777
#
# You can assume that the function is called with a strictly
# positive integer as argument.


def transform(number):
    '''
    >>> transform(1)
    1
    >>> transform(12)
    112
    >>> transform(321)
    332111
    >>> transform(2143)
    2111144433
    >>> transform(3000)
    333
    >>> transform(40025000170)
    4422222511111117777
    '''
    return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
