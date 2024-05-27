# Final Exam - Question 3

# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def f(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when
    z is reached.

    You can assume that width and height are strictly positive integers

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

    # INSERT YOUR CODE HERE
    current_char = ord('a')
    for row in range(height):
        line = []
        for col in range(width):
            line.append(chr(current_char))
            current_char += 1
            if current_char > ord('z'):
                current_char = ord('a')
        
        if row % 2 == 1:
            line = line[::-1]
            #line.reverse()
        print(''.join(line))


if __name__ == '__main__':
    import doctest
    doctest.testmod()