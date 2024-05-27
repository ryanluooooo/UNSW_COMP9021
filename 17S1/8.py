'''A text file consists of sentences.
   A sentence consists of words, possibly directly followed by a comma,
   except for the last word which is directly followed by a full stop.
   Words are separated by spaces.

   Recall that dir(str) outputs all string methods.
'''

def f(filename):
    '''
    >>> f('text_file_1.txt')
    There are 2 sentence(s).
    The shortest sentence has 31 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 9 character(s).
    >>> f('text_file_2.txt')
    There are 4 sentence(s).
    The shortest sentence has 6 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    >>> f('text_file_3.txt')
    There are 1 sentence(s).
    The shortest sentence has 30 word(s).
    The longest sentence has 30 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    '''
#input your code
    with open(filename,"r") as file:
        lines = file.readlines()
        print(lines)


if __name__ == '__main__':
    import doctest
    doctest.testmod()