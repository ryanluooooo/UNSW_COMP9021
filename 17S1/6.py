''' Hint in the form of syntactic notes:
    str(n) converts a number n to a string.
    set(s) converts a string s to a set of characters.
    len() returns the number of elements in its argument, e.g, a string, or a set.
    
    S1 | S2 returns the union of two sets S1 and S2.

'''

import sys


def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that
    every digit occurs at most once in i, j and i * j.
    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(32, 49)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(30, 50)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(40, 80)
    48 * 65 = 3120 is a solution
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    68 * 74 = 5032 is a solution
    >>> f(50, 110)
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    53 * 92 = 4876 is a solution
    57 * 86 = 4902 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    59 * 108 = 6372 is a solution
    62 * 87 = 5394 is a solution
    68 * 74 = 5032 is a solution
    69 * 108 = 7452 is a solution
    72 * 95 = 6840 is a solution
    74 * 85 = 6290 is a solution
    '''
    for i in range(a, b ):
        for j in range(i, b + 1):
            k = i * j
            if i <= j and len(set(str(i)))  == len(str(i))\
                    and len(set(str(j)))  == len(str(j))\
                    and len(set(str(k)))  == len(str(k)) \
                    and len(set(str(i) + str(j) + str(k))) == len(str(i) + str(j) + str(k)):

                print(f"{i} * {j} = {k} is a solution")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
