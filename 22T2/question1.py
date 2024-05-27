# A sequence of identical digits is collapsed to one digit
# in the returned integer.
#
# You can assume that the function is called with an integer
# as argument.


def collapse(number):
    '''
    >>> collapse(0)
    0
    >>> collapse(-0)
    0
    >>> collapse(9)
    9
    >>> collapse(-9)
    -9
    >>> collapse(12321)
    12321
    >>> collapse(-12321)
    -12321
    >>> collapse(-1111222232222111)
    -12321
    >>> collapse(1155523335551116111666)
    152351616
    >>> collapse(-900111212777394440300)
    -9012127394030
    '''
    num_str=str(number)
    num_list=list(num_str)

    point=num_list[0]
    result = [point]
    for i in range(len(num_list)):
        if num_list[i]==point:
            continue
        else:
            point=num_list[i]
            result.append(point)
    result_str=''.join(result)
    result_int=int(result_str)
    return result_int
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()