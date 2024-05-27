
# 19T1 pre-final

def rearrange(number):
    '''
    Returns an integer consisting of all nonzero digits in "number",
    from smallest to largest.

    You can assume that "number" is a valid strictly positive integer.
    
    >>> rearrange(1)
    1
    >>> rearrange(200)
    2
    >>> rearrange(395)
    359
    >>> rearrange(10029001)
    1129
    >>> rearrange(301302004)
    12334
    >>> rearrange(9409898038908908934890)
    33448888889999999
    '''
    
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    #print(type(number))
    a = str(number)
    #print(type(a))
    b = sorted(a)
    #print(b)
    c = "".join(b)
    #print(c)
    #print(type(c))
    d = c.strip('0')
    #print(d)

    print("".join(sorted(str(number))).strip('0'))
    
    
    
    
    
   
    
    
 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
