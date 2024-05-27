# -*- encoding:utf-8 -*-
# Given a nonzero natural number q, a q-arithmetic progression
# is a sequence of the form x, x + q, x + 2q, ... x + nq
# for some integer x and some natural number n.
#
# q-arithmetic progressions are output from smallest to largest
# first element.
#
# You can assume that the function is called with L a list of integers
# and q an integer at least equal to 1.


from random import seed, randint
from collections import defaultdict


def arithmetic_progressions(L, q):
    '''
    >>> arithmetic_progressions([3, 3, 3, 3], 4)
    The longest 4-arithmetic progressions of members of L are:
    3
    >>> arithmetic_progressions([7, 3], 4)
    The longest 4-arithmetic progressions of members of L are:
    3 -- 7
    >>> arithmetic_progressions([1, 3, 5, 7, 1, 3, 5, 7], 2)
    The longest 2-arithmetic progressions of members of L are:
    1 -- 3 -- 5 -- 7
    >>> arithmetic_progressions([50, 0, 5, 10, 12, 7, 2, 25, 20, 30, 60, 65], 5)
    The longest 5-arithmetic progressions of members of L are:
    0 -- 5 -- 10
    2 -- 7 -- 12
    20 -- 25 -- 30
    >>> arithmetic_progressions([8, -6, 0, 8, 0, 11, 0, 11, -6, -6, 11, 8, 11],\
10)
    The longest 10-arithmetic progressions of members of L are:
    -6
    0
    8
    11
    >>> arithmetic_progressions([10, 9, -1, -2, -6, 0, 9, 4, -6, -2, 7, 3,\
-5, -5, 2, -7, -6, 8], 5)
    The longest 5-arithmetic progressions of members of L are:
    -7 -- -2 -- 3 -- 8
    -6 -- -1 -- 4 -- 9
    >>> seed(0); L = [randint(-100, 100) for _ in range(20000)]
    >>> arithmetic_progressions(L, 19)
    The longest 19-arithmetic progressions of members of L are:
    -100 -- -81 -- -62 -- -43 -- -24 -- -5 -- 14 -- 33 -- 52 -- 71 -- 90
    -99 -- -80 -- -61 -- -42 -- -23 -- -4 -- 15 -- 34 -- 53 -- 72 -- 91
    -98 -- -79 -- -60 -- -41 -- -22 -- -3 -- 16 -- 35 -- 54 -- 73 -- 92
    -97 -- -78 -- -59 -- -40 -- -21 -- -2 -- 17 -- 36 -- 55 -- 74 -- 93
    -96 -- -77 -- -58 -- -39 -- -20 -- -1 -- 18 -- 37 -- 56 -- 75 -- 94
    -95 -- -76 -- -57 -- -38 -- -19 -- 0 -- 19 -- 38 -- 57 -- 76 -- 95
    -94 -- -75 -- -56 -- -37 -- -18 -- 1 -- 20 -- 39 -- 58 -- 77 -- 96
    -93 -- -74 -- -55 -- -36 -- -17 -- 2 -- 21 -- 40 -- 59 -- 78 -- 97
    -92 -- -73 -- -54 -- -35 -- -16 -- 3 -- 22 -- 41 -- 60 -- 79 -- 98
    -91 -- -72 -- -53 -- -34 -- -15 -- 4 -- 23 -- 42 -- 61 -- 80 -- 99
    -90 -- -71 -- -52 -- -33 -- -14 -- 5 -- 24 -- 43 -- 62 -- 81 -- 100
    '''

    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
    l=sorted(L)
    result_dict=defaultdict(list)
    result=[]
    for i in range(len(l)):
        if l[i] not in result_dict:
            result_dict[l[i]].append(l[i])
    for key, value in result_dict.items():
        for i in range(len(l)):
            if l[i] != key and (l[i] - key) % q == 0 and l[i] - key > 0 and l[i] not in result_dict[key]:
                result_dict[key].append(l[i])
    for key, value in result_dict.items():
        ans = ''
        if value:
            length = len(value)
            for i in range(length):
                if i == 0:
                    ans += str(value[i])
                else:
                    ans += ' -- '
                    ans += str(value[i])
        print(ans)







if __name__ == '__main__':
    import doctest
    doctest.testmod()