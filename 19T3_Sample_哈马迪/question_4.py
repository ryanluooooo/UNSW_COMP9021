# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 4
from itertools import compress

def get_all_prime(n):
    if n<2:
        return 0
    if n==2:
        return[2]
    if n>2:
        sieve =bytearray([True])*(n//2)
        for i in range(3, int(sqrt(n))+1,2):
            if sieve[i//2]:
                sieve[i*i//2::i]=bytearray((n-i*i-1)//(2*i)+1)
        return ([2,*compress(range(3,n,2),sieve[1:])])

'''
Will be tested with a at equal equal to 2 and b at most equal to 10_000_000.
'''

import sys
from math import sqrt


def f(a, b):
    '''
    >>> f(2, 2)
    There is a unique prime number beween 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number beween 4 and 4.
    >>> f(14, 16)
    There is no prime number beween 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    '''
    
    # Insert your code here
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
