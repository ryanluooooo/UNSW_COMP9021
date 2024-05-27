import sys
from math import sqrt,ceil
def is_prime(n):
    if n == 2:
        return True
    for i in range(2,ceil(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

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
    if a != b:
        last_prime = 0
        next_prime = 0
        for i in range(a, b+1):
            if is_prime(i):
                last_prime = next_prime
                next_prime = i
                if last_prime != 0 and next_prime - last_prime - 1 > max_gap:
                    #print((last_prime,next_prime))
                    max_gap = next_prime-last_prime-1
        if last_prime == 0:
            max_gap = 0
    print(f'The maximum gap between successive prime numbers in that interval is {max_gap}')




if __name__ == '__main__':
    import doctest
    doctest.testmod()
