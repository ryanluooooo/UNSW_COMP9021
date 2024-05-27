# On each line of the form "x plus y equals z", x, y and z are
# possibly padded with 0s on the left; in particular, the number of
# digits in both x and y is the maximum of the number of digits in
# the first input, m, and the number of digits in the second input, n.
#
# The third argument, direction, is one of 'L' or 'R',
# for left or right rotation.


def f(m, n, direction):
    '''
    >>> f(0, 0, 'L')
    0 plus 0 equals 0
    >>> f(0, 0, 'R')
    0 plus 0 equals 0
    >>> f(1234, 0, 'L')
    1234 plus 0000 equals 1234
    2341 plus 0000 equals 2341
    3412 plus 0000 equals 3412
    4123 plus 0000 equals 4123
    >>> f(1234, 0, 'R')
    1234 plus 0000 equals 1234
    4123 plus 0000 equals 4123
    3412 plus 0000 equals 3412
    2341 plus 0000 equals 2341
    >>> f(2134, 3412, 'L')
    2134 plus 3412 equals 5546
    1342 plus 4123 equals 5465
    3421 plus 1234 equals 4655
    4213 plus 2341 equals 6554
    >>> f(2134, 3412, 'R')
    2134 plus 3412 equals 5546
    4213 plus 2341 equals 6554
    3421 plus 1234 equals 4655
    1342 plus 4123 equals 5465
    >>> f(213287, 3166, 'L')
    213287 plus 003166 equals 0216453
    132872 plus 031660 equals 0164532
    328721 plus 316600 equals 0645321
    287213 plus 166003 equals 0453216
    872132 plus 660031 equals 1532163
    721328 plus 600316 equals 1321644
    >>> f(8901, 3419306, 'R')
    0008901 plus 3419306 equals 03428207
    1000890 plus 6341930 equals 07342820
    0100089 plus 0634193 equals 00734282
    9010008 plus 3063419 equals 12073427
    8901000 plus 9306341 equals 18207341
    0890100 plus 1930634 equals 02820734
    0089010 plus 4193063 equals 04282073
    >>> f(800095, 900003, 'L')
    800095 plus 900003 equals 1700098
    000958 plus 000039 equals 0000997
    009580 plus 000390 equals 0009970
    095800 plus 003900 equals 0099700
    958000 plus 039000 equals 0997000
    580009 plus 390000 equals 0970009
    '''
    # INSERT YOUR CODE HERE    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
