# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.
    
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
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    lines=''
    if word:
        lines = [[word[0]]]
        first = word[0]
        for second in str(word)[1:]:
            if ord(first)+1 == ord(second):
                lines[-1].append(second)
            else:
                lines.append([second])
            first = second
        max_len = 0
        for line in lines:
            if max_len< len(line):
                max_len = len(line)

        for line in lines:
            if len(line)==max_len:
                return (''.join(line))
    else:
        return lines
    
            

                
            
        
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
