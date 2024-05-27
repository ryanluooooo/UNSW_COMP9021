
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here
    if not {number for line in square for number in line} == set(range(1,n**2+1)):
        return False
    


    
    if not_good_line(square,n):
        return False

    return True

def not_good_line(square,n):
    L = [None]*n
    L2 = [None]*n
    for i in range(n):
        L[i] = sum(square[i])
    dia = sum(square[i][i] for i in range(n))
    dia2 = sum(square[i][n-1-i] for i in range(n))


    square2 = [[square[j][i] for j in range(n)] for i in range(n)]

    for k in range(n):
        L2[k] = sum(square2[k])
    L3 = L+L2
    L3.append(dia)
    L3.append(dia2)
    if len(set(L3)) == len(L3):
        return False
    else:
        return True
        


    
# Possibly define other functions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
