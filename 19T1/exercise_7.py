
# POSSIBLY DEFINE OTHER
from itertools import permutations


def subnumbers_whose_digits_add_up_to(number, sum_of_digits):
    '''
    You can assume that "number" consists of digits not equal to 0
    and that "sum_of_digits" is an integer.

    A solution is obtained by possibly deleting some digits in "number"
    (keeping the order of the remaining digits) so that the sum of
    of the remaining digits is equal to "sum_of_digits".

    The solutions are listed from smallest to largest, with no duplicate.

    >>> subnumbers_whose_digits_add_up_to(13, 2)
    []
    >>> subnumbers_whose_digits_add_up_to(222, 2)
    [2]
    >>> subnumbers_whose_digits_add_up_to(123, 6)
    [123]
    >>> subnumbers_whose_digits_add_up_to(222, 4)
    [22]
    >>> subnumbers_whose_digits_add_up_to(1234, 5)
    [14, 23]
    >>> subnumbers_whose_digits_add_up_to(12341234, 4)
    [4, 13, 22, 31, 112, 121]
    >>> subnumbers_whose_digits_add_up_to(121212, 5)
    [122, 212, 221, 1112, 1121, 1211]
    >>> subnumbers_whose_digits_add_up_to(123454321, 10)
    [145, 154, 235, 244, 253, 343, 352, 442, 451, 532, 541, 1234, 1243, \
1252, 1342, 1351, 1432, 1441, 1531, 2332, 2341, 2431, 2521, 3421, \
4321, 12331, 12421, 13321]
    '''
    solution=sorted([''.join(x) for i in range(0,len(str(number))) for x in permutations(str(sum_of_digits),str(number)) if ''.join(x) in str(number)])
    print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(subnumbers_whose_digits_add_up_to(123, 6))
    # print(sorted(subnumbers_whose_digits_add_up_to(123454321, 10)))
