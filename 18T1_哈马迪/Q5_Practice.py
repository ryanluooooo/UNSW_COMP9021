def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    # Insert your code here
    con_list = []
    temp_str = ''
    for w in word:
        if len(temp_str) == 0 or ord(w)-1 == ord(temp_str[-1]):
            temp_str += w
        else:
            con_list.append(temp_str)
            temp_str = w
    con_list.append(temp_str)
    
    max_length = 0
    for i in con_list:
        if len(i) > max_length:
            max_length = len(i)
            left_str = i
    print(f'The longest substring of consecutive letters has a length of {max_length}.')
    print(f'The leftmost such substring is {left_str}.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()