# COMP9021 22T3 - Rachid Hamadi
# Final Exam Question 4

'''
No point to hard code for small values of n, will be tested
only for large enough values...
'''


def pascal_triangle_line(n):
    '''
    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''

    # REPLACE return WITH YOUR CODE
    if n == 1:
        return [1]

    previous_line = pascal_triangle_line(n-1)
    result = [1]
    for n in range(len(previous_line)-1):
        result.append(previous_line[n]+previous_line[n+1])
    
    result.append(1)

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()