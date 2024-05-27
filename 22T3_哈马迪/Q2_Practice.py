# COMP9021 22T3 - Rachid Hamadi
# Final Exam Question 2

def redistribute(list_of_lists):
    '''
    list_of_lists being a list of n lists of length l1, ..., ln,
    returns a list of n lists of length l1, ..., ln consisting of
    all elements in list_of_lists ordered from smallest to largest.

    You can assume that the lists in list_of_lists are lists of integers.

    >>> redistribute([[]])
    [[]]
    >>> redistribute([[3, 1, 10, 5, 1, 10, 8]])
    [[1, 1, 3, 5, 8, 10, 10]]
    >>> redistribute([[2], [1], [2], [4]])
    [[1], [2], [2], [4]]
    >>> redistribute([[3, 40], [0], [7]])
    [[0, 3], [7], [40]]
    >>> redistribute([[32], [3, 40, 7], [40, 11]])
    [[3], [7, 11, 32], [40, 40]]
    >>> redistribute([[97, 21], [65], [9, 25, 24], [64], [73, 38, 98, 50]])
    [[9, 21], [24], [25, 38, 50], [64], [65, 73, 97, 98]]
    '''


    # REPLACE return WITH YOUR CODE
    extract_num = []
    for lst in list_of_lists:
        extract_num += lst
    extract_num = sorted(extract_num)
    
    result = []
    used = 0
    for lst in list_of_lists:
        result.append(extract_num[used : used+len(lst)])
        used += len(lst)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()