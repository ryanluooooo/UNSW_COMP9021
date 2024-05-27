import sys
from math import sqrt


def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0
    # Insert your code here
    L = []
    if a%2:
        for i in range(a,b+1,2):
            if is_prime(i):
                L.append(i)      
                
    else:
        for i in range(a+1,b+1,2):
            if is_prime(i):
                L.append(i)
    L1 = []
    for j in range(len(L)-1):
        L1.append(L[j+1]-L[j])
    if len(L1) == 0:
        max_gap = 0
    else:
        max_gap = max(L1)-1



    
    print('The maximum gap between successive prime numbers in that interval is', max_gap)
    


def is_prime(n):
    return all(n%d for d in range(3,round(sqrt(n))+1,2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
