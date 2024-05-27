# COMP9021 22T3 - Rachid Hamadi
# Final Exam Question 8

def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.

    Conjunctions of inputs will be tested, so hard coding will not help.

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


    # REPLACE return WITH YOUR CODE
    numbers = []
    for lst in square:
        numbers += lst
    
    if set(numbers) != set(range(1,len(square) ** 2 + 1)):
        return False
    
    sum1 = []
    for lst in square:
        line_sum = 0
        for number in lst:
           line_sum += number
        sum1.append(line_sum) 
    #print(sum1)

    sum2 = [] 
    for i in range(len(square)):
        col = []
        for lst in square:
            col.append(lst[i])
        sum2.append(sum(col))
    #print(sum2)

    sum3 = []
    for i in range(len(square)):
        for j in range(len(square)):
            if i == j:
                sum3.append(square[i][j])
    sum3 = [sum(sum3)]
    #print(sum3)

    sum4 = []
    for i in range(len(square)):
        for j in range(len(square)):
            if i+j == len(square)-1:
                sum4.append(square[i][j])
    sum4 = [sum(sum4)]
    #print(sum4)

    all_sum = sum1 + sum2 + sum3 + sum4
    return len(set(all_sum)) == len(all_sum)

    # POSSIBLY DEFINE OTHER FUNCTIONS


if __name__ == '__main__':
    import doctest
    doctest.testmod()