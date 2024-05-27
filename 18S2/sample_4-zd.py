from collections import defaultdict, deque
import sys


'''
Determines whether a given sequence of words is a word ladder
from a given word word_1 to a given word word_2, that is,
a sequence of words all in the provided dictionary, of minimal length,
starting with word_1, ending in word_2, and such that two consecutive words
in the sequence differ by exactly one letter.

Assume that word_1 and word_2 are sequences of uppercase letters.

Note that a single test will examine many potential sequences at once,
so no form of hardcoding will achieve anything...

Hint to make the solution efficient enough:
- Check whether the given sequence can be a word ladder because:
   . its first word is word_1;
   . its last word is word_2;
   . any pair of consecutive words are in the dictionary and differ by exactly one letter.
- Then compute the length of some word ladder between word_1 and word_2, if any,
  giving up in case it can no longer be at most equal to the length of the given sequence,
  and check whether it is equal to the length of the given sequence.
'''


dictionary_file = 'dictionary.txt'

def get_words_and_word_relationships():
    try:
        with open(dictionary_file) as dictionary:
            lexicon = set()
            contextual_slots = defaultdict(list)
            for word in dictionary:
                word = word.rstrip()
                lexicon.add(word)
                for i in range(len(word)):
                    contextual_slots[word[: i], word[i + 1: ]].append(word)
            closest_words = defaultdict(set)
            for slot in contextual_slots:
                for i in range(len(contextual_slots[slot])):
                    for j in range(i + 1, len(contextual_slots[slot])):
                        closest_words[contextual_slots[slot][i]].add(contextual_slots[slot][j])
                        closest_words[contextual_slots[slot][j]].add(contextual_slots[slot][i])
            return lexicon, closest_words
    except FileNotFoundError:
        print(f'Could not open {dictionary_file}. Giving up...')
        sys.exit()

def is_word_word_ladder(word_1, word_2, candidate_ladder):
    '''
    >>> is_word_word_ladder('AAA', 'AAA', ['AAA'])
    False
    >>> is_word_word_ladder('DAY', 'MEW', ['DAY', 'DAW', 'DEW', 'MEW'])
    False
    >>> is_word_word_ladder('COLD', 'WARM', ['COLD', 'CALD', 'CARD', 'WARD', 'WARM'])
    False
    >>> is_word_word_ladder('COLD', 'WARM', ['COLD', 'CORD', 'WORD', 'WARD', 'WARP', 'WARM'])
    False
    >>> is_word_word_ladder('TABLE', 'TABLE', ['TABLE'])
    True
    >>> is_word_word_ladder('DAY', 'MEW', ['DAY', 'HAY', 'HEY', 'HEW', 'MEW'])    
    True
    >>> is_word_word_ladder('COLD', 'WARM', ['COLD', 'CORD', 'WORD', 'WARD', 'WARM'])
    True
    '''
    # Note how get_words_and_word_relationships() is called below.
    # Insert your code here
    

if __name__ == '__main__':
    # lexicon is a set that records all words in the dictionary.
    # closest_words is a dictionary that maps any word w in the dictionary
    # to the set of all words that differ from w by exactly one letter.
    import doctest
    doctest.testmod()
