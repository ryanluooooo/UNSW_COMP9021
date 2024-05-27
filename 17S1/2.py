from random import seed, randint
import sys

def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    >>> f(0, 1, 10)
    Here is L: [6]
    1 element starts with 6
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    2 elements start with 6
    >>> f(1, 2, 100)
    Here is L: [17, 72]
    1 element starts with 1
    1 element starts with 7
    >>> f(2, 3, 1000)
    Here is L: [978, 883, 970]
    1 element starts with 8
    2 elements start with 9
    >>> f(8, 6, 1000)
    Here is L: [232, 379, 985, 384, 129, 197]
    2 elements start with 1
    1 element starts with 2
    2 elements start with 3
    1 element starts with 9
    >>> f(20, 8, 10000)
    Here is L: [2477, 4257, 1663, 5364, 9387, 2775, 442, 6742]
    1 element starts with 1
    2 elements start with 2
    2 elements start with 4
    1 element starts with 5
    1 element starts with 6
    1 element starts with 9
    '''
    seed(arg_for_seed)
    L = [randint(0,max_element) for _ in range(nb_of_elements)]
    print ('Here is L:',L)
    dic = {}
    for e in L:
        if str(e)[0] not in dic.keys():
            dic[str(e)[0]] = 1
        else:
            dic[str(e)[0]] += 1
    keys = sorted(dic.keys())
    for e in keys:
        if dic[e] == 1:
            print(f'{dic[e]} element starts with {e}')
        else:
            print(f'{dic[e]} elements start with {e}')


#    from collections import defaultdict
#    result = defaultdict(int)
#    for e in L:
 #       str_e = str(e)
 #       result[str_e[0]] +=1
  #  if len(result):
  #      for key in sorted(result.keys()):
 #           print(f"{result[key]} element starts with {key}")



if __name__ == '__main__':
    import doctest
    doctest.testmod()
