# COMP9021 24T1 - Rachid Hamadi
# Sample Exam Question 8


'''
Write a function that accepts a string of DISTINCT UPPERCASE letters only called letters 
and displays all pairs of words using all (distinct) letters in letters.

Please note that the words need to be valid. Use the provided dictionary.txt to check the validity of words.  

Will be tested with letters, a string of DISTINCT UPPERCASE letters only.
'''

from itertools import permutations

def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []

    # Insert your code here
    with open(dictionary) as words_file:
        valid_words = set()
        for word in words_file:
            valid_words.add(word.rstrip())
    
    for w1_len in range(1,len(letters)):
        for w1 in permutations(letters,w1_len):
            w1 = ''.join(w1)
            if w1 in valid_words:
                remaining_letter = set(letters) - set(w1)
                for w2 in permutations(remaining_letter,len(letters)-w1_len):
                    w2 = ''.join(w2)
                    if w2 in valid_words and w1 < w2:
                        solutions.append((w1,w2))
    
    solutions = sorted(solutions)


    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()