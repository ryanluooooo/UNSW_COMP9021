# COMP9021 24T1 - Rachid Hamadi
# Sample Exam Question 3


'''
Write a function that accepts a strictly positive integer greater or equal to 2 and "not too large" 
and displays its decomposition into prime factors.

Will be tested with n at least equal to 2, and "not too large".
'''

def f(n):   
    '''
    >>> f(2)
    The decomposition of 2 into prime factors reads:
       2 = 2
    >>> f(3)
    The decomposition of 3 into prime factors reads:
       3 = 3
    >>> f(4)
    The decomposition of 4 into prime factors reads:
       4 = 2^2
    >>> f(5)
    The decomposition of 5 into prime factors reads:
       5 = 5
    >>> f(6)
    The decomposition of 6 into prime factors reads:
       6 = 2 x 3
    >>> f(8)
    The decomposition of 8 into prime factors reads:
       8 = 2^3
    >>> f(10)
    The decomposition of 10 into prime factors reads:
       10 = 2 x 5
    >>> f(15)
    The decomposition of 15 into prime factors reads:
       15 = 3 x 5
    >>> f(100)
    The decomposition of 100 into prime factors reads:
       100 = 2^2 x 5^2
    >>> f(5432)
    The decomposition of 5432 into prime factors reads:
       5432 = 2^3 x 7 x 97
    >>> f(45103)
    The decomposition of 45103 into prime factors reads:
       45103 = 23 x 37 x 53
    >>> f(45100)
    The decomposition of 45100 into prime factors reads:
       45100 = 2^2 x 5^2 x 11 x 41
    '''
    factors = {}

    # Insert your code here
    
    print(f'The decomposition of {n} into prime factors reads:')
    print('  ', n, '=', end = ' ')
    print(' x '.join(factors[x] == 1 and str(x) or f'{x}^{factors[x]}'for x in sorted(factors)))
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()