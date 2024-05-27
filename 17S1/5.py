import sys
from math import sqrt,ceil
from itertools import compress

def is_prime(n):
    if n == 2:
        return True

    for i in range(2,ceil(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    # Only used to test odd numbers.




def f(a, b):
    '''
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The number of prime numbers between 3 and 3 included is 1
    >>> f(4, 4)
    The number of prime numbers between 4 and 4 included is 0
    >>> f(2, 5)
    The number of prime numbers between 2 and 5 included is 3
    >>> f(2, 10)
    The number of prime numbers between 2 and 10 included is 4
    >>> f(2, 11)
    The number of prime numbers between 2 and 11 included is 5
    >>> f(1234, 567890)
    The number of prime numbers between 1234 and 567890 included is 46457
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    '''

    count = 0
    for i in range(a,b+1):
        if is_prime(i):
            count += 1

    print(f"The number of prime numbers between {a} and {b} included is {count}")

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    f(89,5678901)
