# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    # print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    # 1.两种,边打印，边输出 2.放到list 一起打印
    a_code = ord("a")
    c = a_code
    for i in range(height):
        line = ''
        for j in range(width):
            line+=(chr((c-a_code)%26+a_code))
            c+=1


        if i % 2 == 0:
            print(line)
        else:
            print(line[::-1])
    
            
    
        
        
        
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
