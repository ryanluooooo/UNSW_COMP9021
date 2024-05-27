# Will be tested only with number an integer.
#
# If number is positive, returns a positive integer.
# If number is negative, returns a negative integer.
#
# The digits of the returned integer are the digits of number
# ordered from largest to smallest.

def reorder(number):
    '''
    >>> reorder(0)
    0
    >>> reorder(2)
    2
    >>> reorder(-33)
    -33
    >>> reorder(202)
    220
    >>> reorder(242242)
    442222
    >>> reorder(-3210123)
    -3322110
    >>> reorder(22659717106393887106)
    99887776665332211100
    '''
    zf=1
    num_str=str(number)
    num_str_list=list(num_str)
    if num_str_list[0]=='-':
        zf=-1
        num_str_list=num_str_list[1:]
    num_str_list.sort(reverse=True)
    result=[]
    if zf==-1:
        result.append('-')
    result.extend(num_str_list)
    result=''.join(result)
    result=int(result)
    print(result)
    # return result
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

if __name__ == '__main__':
    import doctest
    doctest.testmod()
