from math import sqrt

def f(n, d):
    '''
    >>> f(2, 1)
    1 is not a proper factor of 2.
    >>> f(2, 2)
    2 is not a proper factor of 2.
    >>> f(16, 2)
    2 is a proper factor of 16 of mutiplicity 4.
    >>> f(100, 20)
    20 is a proper factor of 100 of mutiplicity 1.
    >>> f(8 ** 7 * 3 ** 5 * 11 ** 2, 8)
    8 is a proper factor of 61662560256 of mutiplicity 7.
    >>> f(3 ** 3 * 11 * 13 ** 2 * 40 ** 6, 8)
    8 is a proper factor of 205590528000000 of mutiplicity 6.
    '''
    # Insert your code here
    count = 0
    temp_n = n
    if d == 1 or d == n:
        print(f'{d} is not a proper factor of {n}.')
    else:
        while temp_n % d == 0:
                count += 1
                temp_n = temp_n // d
        print(f'{d} is a proper factor of {n} of mutiplicity {count}.')



if __name__ == '__main__':
    import doctest
    doctest.testmod()