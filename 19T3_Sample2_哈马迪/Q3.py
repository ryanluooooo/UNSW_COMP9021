# COMP9021 19T3 - Rachid Hamadi
# Sample Exam 2


'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''


class Solution:
    self.mark = []
    self.island = 0

    def recurse(self, grid, i, j):
        if [i, j] in self.mark:
            return
        else:
            self.mark.append([i, j]):
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                self.recurse(grid, i + 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                self.recurse(grid, i, j + 1)
            return

    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if [i, j] not in self.mark:
                    self.island += 1
                    self.recurse(grid, i, j)
        return self.island


def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    
    result = ['']
    if word.rstrip() == '':
        return result
    word_set = set(word)
    for i in range(len(word)):
        if word[i] not in result:
            result.append(word[i])
            start = word[i]
            j = 0
            while j < len(word_set):
                for k in range(i+1,len(word)):
                    if word[k] not in start and start+word[k] not in result:
                        start = start+word[k]
                        result.append(start)
                start = word[i]
                j += 1
    result.sort()
    return result
            
    

# Possibly define another function
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()
