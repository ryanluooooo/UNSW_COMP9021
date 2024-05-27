import sys
from math import sqrt


def get_divisors(n):
    if n == 1:
        return [0]
    else:
        divisors = []
        for i in range(1,1+n//2):
            if n % i == 0:
                divisors.append(i)
        return divisors


def f(n):
    '''
    A number n is deficient if the sum of its proper divisors,
    1 included and itself excluded,
    is strictly smaller than n.
    
    >>> f(1)
    1 is deficient
    >>> f(2)
    2 is deficient
    >>> f(3)
    3 is deficient
    >>> f(6)
    6 is not deficient
    >>> f(29)
    29 is deficient
    >>> f(30)
    30 is not deficient
    >>> f(47)
    47 is deficient
    >>> f(48)
    48 is not deficient
    '''
    #input your code
    divisors = get_divisors(n)
    if sum(divisors) < n:
        print(f"{n} is deficient")
    else:
        print(f"{n} is not deficient")

def g(a, b):
    '''
    a and b are amicable if
    - the sum of the proper divisors of a, 1 included and a excluded, is equal to b, and
    - the sum of the proper divisors of b, 1 included and b excluded, is equal to a.
    
    >>> g(220, 284)
    220 and 284 are amicable.
    >>> g(2924, 2620)
    2924 and 2620 are amicable.
    >>> g(1084, 1208)
    1084 and 1208 are not amicable.
    >>> g(5010, 5574)
    5010 and 5574 are not amicable.
    
    '''
    a_divisors = get_divisors(a)
    b_divisors = get_divisors(b)
    if sum(a_divisors) == b and sum(b_divisors) == a:
        print(f"{a} and {b} are amicable.")
    else:
        print(f"{a} and {b} are not amicable.")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
