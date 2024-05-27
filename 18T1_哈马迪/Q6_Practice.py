def display(square):
    print('\n'.join(' '.join(f'{x:2d}' for x in row) for row in square))

def check_out_square_and_fix_if_corrupted(square):
    '''
    Call "good square" an n x n matrix with n >= 2 consisting of all numbers
    between 1 and n ** 2.
    Call "corrupted square" a good square exactly one of whose entries has been
    replaced by 0.

    Note: marks can be scored by just checking whether the square is good or corrupted,
    without fixing it in case it is corrupted -- but hard coding won't help.
    
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6  4  8
    It is a good square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 10, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6 10  8
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 0],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  0
     6  4  8
    It is a corrupted square, the good square being:
     1  5  7
     2  9  3
     6  4  8
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [2, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     2  9  0 16
     6  4  8 12
    13 14 15  2
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [3, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     3  9  0 16
     6  4  8 12
    13 14 15  2
    It is a corrupted square, the good square being:
     1  5  7 11
     3  9 10 16
     6  4  8 12
    13 14 15  2
    '''
    n = len(square)
    if n < 2 or any(len(line) != n for line in square):
        return False
    print('Here is the square: ')
    display(square)
    good_square = False
    corrupted_square = False
    # Insert your code here

    number = []
    test = set()
    for lst in square:
        for n in lst:
            number.append(n)
    for num in range(1,len(square)*len(square)+1):
        test.add(num)
    
    if set(number) == test:
        print('It is a good square.')
    elif len(set(number) - test) > 1 or set(number) - test != {0} or len(set(number)) != len(square)*len(square):
        print('It is neither a good nor a corrupted square.')
    else:
        lack_letter = list(test - set(number))
        wrong_letter = list(set(number) - test)
        for i in range(len(square)):
            for j in range(len(square)):
                if square[i][j] == wrong_letter[0]:
                    square[i][j] = lack_letter[0] 
        print('It is a corrupted square, the good square being:')
        display(square)

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    '''
    哈马迪的标答
    set1 = set([x for row in square for x in row])
    set2 = set([x for x in range(1,n ** 2 + 1)])
    set3 = set1 - set2
    set4 = set2 - set1
    if len(set3) == 0:
        good_square = True
    else:
        if set3 =={0} and len(set4) == 1:
            corrupted_square = True
            value = list(set4)[0]
            for i in range(len(square)):
                for j in range(len(square[i])):
                    if square[i][j] == 0:
                        square[i][j] = value
                
    if good_square:
        print('It is a good square.')
    else:
        if not corrupted_square:
            print('It is neither a good nor a corrupted square.')
        else:
            print('It is a corrupted square, the good square being:')
            display(square)
    
    '''