# -*- encoding:utf-8 -*-
# For an example, the rotations of 14238 are
# 14238, 42381, 23814, 38142 and 81423.
# - The smallest prime factor of 14238 is 2 (14238 = 2 x 7119)
# - The smallest prime factor of 42381 is 3 (42381 = 3 x 14127)
# - The smallest prime factor of 23814 is 2 (23814 = 2 x 11907)
# - The smallest prime factor of 38142 is 2 (38142 = 2 x 19071)
# - The smallest prime factor of 81423 is 3 (81423 = 3 x 27141)
# Hence the largest number that is the smallest prime factor
# of a rotation of 14238 is 3.
#
# Leading 0s in a rotation are ignored.
#
# Solutions are output from smallest to largest.
#
# You can assume that the function is called with an integer
# at least equal to 2 as argument.


from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def largest_smallest_prime_factor_in_rotations(n):
    '''
    >>> largest_smallest_prime_factor_in_rotations(2)
    The largest number that is the smallest prime factor
    of a rotation of 2 is 2.
    This is for the following rotations of 2:
    2, equal to 2 x 1
    >>> largest_smallest_prime_factor_in_rotations(23509)
    The largest number that is the smallest prime factor
    of a rotation of 23509 is 50923.
    This is for the following rotations of 23509:
    50923, equal to 50923 x 1
    >>> largest_smallest_prime_factor_in_rotations(10_000)
    The largest number that is the smallest prime factor
    of a rotation of 10000 is 2.
    This is for the following rotations of 10000:
    10, equal to 2 x 5
    100, equal to 2 x 50
    1000, equal to 2 x 500
    10000, equal to 2 x 5000
    >>> largest_smallest_prime_factor_in_rotations(34305)
    The largest number that is the smallest prime factor
    of a rotation of 34305 is 3.
    This is for the following rotations of 34305:
    5343, equal to 3 x 1781
    34305, equal to 3 x 11435
    43053, equal to 3 x 14351
    >>> largest_smallest_prime_factor_in_rotations(357427)
    The largest number that is the smallest prime factor
    of a rotation of 357427 is 7.
    This is for the following rotations of 357427:
    357427, equal to 7 x 51061
    427357, equal to 7 x 61051
    574273, equal to 7 x 82039
    >>> largest_smallest_prime_factor_in_rotations(4780)
    The largest number that is the smallest prime factor
    of a rotation of 4780 is 13.
    This is for the following rotations of 4780:
    8047, equal to 13 x 619
    >>> largest_smallest_prime_factor_in_rotations(1234567)
    The largest number that is the smallest prime factor
    of a rotation of 1234567 is 191.
    This is for the following rotations of 1234567:
    2345671, equal to 191 x 12281
    '''
    smallest_prime_factor = 1
    winners = []
    # INSERT YOUR CODE HERE
    print('The largest number that is the smallest prime factor\n'
          f'of a rotation of {n} is {smallest_prime_factor}.\n'
          f'This is for the following rotations of {n}:'
         )
    for winner in winners:
        print(f'{winner}, equal to',
              smallest_prime_factor, 'x', winner // smallest_prime_factor
             )


if __name__ == '__main__':
    import doctest
    doctest.testmod()