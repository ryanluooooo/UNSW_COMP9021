import sys
from math import factorial


def f(n):
    '''
    >>> f(0)
    0 factorial is 1
    It has 1 digit, the trailing 0's excepted
    >>> f(4)
    4 factorial is 24
    It has 2 digits, the trailing 0's excepted
    >>> f(6)
    6 factorial is 720
    It has 2 digits, the trailing 0's excepted
    >>> f(10)
    10 factorial is 3628800
    It has 5 digits, the trailing 0's excepted
    >>> f(20)
    20 factorial is 2432902008176640000
    It has 15 digits, the trailing 0's excepted
    >>> f(30)
    30 factorial is 265252859812191058636308480000000
    It has 26 digits, the trailing 0's excepted
    >>> f(40)
    40 factorial is 815915283247897734345611269596115894272000000000
    It has 39 digits, the trailing 0's excepted
    '''
    if n < 0:
        sys.exit()
    n_factorial = factorial(n)
    nb_of_digits_excluding_the_trailing_0s = 0
    # Insert your code here
    n_f = str(n_factorial)
    if len(n_f)==1:
        t_0 = 0
    else:
        t_0 = min(i for i in range(1,len(n_f)) if n_f[-i] != '0')-1
      

    nb_of_digits_excluding_the_trailing_0s = len(n_f)-t_0
    if nb_of_digits_excluding_the_trailing_0s == 1:
        print(n,'factorial is', n_factorial)
        print("It has", nb_of_digits_excluding_the_trailing_0s,"digit, the trailing 0's excepted")
    else:
        print(n,'factorial is', n_factorial)
        print("It has", nb_of_digits_excluding_the_trailing_0s,"digits, the trailing 0's excepted")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
