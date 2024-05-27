# COMP9021 20T3 - Rachid Hamadi
# Final Exam - Question 6

def found_word_in(word, filename):
    '''
    Returns True or False depending on whether "word" can be read
    from the grid represented in the provided file "filename",
    assumed to be stored in the working directory.

    There can be spaces anywhere in the file. In particular,
    letters on a given line of the file can be separated by an
    arbitrary number of spaces (possibly none), and there can be
    lines with nothing but spaces.

    Words are to be read HORIZONTALLY FROM LEFT TO RIGHT,
    or VERTICALLY FROM TOP TO BOTTOM,
    or DIAGONALLY FROM TOP LEFT TO BOTTOM RIGHT


    >>> found_word_in('MANGANESE', 'word_search_1.txt'),\
        found_word_in('GOLD', 'word_search_1.txt')
    (True, False)
    >>> found_word_in('NICKEL', 'word_search_1.txt'),\
        found_word_in('SILVER', 'word_search_1.txt')
    (True, True)
    >>> found_word_in('ZINC', 'word_search_1.txt'),\
        found_word_in('RUBIS', 'word_search_1.txt')
    (True, False)
    >>> found_word_in('BANANA', 'word_search_2.txt'),\
        found_word_in('RASPBERRY', 'word_search_2.txt')
    (True, True)
    '''

    pass
    # REPLACE "pass" ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()


