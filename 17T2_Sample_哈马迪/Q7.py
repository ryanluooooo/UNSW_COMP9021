
# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def f(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> f(1, 1)
    a
    >>> f(2, 3)
    ab
    dc
    ef
    >>> f(3, 2)
    abc
    fed
    >>> f(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    if width <= 0 or height <= 0:
        sys.exit()
    # Insert your code here
    c = ord('a')
    A_code = ord('a')
    for i in range(height):
        if not i%2:
            for j in range(width):
                print(chr(c), end = '')
                c = (c - A_code + 1)%26 +A_code
        else:
            for j in range(width):
                print(chr(c), end = '')
                c = (c - A_code - 1)%26 +A_code
        print()
        if not i%2:
            c = (c - A_code + width-1)%26 +A_code
        else:
            c = (c - A_code + width+1)%26 +A_code
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
