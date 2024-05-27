
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''


    # Insert your code here
    #肯定要构建字典
    #key为面值，value为张数
    #先构建key的list
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    #构建以上面的list为key的字典，value取值先为0
    banknotes = dict.fromkeys(banknote_values, 0)
    #从100开始遍历banknote_values，面值1对应的index是0，100对应的是6
    #所以index初始值为banknote_values长度-1(也就是6)，
    index = len(banknote_values) - 1
    while N > 0 and index >= 0:
        #用N除以面值，得到的商count就是要取几张该面值的币， 余数就变成了下一个N
        count, N = divmod(N, banknote_values[index])
        #当count >0 的时候，把count放到字典中对应面值key的value里
        if count > 0:
            banknotes[banknote_values[index]] = count
        index -= 1

    print('Here are your banknotes:')
    #按照面值从小到大排序，逐行打印
    for value in sorted(banknotes):
        #打印字典中value不是0的
        if banknotes[value]:
            #{ } { } .format(value1, value2)
            #format是个填空的函数，可在{}中填入value
            print('${}: {}'.format(value, banknotes[value]))
        
        
    # Insert your code here
  
                        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
