# COMP9021 22T3 - Rachid Hamadi
# Final Exam Question 3

'''
You might find the ord() function useful.
'''


def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''


    # REPLACE return WITH YOUR CODE
    if word == '':
        return word
    
    consecutive_letter = []
    temp_str = ''
    for letter in word:
        if len(temp_str) == 0 or ord(letter)-1 == ord(temp_str[-1]):
            temp_str += letter
        else:
            consecutive_letter.append(temp_str)
            temp_str = letter
    consecutive_letter.append(temp_str)

    left_max = 0
    for s in consecutive_letter:
        if len(s) > left_max:
            left_max = len(s)
            result = s

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()