from collections import defaultdict

def words(text):
    '''
    You can assume that "text" contains nothing but words that consist of nothing but letters
    (no apostrophe, no hyphen, no quote symbol...), possibly followed by commas, full stops,
    colons, semicolons, question marks and exclamation marks (all with no space before, and
    with a space after if not the last character).
    Prints out lists of words with all uppercase letters changed to lowercase,
    with no duplicate, in lexicographic order, grouped together by number of letters,
    from smallest number of letters to largest number of letters.
    Observe that each list of words is preceded with 4 spaces.
    
    >>> words('Twelve will, believe me, be quite enough for your purpose.')
    Words of length 2:
        ['be', 'me']
    Words of length 3:
        ['for']
    Words of length 4:
        ['will', 'your']
    Words of length 5:
        ['quite']
    Words of length 6:
        ['enough', 'twelve']
    Words of length 7:
        ['believe', 'purpose']
    >>> words('What was that? What does the Bishop mean?')
    Words of length 3:
        ['the', 'was']
    Words of length 4:
        ['does', 'mean', 'that', 'what']
    Words of length 6:
        ['bishop']
    >>> words('You must not fall into the common error of mistaking these simpletons '\
              'for liars and hypocrites. They believe honestly and sincerely that their '\
              'diabolical inspiration is divine. Therefore you must be on your guard against '\
              'your natural compassion. You are all, I hope, merciful men: how else could you '\
              'have devoted your lives to the service of our gentle Savior? You are going '\
              'to see before you a young girl, pious and chaste; for I must tell you, gentlemen, '\
              'that the things said of her by our English friends are supported by no evidence, '\
              'whilst there is abundant testimony that her excesses have been excesses of religion '\
              'and charity and not of worldliness and wantonness.')
    Words of length 1:
        ['a', 'i']
    Words of length 2:
        ['be', 'by', 'is', 'no', 'of', 'on', 'to']
    Words of length 3:
        ['all', 'and', 'are', 'for', 'her', 'how', 'men', 'not', 'our', 'see', 'the', 'you']
    Words of length 4:
        ['been', 'else', 'fall', 'girl', 'have', 'hope', 'into', 'must', 'said', 'tell', 'that', 'they', 'your']
    Words of length 5:
        ['could', 'error', 'going', 'guard', 'liars', 'lives', 'pious', 'their', 'there', 'these', 'young']
    Words of length 6:
        ['before', 'chaste', 'common', 'divine', 'gentle', 'savior', 'things', 'whilst']
    Words of length 7:
        ['against', 'believe', 'charity', 'devoted', 'english', 'friends', 'natural', 'service']
    Words of length 8:
        ['abundant', 'evidence', 'excesses', 'honestly', 'merciful', 'religion']
    Words of length 9:
        ['gentlemen', 'mistaking', 'sincerely', 'supported', 'testimony', 'therefore']
    Words of length 10:
        ['compassion', 'diabolical', 'hypocrites', 'simpletons', 'wantonness']
    Words of length 11:
        ['inspiration', 'worldliness']
    '''
    print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
